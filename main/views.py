# Penambahan import untuk implementasi penggunaan data dari cookies
import datetime
import json
# NOTE: gunakan django.utils.timezone bukan time.timezone
from django.utils import timezone

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

# Penambahan import modul decorator login_required dari sistem autentikasi milik Django
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products

# Penambahan import modul untuk request pengiriman data ke dalam bentuk XML dan JSON
from django.core import serializers

# Penambahan import modul untuk membuat fungsi dan form registrasi serta fungsi login dan logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Import tambahan untuk menampilkan data di halaman utama menggunakan AJAX
from django.views.decorators.http import require_POST, require_http_methods

# Penambahan import untuk melindungi aplikasi web dari XSS
from django.utils.html import strip_tags

# import tambahan untuk render ke bentuk string
from django.template.loader import render_to_string


# -----------------------------------------
# Function untuk mendapatkan data produk dalam bentuk HTML (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
def get_products_html(request):
    """Mengembalikan HTML daftar produk untuk AJAX refresh"""
    try:
        filter_type = request.GET.get("filter", "all")
        
        if filter_type == "all":
            products_list = Products.objects.all().order_by('-created_at')
        else:
            products_list = Products.objects.filter(user=request.user).order_by('-created_at')
        
        # Render template partial untuk daftar produk
        html = render_to_string("partials/products_list.html", {
            'products_list': products_list
        }, request=request)
        
        return JsonResponse({
            'success': True,
            'html': html,
            'count': products_list.count()
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load products: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk mendapatkan form create product (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
def get_create_form(request):
    """Mengembalikan HTML form create product untuk modal"""
    try:
        form = ProductsForm()
        html = render_to_string("partials/products_form_modal.html", {
            'form': form,
            'form_title': 'Add New Product',
            'submit_url': reverse('main:add_products_entry_ajax'),
            'submit_text': 'Add Product'
        }, request=request)
        return JsonResponse({'success': True, 'html': html})
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load form: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk mendapatkan form edit product (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
def get_edit_form(request, id):
    """Mengembalikan HTML form edit product untuk modal"""
    try:
        products = get_object_or_404(Products, pk=id)
        
        # Permission check
        if products.user and request.user != products.user:
            return JsonResponse({
                'success': False, 
                'message': 'You are not authorized to edit this product'
            }, status=403)
            
        form = ProductsForm(instance=products)
        html = render_to_string("partials/products_form_modal.html", {
            'form': form,
            'products': products,
            'form_title': 'Edit Product',
            'submit_url': reverse('main:edit_products', args=[id]),
            'submit_text': 'Update Product'
        }, request=request)
        return JsonResponse({'success': True, 'html': html})
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load form: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk mendapatkan konfirmasi delete (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
def get_delete_confirm(request, id):
    """Mengembalikan HTML modal konfirmasi delete"""
    try:
        products = get_object_or_404(Products, pk=id)
        
        # Permission check
        if products.user and request.user != products.user:
            return JsonResponse({
                'success': False, 
                'message': 'You are not authorized to delete this product'
            }, status=403)
            
        html = render_to_string("partials/delete_confirm_modal.html", {
            'products': products
        }, request=request)
        return JsonResponse({'success': True, 'html': html})
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load confirmation: {str(e)}'
        }, status=500)


# -----------------------------------------
# Penambahan function untuk add_products_entry_ajax
# -----------------------------------------
@login_required(login_url='/login')
@require_POST
def add_products_entry_ajax(request):
    """Handle AJAX request untuk create product"""
    try:
        # Support both JSON body and form-data
        if request.content_type == 'application/json':
            payload = json.loads(request.body)
            title = strip_tags(payload.get("title", "").strip())
            content = strip_tags(payload.get("content", "").strip())
            category = payload.get("category", "")
            thumbnail = payload.get("thumbnail", "")
            is_featured = payload.get("is_featured", False)
        else:
            # form-data or urlencoded
            title = strip_tags(request.POST.get("title", "").strip())
            content = strip_tags(request.POST.get("content", "").strip())
            category = request.POST.get("category", "")
            thumbnail = request.POST.get("thumbnail", "")
            is_featured = request.POST.get("is_featured") in ("on", "true", "1", True)
    
        # Validation
        if not title:
            return JsonResponse({
                'success': False, 
                'message': 'Product title is required'
            }, status=400)
            
        if not content:
            return JsonResponse({
                'success': False, 
                'message': 'Product description is required'
            }, status=400)
    
        form = ProductsForm({
            'title': title,
            'content': content,
            'category': category,
            'thumbnail': thumbnail,
            'is_featured': is_featured,
        })
        
        if form.is_valid():
            prod = form.save(commit=False)
            # Associate user if authenticated
            if request.user.is_authenticated:
                prod.user = request.user
            prod.save()

            # Return success response dengan data produk baru
            return JsonResponse({
                'success': True, 
                'message': 'Product added successfully!',
                'product_id': str(prod.id),
                'product_title': prod.title
            }, status=201)
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'success': False, 
                'message': 'Please correct the errors below',
                'errors': errors
            }, status=400)
            
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to create product: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk delete_products (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
@require_POST
def delete_products(request, id):
    """Handle AJAX request untuk delete product"""
    try:
        products = get_object_or_404(Products, pk=id)
        product_title = products.title
        
        # Permission check
        if products.user and request.user != products.user:
            return JsonResponse({
                'success': False, 
                'message': 'You are not authorized to delete this product'
            }, status=403)

        products.delete()
        return JsonResponse({
            'success': True, 
            'message': f'Product "{product_title}" deleted successfully!',
            'product_id': str(id)
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to delete product: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk edit_products (AJAX)
# -----------------------------------------
@login_required(login_url='/login')
@require_http_methods(["POST"])
def edit_products(request, id):
    """Handle AJAX request untuk update product"""
    try:
        products = get_object_or_404(Products, pk=id)

        # Permission check
        if products.user and request.user != products.user:
            return JsonResponse({
                'success': False, 
                'message': 'You are not authorized to edit this product'
            }, status=403)

        # Support JSON or form-data
        if request.content_type == 'application/json':
            payload = json.loads(request.body)
            data = {
                'title': strip_tags(payload.get('title', products.title).strip()),
                'content': strip_tags(payload.get('content', products.content).strip()),
                'category': payload.get('category', products.category),
                'thumbnail': payload.get('thumbnail', products.thumbnail),
                'is_featured': payload.get('is_featured', products.is_featured),
            }
        else:
            data = {
                'title': strip_tags(request.POST.get('title', products.title).strip()),
                'content': strip_tags(request.POST.get('content', products.content).strip()),
                'category': request.POST.get('category', products.category),
                'thumbnail': request.POST.get('thumbnail', products.thumbnail),
                'is_featured': request.POST.get('is_featured', products.is_featured) in ("on", "true", "1", True),
            }

        # Validation
        if not data['title']:
            return JsonResponse({
                'success': False, 
                'message': 'Product title is required'
            }, status=400)
            
        if not data['content']:
            return JsonResponse({
                'success': False, 
                'message': 'Product description is required'
            }, status=400)

        form = ProductsForm(data, instance=products)

        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'success': True, 
                'message': 'Product updated successfully!',
                'product_id': str(id),
                'product_title': product.title
            })
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'success': False, 
                'message': 'Please correct the errors below',
                'errors': errors
            }, status=400)

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False, 
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to update product: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk logout (AJAX)
# -----------------------------------------
@require_POST
def logout_user(request):
    """Handle AJAX request untuk logout"""
    try:
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)
            data_response = {
                'status': 'success',
                'message': f'Goodbye {username}! You have been successfully logged out.',
                'redirect_url': reverse('main:login')
            }
        else:
            data_response = {
                'status': 'error',
                'message': 'User not authenticated'
            }
        
        response = JsonResponse(data_response)
        response.delete_cookie('last_login')
        return response
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Logout failed: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk login (AJAX)
# -----------------------------------------
@require_http_methods(["POST", "GET"])
def login_user(request):
    """Handle AJAX request untuk login"""
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        form = AuthenticationForm(request=request, data=data)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            data_response = {
                'status': 'success',
                'message': f'Welcome back, {user.username}!',
                'redirect_url': reverse('main:show_main'),
                'user': {
                    'username': user.username,
                    'is_authenticated': True
                }
            }

            response = JsonResponse(data_response)
            response.set_cookie('last_login', str(timezone.now()))
            return response
        
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
                
            return JsonResponse({
                'status': 'error',
                'message': 'Login failed. Please check your credentials.',
                'errors': errors
            }, status=400)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Login failed: {str(e)}'    
        }, status=500)


