import json
import uuid
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST, require_http_methods
from django.utils.html import strip_tags
from django.template.loader import render_to_string


# -----------------------------------------
# MAIN VIEW
# -----------------------------------------
@login_required(login_url='/login')
def show_main(request):
    """Main view - hanya render template dasar, data di-load via AJAX"""
    context = {
        'applicationName': 'House Of Champions',
        'name': 'Christna Yosua Rotinsulu',
        'npm': '2406495691',
        'class': 'PBP A',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# -----------------------------------------
# PRODUCT CRUD - AJAX ENDPOINTS
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


@login_required(login_url='/login')
def get_create_form(request):
    """Mengembalikan HTML form create product untuk modal"""
    form = ProductsForm()
    html = render_to_string("partials/products_form_modal.html", {
        'form': form,
        'form_title': 'Add New Product',
        'submit_url': reverse('main:add_products_entry_ajax'),
    }, request=request)
    return JsonResponse({'success': True, 'html': html})


@login_required(login_url='/login')
def get_edit_form(request, id):
    """Mengembalikan HTML form edit product untuk modal"""
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
    }, request=request)
    return JsonResponse({'success': True, 'html': html})


@login_required(login_url='/login')
def get_delete_confirm(request, id):
    """Mengembalikan HTML modal konfirmasi delete"""
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


@login_required(login_url='/login')
@require_POST
def add_products_entry_ajax(request):
    """Handle AJAX request untuk create product"""
    try:
        # Parse JSON data
        data = json.loads(request.body)
        
        # Extract and sanitize data sesuai model baru
        name = strip_tags(data.get("name", "").strip())
        price = data.get("price", 0)
        description = strip_tags(data.get("description", "").strip())
        category = data.get("category", "")
        thumbnail1 = data.get("thumbnail1", "")
        thumbnail2 = data.get("thumbnail2", "")
        thumbnail3 = data.get("thumbnail3", "")
        stock = data.get("stock", 0)
        rating = data.get("rating", 0.0)
        brand = data.get("brand", "")
        brandName = data.get("brandName", "")
        is_featured = data.get("is_featured", False)

        # Validation
        if not name:
            return JsonResponse({
                'success': False, 
                'message': 'Product name is required'
            }, status=400)
            
        if not description:
            return JsonResponse({
                'success': False, 
                'message': 'Product description is required'
            }, status=400)

        if price < 0:
            return JsonResponse({
                'success': False, 
                'message': 'Price cannot be negative'
            }, status=400)

        # Create product dengan model yang baru
        products = Products(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail1=thumbnail1,
            thumbnail2=thumbnail2,
            thumbnail3=thumbnail3,
            stock=stock,
            rating=rating,
            brand=brand,
            brandName=brandName,
            is_featured=is_featured,
            user=request.user
        )
        products.save()

        return JsonResponse({
            'success': True, 
            'message': 'Product added successfully!',
            'product_id': str(products.id)
        }, status=201)
            
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to create product: {str(e)}'
        }, status=500)


@login_required(login_url='/login')
@require_POST
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

        # Parse JSON data
        data = json.loads(request.body)
        
        # Update fields sesuai model baru
        products.name = strip_tags(data.get('name', products.name).strip())
        products.price = data.get('price', products.price)
        products.description = strip_tags(data.get('description', products.description).strip())
        products.category = data.get('category', products.category)
        products.thumbnail1 = data.get('thumbnail1', products.thumbnail1)
        products.thumbnail2 = data.get('thumbnail2', products.thumbnail2)
        products.thumbnail3 = data.get('thumbnail3', products.thumbnail3)
        products.stock = data.get('stock', products.stock)
        products.rating = data.get('rating', products.rating)
        products.brand = data.get('brand', products.brand)
        products.brandName = data.get('brandName', products.brandName)
        products.is_featured = data.get('is_featured', products.is_featured)

        # Validation
        if not products.name:
            return JsonResponse({
                'success': False, 
                'message': 'Product name is required'
            }, status=400)
            
        if not products.description:
            return JsonResponse({
                'success': False, 
                'message': 'Product description is required'
            }, status=400)

        if products.price < 0:
            return JsonResponse({
                'success': False, 
                'message': 'Price cannot be negative'
            }, status=400)

        products.save()
        return JsonResponse({
            'success': True, 
            'message': 'Product updated successfully!',
            'product_id': str(id)
        })

    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to update product: {str(e)}'
        }, status=500)


