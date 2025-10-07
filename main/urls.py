from django.urls import path
from main.views import show_main, create_products, show_products, show_xml, show_json, show_json_by_id, show_xml_by_id

# Penambahan import fungsi register
from main.views import register

# Penambahan import fungsi login_user
from main.views import login_user

# Penambahan import fungsi logout_user
from main.views import logout_user

# Penambahan import fungsi edit_products
from main.views import edit_products    

# Penambahan import fungsi delete_products
from main.views import delete_products

# Dummy import
from main.views import product_us
from main.views import contact_us

# Menambahkan path untuk akses fungsi add_products_entry_ajax
from main.views import add_products_entry_ajax

# -----------------------------------------
# NEW IMPORTS: Add these new view functions
# -----------------------------------------
from main.views import (
    get_products_html, get_create_form, get_edit_form, 
    get_delete_confirm, get_login_form, get_register_form
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    # Menambahkan path untuk create dan show products
    path('create-products/', create_products, name='create_products'),
    path('products/<str:id>/', show_products, name='show_products'),

    # Menambahkan path agar dapat mengakses data dalam bentuk XML dan JSON
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),

    # Menambahkan path agar dapat mengakses data dalam bentuk XML dan JSON berdasarkan ID
    path('xml/<str:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:products_id>/', show_json_by_id, name='show_json_by_id'),

    # Menambahkan path url untuk mengakses fungsi register
    path('register/', register, name='register'),

    # Menambahkan path url untuk mengakses fungsi login_user
    path('login/', login_user, name='login'),

    # Menambahkan path url untuk mengakses fungsi logout_user
    path('logout/', logout_user, name='logout'),

    # Penambahan path url untuk mengakses fungsi edit_products
    path('products/<uuid:id>/edit/', edit_products, name='edit_products'),

    # Penambahan path url untuk mengakses fungsi delete_products
    path('products/<uuid:id>/delete/', delete_products, name='delete_products'),

    # Dummy path url
    path('product_us/', product_us, name='product_us'),
    path('contact_us/', contact_us, name='contact_us'),

    # Penambahan path url untuk mengakses fungsi add_products_entry_ajax
    path('create-products-ajax/', add_products_entry_ajax, name='add_products_entry_ajax'),

    # =========================================================================
    # PATTERN UNTUK AKSES FUNCTION AJAX REQUEST
    # =========================================================================
    
    # Path untuk mendapatkan HTML daftar produk (refresh AJAX)
    path('get-products-html/', get_products_html, name='get_products_html'),
    
    # Path untuk mendapatkan form dalam modal
    path('get-create-form/', get_create_form, name='get_create_form'),
    path('get-edit-form/<uuid:id>/', get_edit_form, name='get_edit_form'),
    path('get-delete-confirm/<uuid:id>/', get_delete_confirm, name='get_delete_confirm'),
    
    # Path untuk mendapatkan form autentikasi dalam modal
    path('get-login-form/', get_login_form, name='get_login_form'),
    path('get-register-form/', get_register_form, name='get_register_form'),
]