# -----------------------------------------
# Function untuk register (AJAX)
# -----------------------------------------
@require_http_methods(["POST", "GET"])
def register(request):
    """Handle AJAX request untuk registrasi"""
    try:
        if request.content_type == 'application/json':
            payload = json.loads(request.body)
            form = UserCreationForm(payload)
        else:
            form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            data_response = {
                'status': 'success',
                'message': f'Welcome {user.username}! Your account has been successfully created.',
                'redirect_url': reverse('main:show_main'),
                'user': {
                    'username': user.username,
                    'is_authenticated': True
                }                
            }

            response = JsonResponse(data_response)
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
                
            return JsonResponse({
                'status': 'error',
                'message': 'Registration failed. Please correct the errors below.',
                'errors': errors
            }, status=400)

    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'    
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Registration failed: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk mendapatkan login form (AJAX)
# -----------------------------------------
def get_login_form(request):
    """Mengembalikan HTML form login untuk modal"""
    try:
        form = AuthenticationForm()
        html = render_to_string("partials/auth_login_modal.html", {
            'form': form,
            'form_title': 'Login',
            'submit_url': reverse('main:login_user'),
            'submit_text': 'Login'
        }, request=request)
        return JsonResponse({'success': True, 'html': html})
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load login form: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk mendapatkan register form (AJAX)
# -----------------------------------------
def get_register_form(request):
    """Mengembalikan HTML form register untuk modal"""
    try:
        form = UserCreationForm()
        html = render_to_string("partials/auth_register_modal.html", {
            'form': form,
            'form_title': 'Register',
            'submit_url': reverse('main:register'),
            'submit_text': 'Register'
        }, request=request)
        return JsonResponse({'success': True, 'html': html})
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to load register form: {str(e)}'
        }, status=500)


