from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # ==================== AUTHENTICATION URLS ====================
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # ==================== MAIN VIEWS URLS ====================
    path('', views.show_main, name='show_main'),
    path('products/create/', views.create_products, name='create_products'),
    path('products/<uuid:id>/', views.show_products, name='show_products'),

    # ==================== PRODUCT CRUD URLS ====================
    path('products/<uuid:id>/edit/', views.edit_products, name='edit_products'),
    path('products/<uuid:id>/delete/', views.delete_products, name='delete_products'),

    # ==================== AJAX SPECIFIC URLS ====================
    # Increment views (AJAX POST)
    path('ajax/products/<uuid:id>/increment-views/', views.increment_views_ajax, name='increment_views_ajax'),

    # ==================== API URLS (JSON/XML) ====================
    path('api/products/xml/', views.show_xml, name='show_xml'),
    path('api/products/json/', views.show_json, name='show_json'),
    path('api/products/<uuid:products_id>/xml/', views.show_xml_by_id, name='show_xml_by_id'),
    path('api/products/<uuid:products_id>/json/', views.show_json_by_id, name='show_json_by_id'),
]
