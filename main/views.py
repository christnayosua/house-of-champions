# import library yang dibutuhkan 
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models import F, Q
from django.core.paginator import Paginator

from main.forms import ProductsForm
from main.models import Products

# ---------------------------------------------------------------
# Helper functions untuk handle AJAX request
# ---------------------------------------------------------------

def _is_ajax(request):
    """
    Mengecek apakah request adalah AJAX request.
    
    Args:
        request: HttpRequest object
        
    Returns:
        bool: True jika request adalah AJAX, False jika tidak
    """
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def _safe_username(user):
    """
    Mengembalikan username yang aman (handle Anonymous user).
    
    Args:
        user: User object atau None
        
    Returns:
        str: Username atau "Anonymous" jika user tidak ada
    """
    return user.username if user else "Anonymous"

def _safe_user_id(user):
    """
    Mengembalikan user ID yang aman (handle Anonymous user).
    
    Args:
        user: User object atau None
        
    Returns:
        int/None: User ID atau None jika user tidak ada
    """
    return user.id if user else None

def _can_modify(product, user):
    """
    Mengecek apakah user dapat memodifikasi product.
    
    Args:
        product: Products object
        user: User object
        
    Returns:
        bool: True jika user dapat memodifikasi, False jika tidak
    """
    return product.user is not None and product.user == user

def _ajax_response(data, status=200):
    """
    Helper untuk membuat response AJAX yang konsisten.
    
    Args:
        data: Dictionary data untuk response
        status: HTTP status code
        
    Returns:
        JsonResponse: Response object
    """
    return JsonResponse(data, status=status)

# -------------------------
# Authentication views dengan AJAX support
# -------------------------

def register(request):
    """
    Handle user registration dengan AJAX support.
    
    Methods:
        GET: Menampilkan form registrasi (HTML atau JSON dengan form HTML)
        POST: Memproses registrasi user
        
    AJAX Response:
        Success: {status: 'success', message: '...', redirect_url: '...'}
        Error: {status: 'error', message: '...', errors: {...}}
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            if _is_ajax(request):                
                return _ajax_response({
                    'status': 'success',
                    'message': 'Your account has been successfully created!',
                    'redirect_url': reverse('main:show_main')
                })
            
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show_main')
        else:
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'error',
                    'message': 'Validation errors',
                    'errors': form.errors.get_json_data()
                }, status=400)
    else:        
        form = UserCreationForm()

    # Handle GET request untuk AJAX
    if _is_ajax(request) and request.method == "GET":
        html = render(request, 'register_form.html', {'form': form}).content.decode('utf-8')
        return _ajax_response({'form_html': html})

    return render(request, 'register.html', {'form': form})

def login_user(request):
    """
    Handle user login dengan AJAX support.
    
    Methods:
        GET: Menampilkan form login (HTML atau JSON dengan form HTML)
        POST: Memproses login user
        
    AJAX Response:
        Success: {status: 'success', message: '...', redirect_url: '...'}
        Error: {status: 'error', message: '...', errors: {...}}
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if _is_ajax(request):
                response = _ajax_response({
                    'status': 'success',
                    'message': 'Login successful',
                    'redirect_url': reverse('main:show_main')
                })
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
                
            resp = HttpResponseRedirect(reverse('main:show_main'))
            resp.set_cookie('last_login', str(datetime.datetime.now()))
            return resp
        else:
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'error',
                    'message': 'Invalid credentials',
                    'errors': form.errors.get_json_data()
                }, status=400)
    else:
        form = AuthenticationForm()

    # Handle GET request untuk AJAX
    if _is_ajax(request) and request.method == "GET":
        html = render(request, 'login_form.html', {'form': form}).content.decode('utf-8')
        return _ajax_response({'form_html': html})

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    """
    Handle user logout dengan AJAX support.
    
    Methods:
        POST: Logout user
        
    AJAX Response:
        Success: {status: 'success', redirect_url: '...'}
    """
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    
    if _is_ajax(request):
        return _ajax_response({
            'status': 'success', 
            'redirect_url': reverse('main:login')
        })
    
    return response

# -------------------------
# Main / listing / detail views dengan AJAX support
# -------------------------