# -----------------------------------------
# Function untuk XML/JSON (tetap sama)
# -----------------------------------------
def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products_list = Products.objects.all()
    data = [
        {
            'id': str(products.id),
            'title': products.title,
            'content': products.content,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'products_views': products.products_views,
            'created_at': products.created_at.isoformat() if products.created_at else None,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
        }
        for products in products_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, products_id):
    try:
        products_list = Products.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, products_id):
    try:
        products_obj = Products.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [products_obj])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)


# -----------------------------------------
# Main view (diperbarui untuk AJAX)
# -----------------------------------------
@login_required(login_url='/login')
def show_main(request):
    """Main view yang mendukung both full page dan AJAX requests"""
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products_list = Products.objects.all().order_by('-created_at')
    else:
        products_list = Products.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'applicationName': 'House Of Champions',
        'npm': '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'products_list': products_list,
        'products_count': products_list.count(),
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    # AJAX request detection
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string("partials/products_list.html", context, request=request)
        return JsonResponse({
            'success': True, 
            'html': html,
            'count': products_list.count()
        })
    else:
        return render(request, "main.html", context)

# Function untuk create_products
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

# Function untuk show_proudcts
# Decorator untuk fungsi show_products
@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

# Dummy functions (tetap sama)
def product_us(request, id):
    return render(request, "product_us.html", {'id': id})


def contact_us(request, id):
    return render(request, "contact_us.html", {'id': id})