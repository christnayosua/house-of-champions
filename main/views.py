# Penambahan import untuk implementasi penggunaan data dari cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Penambahan import modul decorator login_required dari sistem autentikasi milik Django
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products

# Penambahan import modul untuk request pengiriman data ke dalam bentuk XML dan JSON
from django.http import HttpResponse
from django.core import serializers

# Penambahan import modul untuk membuat fungsi dan form registrasi serta fungsi login dan logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Penambahan import untuk AJAX dan JSON response
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Dummy function
def product_us(request, id):
    return render(request)

def contact_us(request, id):
    return render(request)

# Penambahan function untuk delete_products
def delete_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# Menambahkan function untuk edit_products
def edit_products(request, id):
    products = get_object_or_404(Products, pk=id)
    form = ProductsForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

# Function untuk logout
def logout_user(request):
    # Implementasi untuk logout user
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    # Menghapus cookie -> pembaruan last_login
    response.delete_cookie('last_login')
    return response

# Function untuk mengautentikasi pengguna yang login 
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Konfigurasi untuk implementasi penggunaan data dari cookies
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

# Function untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika ada di-submit dari form 
def register(request):
    form = UserCreationForm()

    # Menerima request dari user
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Function untuk mengirimkan data dalam bentuk XML
def show_xml(request):
     products_list = Products.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

# Function untuk mengirimkan data dalam bentuk JSON
def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

# Mengirimkan data dalam bentuk XML berdasarkan ID
def show_xml_by_id(request, products_id):
   try:
       products_list = Products.objects.filter(pk=products_id)
       xml_data = serializers.serialize("xml", products_list)
       return HttpResponse(xml_data, content_type="application/xml")
    # Handle apabila tidak muncul
   except Products.DoesNotExist:
       return HttpResponse(status=404)

# Mengirimkan data dalam bentuk JSON berdasarkan ID
def show_json_by_id(request, products_id):
   try:
       products_list = Products.objects.get(pk=products_id)
       json_data = serializers.serialize("json", [products_list])
       return HttpResponse(json_data, content_type="application/json")
    # Handle apabila tidak muncul 
   except Products.DoesNotExist:
       return HttpResponse(status=404)

# Decorator login_required untuk show_main
@login_required(login_url='/login')
def show_main(request):
    # Implementasi untuk melakukan 'penyaringan' terhadap produk sesuai toko
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products_list = Products.objects.all()
    else:
        products_list = Products.objects.filter(user=request.user)

    context = {
        'applicationName' : 'House Of Champions',
        'npm' : '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'products_list': products_list,
        # Penambahan variabel untuk last_login
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Konfigurasi untuk menghubungkan satu products dengan satu user
        # commit = false berperan agar Django tidak langsung menyimpan objek hasil form ke database,
        # hal tersebut memungkinkan agar developer dapat melakukan modifikasi pada objek sebelum disimpan
        products_entry = form.save(commit = False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

# Decorator untuk fungsi show_products
@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

# Menambahkan fitur khusus ajax
# View untuk menambah produk dengan AJAX
@csrf_exempt
@require_http_methods(["POST"])
@login_required(login_url='/login')
def create_products_ajax(request):
    if request.method == 'POST':
        # Menggunakan ProductsForm untuk validasi
        form = ProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Product successfully added!',
                'data': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'category': product.category,
                    'stock': product.stock,
                    'rating': product.rating,
                    'views': product.views,
                    'user': product.user.username
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid data',
                'errors': form.errors
            }, status=400)
    return HttpResponseBadRequest("Invalid request method")

# View untuk menghapus produk dengan AJAX
@csrf_exempt
@require_http_methods(["DELETE"])
@login_required(login_url='/login')
def delete_products_ajax(request, id):
    if request.method == 'DELETE':
        try:
            product = get_object_or_404(Products, pk=id, user=request.user)
            product.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Product successfully deleted!'
            })
        except Products.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Product not found or you do not have permission to delete it'
            }, status=404)

# View untuk mengedit produk dengan AJAX
@csrf_exempt
@require_http_methods(["POST", "GET"])
@login_required(login_url='/login')
def edit_products_ajax(request, id):
    product = get_object_or_404(Products, pk=id, user=request.user)
    
    if request.method == 'GET':
        # Return product data for editing
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'rating': float(product.rating),
            'views': product.views
        })
    
    elif request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Product successfully updated!',
                'data': {
                    'id': product.id,
                    'name': product.name,
                    'price': float(product.price),
                    'description': product.description,
                    'category': product.category,
                    'stock': product.stock,
                    'rating': float(product.rating),
                    'views': product.views
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid data',
                'errors': form.errors
            }, status=400)

# View untuk mendapatkan data produk dalam JSON (AJAX)
@login_required(login_url='/login')
def get_products_json(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "all":
        products = Products.objects.all().order_by('-id')
    else:
        products = Products.objects.filter(user=request.user).order_by('-id')
    
    products_data = []
    for product in products:
        products_data.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'rating': float(product.rating),
            'views': product.views,
            'user': product.user.username,
            'can_edit': product.user == request.user  # Check if current user can edit this product
        })
    
    return JsonResponse(products_data, safe=False)

# View untuk increment views dengan AJAX
@csrf_exempt
@require_http_methods(["POST"])
@login_required(login_url='/login')
def increment_views_ajax(request, id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Products, pk=id)
            product.increment_views()
            return JsonResponse({
                'status': 'success',
                'views': product.views
            })
        except Products.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Product not found'
            }, status=404)

# Modifikasi show_main untuk mendukung AJAX
@login_required(login_url='/login')
def show_main(request):
    context = {
        'applicationName': 'House Of Champions',
        'npm': '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)