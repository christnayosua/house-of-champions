from django.urls import path
from main.views import (
    show_main,
    # ... other imports if you still need them for non-AJAX features ...
    show_xml, show_json, show_json_by_id, show_xml_by_id,
    # AJAX views for products
    get_products_html, get_create_form, get_edit_form, get_delete_confirm,
    add_products_entry_ajax, edit_products, delete_products,
    # AJAX views for authentication
    get_login_form, get_register_form, login_user, register, logout_user
)

app_name = 'main'

urlpatterns = [
    # Main page
    path('', show_main, name='show_main'),
    
    # =========================================================================
    # AJAX PATHS FOR PRODUCTS
    # =========================================================================
    # Path to get product list HTML (for AJAX refresh)
    path('get-products-html/', get_products_html, name='get_products_html'),
    
    # Paths to get modal forms
    path('get-create-form/', get_create_form, name='get_create_form'),
    path('get-edit-form/<uuid:id>/', get_edit_form, name='get_edit_form'),
    path('get-delete-confirm/<uuid:id>/', get_delete_confirm, name='get_delete_confirm'),
    
    # Paths for product CRUD operations (AJAX handlers)
    path('create-products-ajax/', add_products_entry_ajax, name='add_products_entry_ajax'),
    path('edit-products/<uuid:id>/', edit_products, name='edit_products'),
    path('delete-products/<uuid:id>/', delete_products, name='delete_products'),
    
    # =========================================================================
    # AJAX PATHS FOR AUTHENTICATION
    # =========================================================================
    # Paths to get authentication modal forms
    path('get-login-form/', get_login_form, name='get_login_form'),
    path('get-register-form/', get_register_form, name='get_register_form'),
    
    # Paths for authentication actions (AJAX handlers)
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    
    # =========================================================================
    # API ENDPOINTS (XML/JSON)
    # =========================================================================
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:products_id>/', show_json_by_id, name='show_json_by_id'),
]