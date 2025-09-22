# Penambahan import untuk implementasi penggunaan data dari cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Penambahan import modul decorator login_required dari sistem autentikasi milik Django
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForm
from main.models import Items

# Penambahan import modul untuk request pengiriman data ke dalam bentuk XML dan JSON
from django.http import HttpResponse
from django.core import serializers

# Penambahan import modul untuk membuat fungsi dan form registrasi serta fungsi login dan logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
     items_list = Items.objects.all()
     xml_data = serializers.serialize("xml", items_list)
     return HttpResponse(xml_data, content_type="application/xml")

# Function untuk mengirimkan data dalam bentuk JSON
def show_json(request):
    items_list = Items.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

# Mengirimkan data dalam bentuk XML berdasarkan ID
def show_xml_by_id(request, items_id):
   try:
       items_list = Items.objects.filter(pk=items_id)
       xml_data = serializers.serialize("xml", items_list)
       return HttpResponse(xml_data, content_type="application/xml")
    # Handle apabila tidak muncul
   except Items.DoesNotExist:
       return HttpResponse(status=404)

# Mengirimkan data dalam bentuk JSON berdasarkan ID
def show_json_by_id(request, items_id):
   try:
       items_list = Items.objects.get(pk=items_id)
       json_data = serializers.serialize("json", [items_list])
       return HttpResponse(json_data, content_type="application/json")
    # Handle apabila tidak muncul 
   except Items.DoesNotExist:
       return HttpResponse(status=404)

# Decorator login_required untuk show_main
@login_required(login_url='/login')
def show_main(request):
    # Implementasi untuk melakukan 'penyaringan' terhadap produk sesuai toko
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        items_list = Items.objects.all()
    else:
        items_list = Items.objects.filter(user=request.user)

    context = {
        'applicationName' : 'House Of Champions',
        'npm' : '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'items_list': items_list,
        # Penambahan variabel untuk last_login
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_items(request):
    form = ItemsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Konfigurasi untuk menghubungkan satu news dengan satu user
        # commit = false berperan agar Django tidak langsung menyimpan objek hasil form ke database,
        # hal tersebut memungkinkan agar developer dapat melakukan modifikasi pada objek sebelum disimpan
        items_entry = form.save(commit = False)
        items_entry.user = request.user
        items_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)

# Decorator untuk fungsi show_items
@login_required(login_url='/login')
def show_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.increment_views()

    context = {
        'items': items
    }

    return render(request, "items_detail.html", context)