@login_required(login_url='/login')
@require_POST
def delete_products(request, id):
    """Handle AJAX request untuk delete product"""
    try:
        products = get_object_or_404(Products, pk=id)
        product_name = products.name
        
        # Permission check
        if products.user and request.user != products.user:
            return JsonResponse({
                'success': False, 
                'message': 'You are not authorized to delete this product'
            }, status=403)

        products.delete()
        return JsonResponse({
            'success': True, 
            'message': f'Product "{product_name}" deleted successfully!',
            'product_id': str(id)
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Failed to delete product: {str(e)}'
        }, status=500)


# -----------------------------------------
# AUTHENTICATION - AJAX ENDPOINTS
# -----------------------------------------
def get_login_form(request):
    """Mengembalikan HTML form login untuk modal"""
    form = AuthenticationForm()
    html = render_to_string("partials/auth_login_modal.html", {
        'form': form,
        'form_title': 'Login',
        'submit_url': reverse('main:login_user'),
    }, request=request)
    return JsonResponse({'success': True, 'html': html})


def get_register_form(request):
    """Mengembalikan HTML form register untuk modal"""
    form = UserCreationForm()
    html = render_to_string("partials/auth_register_modal.html", {
        'form': form,
        'form_title': 'Register',
        'submit_url': reverse('main:register'),
    }, request=request)
    return JsonResponse({'success': True, 'html': html})


@require_http_methods(["POST"])
def login_user(request):
    """Handle AJAX request untuk login"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({
                'success': True,
                'message': f'Welcome back, {user.username}!',
                'redirect_url': reverse('main:show_main'),
            })
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid username or password.'
            }, status=400)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Login failed: {str(e)}'    
        }, status=500)


@require_http_methods(["POST"])
def register(request):
    """Handle AJAX request untuk registrasi"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')

        # Basic validation
        if not username or not password1 or not password2:
            return JsonResponse({
                'success': False,
                'message': 'All fields are required.'
            }, status=400)

        if password1 != password2:
            return JsonResponse({
                'success': False,
                'message': 'Passwords do not match.'
            }, status=400)

        if len(password1) < 8:
            return JsonResponse({
                'success': False,
                'message': 'Password must be at least 8 characters long.'
            }, status=400)

        # Check if username already exists
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                'success': False,
                'message': 'Username already exists.'
            }, status=400)

        # Create user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)

        response = JsonResponse({
            'success': True,
            'message': f'Welcome {user.username}! Your account has been created.',
            'redirect_url': reverse('main:show_main'),
        })
        response.set_cookie('last_login', str(timezone.now()))
        return response

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Registration failed: {str(e)}'
        }, status=500)


@require_POST
def logout_user(request):
    """Handle AJAX request untuk logout"""
    try:
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)
            response = JsonResponse({
                'success': True,
                'message': f'Goodbye {username}! You have been logged out.',
                'redirect_url': reverse('main:get_login_form')
            })
            response.delete_cookie('last_login')
            return response
        else:
            return JsonResponse({
                'success': False,
                'message': 'User not authenticated'
            }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Logout failed: {str(e)}'
        }, status=500)


# -----------------------------------------
# API ENDPOINTS (XML/JSON)
# -----------------------------------------
def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products_list = Products.objects.all()
    data = serializers.serialize("json", products_list)
    return HttpResponse(data, content_type="application/json")


def show_xml_by_id(request, id):
    products = get_object_or_404(Products, pk=id)
    xml_data = serializers.serialize("xml", [products])
    return HttpResponse(xml_data, content_type="application/xml")


def show_json_by_id(request, id):
    products = get_object_or_404(Products, pk=id)
    data = serializers.serialize("json", [products])
    return HttpResponse(data, content_type="application/json")


# -----------------------------------------
# LEGACY VIEWS (Optional - bisa dihapus jika tidak digunakan)
# -----------------------------------------
def create_products(request):
    """Legacy view - bisa dihapus jika hanya menggunakan AJAX"""
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        products_entry = form.save(commit=False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)


@login_required(login_url='/login')
def show_products(request, id):
    """Detail view untuk product"""
    products = get_object_or_404(Products, pk=id)
    products.increment_views()

    context = {
        'products': products
    }
    return render(request, "products_detail.html", context)