@login_required(login_url='/login')
def show_main(request):
    """
    Menampilkan halaman utama dengan daftar products.
    Mendukung filter, pencarian, sorting, dan pagination via AJAX.
    
    Query Parameters:
        filter: 'all' atau 'my_products'
        category: Kategori produk untuk filter
        search: Kata kunci pencarian
        sort: Field untuk sorting (name, price, rating, dll)
        page: Halaman untuk pagination
        per_page: Jumlah item per halaman
        
    AJAX Response:
        Success: {
            status: 'success',
            products: [...],
            current_page: X,
            total_pages: Y,
            has_next: bool,
            has_previous: bool,
            total_products: Z
        }
    """
    # Ambil parameter dari request
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", "")
    search_query = request.GET.get("search", "")
    sort_by = request.GET.get("sort", "-created_at")

    # Filter dasar
    if filter_type == "my_products":
        qs = Products.objects.filter(user=request.user)
    else:
        qs = Products.objects.all()

    # Filter tambahan
    if category_filter:
        qs = qs.filter(category=category_filter)

    if search_query:
        qs = qs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(brandName__icontains=search_query)
        )

    # Sorting
    valid_sort = ['name', '-name', 'price', '-price', 'rating', '-rating', 
                  'created_at', '-created_at', 'visitors', '-visitors']
    if sort_by in valid_sort:
        qs = qs.order_by(sort_by)
    else:
        qs = qs.order_by('-created_at')

    # Handle AJAX request untuk pagination
    if _is_ajax(request):
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 12))
        paginator = Paginator(qs, per_page)
        page_obj = paginator.get_page(page)
        
        # Siapkan data products
        products_data = []
        for product in page_obj:
            products_data.append({
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'formatted_price': product.formatted_price,
                'price_usd': product.get_price_in_dollar(),
                'description': product.description,
                'category': product.category,
                'category_display': product.get_category_display(),
                'stock': product.stock,
                'rating': product.get_clean_rating(),
                'brandName': product.brandName,
                'thumbnail1': product.thumbnail1,
                'is_featured': product.is_featured,
                'visitors': product.visitors,
                'is_products_hot': product.is_products_hot,
                'created_at': product.created_at.strftime('%d %b %Y'),
                'user': _safe_username(product.user),
                'user_id': _safe_user_id(product.user),
                'can_edit': _can_modify(product, request.user),
                'can_delete': _can_modify(product, request.user),
                'detail_url': reverse('main:show_products', kwargs={'id': product.id}),
            })
            
        return _ajax_response({
            'status': 'success',
            'products': products_data,
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'total_products': paginator.count
        })

    # Traditional render untuk non-AJAX request
    context = {
        'applicationName': 'House Of Champions',
        'npm': '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'products_list': qs,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    """
    Menampilkan detail produk dan increment view counter.
    Mendukung AJAX request.
    
    Args:
        id: ID produk
        
    AJAX Response:
        Success: {
            status: 'success',
            product: {...},
            related: [...]
        }
        Error: 404 jika produk tidak ditemukan
    """
    product = get_object_or_404(Products, pk=id)
    
    # Atomic increment untuk menghindari race condition
    Products.objects.filter(pk=product.pk).update(visitors=F('visitors') + 1)
    product.refresh_from_db()

    # Handle AJAX request
    if _is_ajax(request):
        # Ambil produk terkait
        related_products = list(Products.objects
            .filter(category=product.category)
            .exclude(pk=product.pk)
            .order_by('-rating', '-visitors')[:4])
        
        related_data = [{
            'id': str(r.id),
            'name': r.name,
            'formatted_price': r.formatted_price,
            'thumbnail1': r.thumbnail1
        } for r in related_products]
        
        return _ajax_response({
            'status': 'success',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'formatted_price': product.formatted_price,
                'price_usd': product.get_price_in_dollar(),
                'description': product.description,
                'category': product.category,
                'category_display': product.get_category_display(),
                'stock': product.stock,
                'rating': product.get_clean_rating(),
                'brandName': product.brandName,
                'thumbnail1': product.thumbnail1,
                'visitors': product.visitors,
                'is_products_hot': product.is_products_hot,
                'created_at': product.created_at.strftime('%d %b %Y'),
                'user': _safe_username(product.user),
                'user_id': _safe_user_id(product.user),
                'can_edit': _can_modify(product, request.user),
            },
            'related': related_data
        })

    # Traditional render untuk non-AJAX request
    return render(request, "products_detail.html", {'products': product})

# -------------------------
# CRUD operations dengan AJAX support
# -------------------------

@login_required(login_url='/login')
def create_products(request):
    """
    Membuat produk baru. Mendukung AJAX request.
    
    Methods:
        GET: Menampilkan form (HTML atau JSON dengan form HTML)
        POST: Membuat produk baru
        
    AJAX Response:
        Success: {
            status: 'success', 
            message: '...',
            product: {...}
        }
        Error: {
            status: 'error',
            errors: {...}
        }
    """
    form = ProductsForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'success',
                    'message': 'Produk berhasil dibuat!',
                    'product': {
                        'id': str(product.id),
                        'name': product.name,
                        'formatted_price': product.formatted_price,
                        'detail_url': reverse('main:show_products', kwargs={'id': product.id})
                    }
                })
                
            messages.success(request, 'Produk berhasil dibuat!')
            return redirect('main:show_products', id=product.id)
        else:
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'error', 
                    'errors': form.errors.get_json_data()
                }, status=400)

    # Handle GET request untuk AJAX
    if _is_ajax(request) and request.method == 'GET':
        html = render(request, 'create_products.html', {
            'form': form, 
            'title': 'Tambah Produk', 
            'action_url': reverse('main:create_products')
        }).content.decode('utf-8')
        return _ajax_response({'form_html': html})

    # Traditional render untuk non-AJAX request
    return render(request, "create_products.html", {'form': form})

@login_required(login_url='/login')
def edit_products(request, id):
    """
    Mengedit produk yang sudah ada. Hanya owner yang bisa edit.
    Mendukung AJAX request.
    
    Args:
        id: ID produk yang akan diedit
        
    Methods:
        GET: Menampilkan form edit (HTML atau JSON dengan form HTML)
        POST: Memperbarui produk
        
    AJAX Response:
        Success: {
            status: 'success',
            message: '...',
            product: {...}
        }
        Error: {
            status: 'error',
            errors: {...}
        }
    """
    product = get_object_or_404(Products, pk=id, user=request.user)
    form = ProductsForm(request.POST or None, request.FILES or None, instance=product)
    
    if request.method == 'POST':
        if form.is_valid():
            updated_product = form.save()
            
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'success',
                    'message': 'Produk berhasil diupdate!',
                    'product': {
                        'id': str(updated_product.id),
                        'name': updated_product.name,
                        'formatted_price': updated_product.formatted_price
                    }
                })
                
            messages.success(request, 'Produk berhasil diupdate!')
            return redirect('main:show_products', id=product.id)
        else:
            if _is_ajax(request):
                return _ajax_response({
                    'status': 'error', 
                    'errors': form.errors.get_json_data()
                }, status=400)

    # Handle GET request untuk AJAX
    if _is_ajax(request) and request.method == 'GET':
        html = render(request, 'create_product.html', {
            'form': form, 
            'title': 'Edit Produk', 
            'action_url': reverse('main:edit_products', kwargs={'id': product.id}), 
            'product': product
        }).content.decode('utf-8')
        return _ajax_response({'form_html': html})

    # Traditional render untuk non-AJAX request
    return render(request, "edit_products.html", {'form': form, 'product': product})

@login_required(login_url='/login')
@require_http_methods(["POST"])
def delete_products(request, id):
    """
    Menghapus produk. Hanya owner yang bisa menghapus.
    Mendukung AJAX request.
    
    Args:
        id: ID produk yang akan dihapus
        
    AJAX Response:
        Success: {
            status: 'success',
            message: '...',
            redirect_url: '...'
        }
        Error: 404 jika produk tidak ditemukan
    """
    product = get_object_or_404(Products, pk=id, user=request.user)
    product_name = product.name
    product.delete()
    
    if _is_ajax(request):
        return _ajax_response({
            'status': 'success', 
            'message': f'Produk "{product_name}" berhasil dihapus!',
            'redirect_url': reverse('main:show_main')
        })
        
    messages.success(request, f'Produk "{product_name}" berhasil dihapus!')
    return redirect('main:show_main')

# -------------------------
# API endpoints (JSON / XML)
# -------------------------

def show_xml(request):
    """Mengembalikan semua produk dalam format XML"""
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    """Mengembalikan semua produk dalam format JSON"""
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    """Mengembalikan produk spesifik dalam format XML"""
    products_list = Products.objects.filter(pk=products_id)
    if not products_list.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, products_id):
    """Mengembalikan produk spesifik dalam format JSON"""
    try:
        product = Products.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

# -------------------------
# AJAX-specific endpoints
# -------------------------

@require_http_methods(["POST"])
def increment_views_ajax(request, id):
    """
    AJAX endpoint untuk increment view counter produk.
    
    Args:
        id: ID produk
        
    AJAX Response:
        Success: {
            status: 'success',
            views: X,
            is_products_hot: bool
        }
        Error: {
            status: 'error',
            message: '...'
        }
    """
    try:
        Products.objects.filter(pk=id).update(visitors=F('visitors') + 1)
        product = Products.objects.get(pk=id)
        return _ajax_response({
            'status': 'success',
            'views': product.visitors,
            'is_products_hot': product.is_products_hot
        })
    except Products.DoesNotExist:
        return _ajax_response({
            'status': 'error', 
            'message': 'Product not found'
        }, status=404)