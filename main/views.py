import json
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
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
        title = strip_tags(data.get("title", "").strip())
        content = strip_tags(data.get("content", "").strip())
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)

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

        # Create product
        products = Products(
            title=title,
            content=content,
            category=category,
            thumbnail=thumbnail,
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
        products.title = strip_tags(data.get('title', products.title).strip())
        products.content = strip_tags(data.get('content', products.content).strip())
        products.category = data.get('category', products.category)
        products.thumbnail = data.get('thumbnail', products.thumbnail)
        products.is_featured = data.get('is_featured', products.is_featured)

        # Validation
        if not products.title:
            return JsonResponse({
                'success': False, 
                'message': 'Product title is required'
            }, status=400)
            
        if not products.content:
            return JsonResponse({
                'success': False, 
                'message': 'Product description is required'
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
        if user.objects.filter(username=username).exists():
            return JsonResponse({
                'success': False,
                'message': 'Username already exists.'
            }, status=400)

        # Create user
        user = user.objects.create_user(username=username, password=password1)
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
                'redirect_url': reverse('main:login')
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