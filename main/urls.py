from django.urls import path
from main.views import show_main, create_products, show_products, show_xml, show_json, show_json_by_id, show_xml_by_id

# Penambahan import fungsi register
from main.views import register

# Penambahan import fungsi login_user
from main.views import login_user

# Penambahan import fungsi logout_user
from main.views import logout_user

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
]
