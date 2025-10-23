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
# Helper -> handle request ajax when register and delete products
# ---------------------------------------------------------------
def _is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def _safe_username(user):
    return user.username if user else "Anonymous"

def _safe_user_id(user):
    return user.id if user else None

def _can_modify(product, user):
    return product.user is not None and product.user == user

# -------------------------
# Authentication views
# -------------------------
def register(request):
    # Cek request method
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # Validasi input user
        if form.is_valid():
            # Simpan form 
            user = form.save()
            login(request, user)
            # handle ajax request
            if _is_ajax(request):                
                return JsonResponse({
                    'status': 'success',
                    'message': 'Your account has been successfully created!',
                    'redirect_url': reverse('main:show_main')
                })
            # success messages
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show_main')
        else:
            # Handle ketika validasi error
            if _is_ajax(request):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Validation errors',
                    'errors': form.errors.get_json_data()
                }, status=400)
    else:        
        form = UserCreationForm()

    # Handle untuk request method GET
    if _is_ajax(request) and request.method == "GET":
        # Direct ke halaman partialnya
        html = render(request, 'partials/register_form.html', {'form': form}).content.decode('utf-8')
        return JsonResponse({'form_html': html})

    return render(request, 'register.html', {'form': form})

def login_user(request):
    """
    Login view with AJAX support.
    Sets cookie 'last_login' on success.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if _is_ajax(request):
                resp = JsonResponse({
                    'status': 'success',
                    'message': 'Login successful',
                    'redirect_url': reverse('main:show_main')
                })
                resp.set_cookie('last_login', str(datetime.datetime.now()))
                return resp
            resp = HttpResponseRedirect(reverse('main:show_main'))
            resp.set_cookie('last_login', str(datetime.datetime.now()))
            return resp
        else:
            if _is_ajax(request):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid credentials',
                    'errors': form.errors.get_json_data()
                }, status=400)
    else:
        form = AuthenticationForm()

    if _is_ajax(request) and request.method == "GET":
        html = render(request, 'partials/login_form.html', {'form': form}).content.decode('utf-8')
        return JsonResponse({'form_html': html})

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    """
    Logout user. AJAX returns JSON redirect info.
    """
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    if _is_ajax(request):
        return JsonResponse({'status': 'success', 'redirect_url': reverse('main:login')})
    return response

# -------------------------
# Main / listing / detail
# -------------------------
@login_required(login_url='/login')
def show_main(request):
    """
    Main dashboard with filtering, searching, sorting and AJAX pagination.
    Query params (AJAX):
      - filter=my_products|all
      - category=<category_value>
      - search=<text>
      - sort=<field or -field>
      - page (int), per_page (int)
    """
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", "")
    search_query = request.GET.get("search", "")
    sort_by = request.GET.get("sort", "-created_at")

    if filter_type == "my_products":
        qs = Products.objects.filter(user=request.user)
    else:
        qs = Products.objects.all()

    if category_filter:
        qs = qs.filter(category=category_filter)

    if search_query:
        qs = qs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(brandName__icontains=search_query)
        )

    valid_sort = ['name', '-name', 'price', '-price', 'rating', '-rating', 'created_at', '-created_at', 'visitors', '-visitors']
    if sort_by in valid_sort:
        qs = qs.order_by(sort_by)
    else:
        qs = qs.order_by('-created_at')

    # AJAX paginated response
    if _is_ajax(request):
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 12))
        paginator = Paginator(qs, per_page)
        page_obj = paginator.get_page(page)
        products_data = []
        for p in page_obj:
            products_data.append({
                'id': str(p.id),
                'name': p.name,
                'price': p.price,
                'formatted_price': p.formatted_price,
                'price_usd': p.get_price_in_dollar(),
                'description': p.description,
                'category': p.category,
                'category_display': p.get_category_display(),
                'stock': p.stock,
                'rating': p.get_clean_rating(),
                'brandName': p.brandName,
                'thumbnail1': p.thumbnail1,
                'is_featured': p.is_featured,
                'visitors': p.visitors,
                'is_products_hot': p.is_products_hot,
                'created_at': p.created_at.strftime('%d %b %Y'),
                'user': _safe_username(p.user),
                'user_id': _safe_user_id(p.user),
                'can_edit': _can_modify(p, request.user),
                'can_delete': _can_modify(p, request.user),
                'detail_url': reverse('main:show_products', kwargs={'id': p.id}),
            })
        return JsonResponse({
            'status': 'success',
            'products': products_data,
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'total_products': paginator.count
        })

    # Traditional render
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
    Detail view: increments views and returns HTML or JSON (AJAX).
    """
    product = get_object_or_404(Products, pk=id)
    # atomic increment using F to reduce race condition
    Products.objects.filter(pk=product.pk).update(visitors=F('visitors') + 1)
    product.refresh_from_db()

    if _is_ajax(request):
        related = list(Products.objects.filter(category=product.category).exclude(pk=product.pk).order_by('-rating','-visitors')[:4])
        related_data = [{
            'id': str(r.id),
            'name': r.name,
            'formatted_price': r.formatted_price,
            'thumbnail1': r.thumbnail1
        } for r in related]
        return JsonResponse({
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

    return render(request, "products_detail.html", {'products': product})

# -------------------------
# CRUD (supports AJAX)
# -------------------------
@login_required(login_url='/login')
def create_products(request):
    """
    Create product (form or AJAX). Must be logged in.
    AJAX: POST -> JSON result; GET -> returns HTML for the form (form partial).
    """
    form = ProductsForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            if _is_ajax(request):
                return JsonResponse({
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
                return JsonResponse({'status': 'error', 'errors': form.errors.get_json_data()}, status=400)

    if _is_ajax(request) and request.method == 'GET':
        html = render(request, 'partials/product_form.html', {'form': form, 'title': 'Tambah Produk', 'action_url': reverse('main:create_products')}).content.decode('utf-8')
        return JsonResponse({'form_html': html})

    return render(request, "create_products.html", {'form': form})

@login_required(login_url='/login')
def edit_products(request, id):
    """
    Edit product. Only owner can edit. Supports AJAX and traditional forms.
    """
    product = get_object_or_404(Products, pk=id, user=request.user)
    form = ProductsForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            updated = form.save()
            if _is_ajax(request):
                return JsonResponse({
                    'status': 'success',
                    'message': 'Produk berhasil diupdate!',
                    'product': {
                        'id': str(updated.id),
                        'name': updated.name,
                        'formatted_price': updated.formatted_price
                    }
                })
            messages.success(request, 'Produk berhasil diupdate!')
            return redirect('main:show_products', id=product.id)
        else:
            if _is_ajax(request):
                return JsonResponse({'status': 'error', 'errors': form.errors.get_json_data()}, status=400)

    if _is_ajax(request) and request.method == 'GET':
        html = render(request, 'partials/product_form.html', {'form': form, 'title': 'Edit Produk', 'action_url': reverse('main:edit_products', kwargs={'id': product.id}), 'product': product}).content.decode('utf-8')
        return JsonResponse({'form_html': html})

    return render(request, "edit_products.html", {'form': form, 'product': product})

@login_required(login_url='/login')
@require_http_methods(["POST"])
def delete_products(request, id):
    """
    Delete a product. Accepts POST (for form) and will return JSON if AJAX.
    (If you want DELETE verb support, add a dedicated view with csrf_exempt or handle via fetch with POST + _method.)
    """
    product = get_object_or_404(Products, pk=id, user=request.user)
    name = product.name
    product.delete()
    if _is_ajax(request):
        return JsonResponse({'status': 'success', 'message': f'Produk \"{name}\" berhasil dihapus!', 'redirect_url': reverse('main:show_main')})
    messages.success(request, f'Produk \"{name}\" berhasil dihapus!')
    return redirect('main:show_main')

# -------------------------
# Simple API endpoints (JSON / XML)
# -------------------------
def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    products_list = Products.objects.filter(pk=products_id)
    if not products_list.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, products_id):
    try:
        product = Products.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [product])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

# -------------------------
# AJAX-specific helper: increment views
# -------------------------
@require_http_methods(["POST"])
def increment_views_ajax(request, id):
    """
    AJAX endpoint: increment view counter for product and return updated count.
    """
    try:
        Products.objects.filter(pk=id).update(visitors=F('visitors') + 1)
        product = Products.objects.get(pk=id)
        return JsonResponse({
            'status': 'success',
            'views': product.visitors,
            'is_products_hot': product.is_products_hot
        })
    except Products.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)
