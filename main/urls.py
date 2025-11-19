from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    # =========================================================================
    # AUTHENTICATION URLS
    # =========================================================================
    
    path('register/', views.register, name='register'),
    # URL: /register/
    # View: views.register
    # Description: Handle user registration dengan AJAX support
    # Methods: GET (menampilkan form), POST (memproses registrasi)
    # AJAX Support: Ya (GET mengembalikan form HTML, POST mengembalikan JSON)
    
    path('login/', views.login_user, name='login'),
    # URL: /login/
    # View: views.login_user
    # Description: Handle user login dengan AJAX support
    # Methods: GET (menampilkan form), POST (memproses login)
    # AJAX Support: Ya (GET mengembalikan form HTML, POST mengembalikan JSON)
    
    path('logout/', views.logout_user, name='logout'),
    # URL: /logout/
    # View: views.logout_user
    # Description: Handle user logout dengan AJAX support
    # Methods: POST (memproses logout)
    # AJAX Support: Ya (mengembalikan JSON dengan redirect URL)
    
    # =========================================================================
    # MAIN PAGES & PRODUCT LISTING URLS
    # =========================================================================
    
    path('', views.show_main, name='show_main'),
    # URL: /
    # View: views.show_main
    # Description: Menampilkan halaman utama dengan daftar produk
    # Methods: GET
    # AJAX Support: Ya (mengembalikan JSON dengan data produk terpaginate)
    # Query Parameters:
    #   - filter: 'all' atau 'my_products'
    #   - category: filter berdasarkan kategori
    #   - search: kata kunci pencarian
    #   - sort: field untuk sorting
    #   - page: halaman untuk pagination
    #   - per_page: jumlah item per halaman
    
    path('product/<uuid:id>/', views.show_products, name='show_products'),
    # URL: /product/<id>/
    # View: views.show_products
    # Description: Menampilkan detail produk dan increment view counter
    # Methods: GET
    # AJAX Support: Ya (mengembalikan JSON dengan detail produk dan related products)
    # Parameters:
    #   - id: UUID produk (menggunakan UUIDField di model)
    
    # =========================================================================
    # CRUD OPERATIONS URLS
    # =========================================================================
    
    path('create-product/', views.create_products, name='create_products'),
    # URL: /create-product/
    # View: views.create_products
    # Description: Membuat produk baru
    # Methods: GET (menampilkan form), POST (memproses pembuatan produk)
    # AJAX Support: Ya (GET mengembalikan form HTML, POST mengembalikan JSON)
    # Authentication Required: Ya
    
    path('edit-product/<uuid:id>/', views.edit_products, name='edit_products'),
    # URL: /edit-product/<id>/
    # View: views.edit_products
    # Description: Mengedit produk yang sudah ada
    # Methods: GET (menampilkan form), POST (memproses update produk)
    # AJAX Support: Ya (GET mengembalikan form HTML, POST mengembalikan JSON)
    # Authentication Required: Ya
    # Authorization: Hanya owner produk yang bisa edit
    
    path('delete-product/<uuid:id>/', views.delete_products, name='delete_products'),
    # URL: /delete-product/<id>/
    # View: views.delete_products
    # Description: Menghapus produk
    # Methods: POST (memproses penghapusan produk)
    # AJAX Support: Ya (mengembalikan JSON dengan pesan sukses)
    # Authentication Required: Ya
    # Authorization: Hanya owner produk yang bisa hapus
    
    # =========================================================================
    # API ENDPOINTS (JSON/XML)
    # =========================================================================
    
    path('xml/', views.show_xml, name='show_xml'),
    # URL: /xml/
    # View: views.show_xml
    # Description: Mengembalikan semua produk dalam format XML
    # Methods: GET
    # AJAX Support: Tidak (mengembalikan raw XML)
    
    path('json/', views.show_json, name='show_json'),
    # URL: /json/
    # View: views.show_json
    # Description: Mengembalikan semua produk dalam format JSON
    # Methods: GET
    # AJAX Support: Tidak (mengembalikan raw JSON)
    
    path('xml/<uuid:products_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    # URL: /xml/<products_id>/
    # View: views.show_xml_by_id
    # Description: Mengembalikan produk spesifik dalam format XML
    # Methods: GET
    # AJAX Support: Tidak (mengembalikan raw XML)
    # Parameters:
    #   - products_id: UUID produk yang ingin dilihat
    
    path('json/<uuid:products_id>/', views.show_json_by_id, name='show_json_by_id'),
    # URL: /json/<products_id>/
    # View: views.show_json_by_id
    # Description: Mengembalikan produk spesifik dalam format JSON
    # Methods: GET
    # AJAX Support: Tidak (mengembalikan raw JSON)
    # Parameters:
    #   - products_id: UUID produk yang ingin dilihat
    
    # =========================================================================
    # AJAX-SPECIFIC ENDPOINTS
    # =========================================================================
    
    path('ajax/increment-views/<uuid:id>/', views.increment_views_ajax, name='increment_views_ajax'),
    # URL: /ajax/increment-views/<id>/
    # View: views.increment_views_ajax
    # Description: AJAX endpoint untuk increment view counter produk
    # Methods: POST
    # AJAX Support: Ya (khusus untuk AJAX request)
    # Parameters:
    #   - id: UUID produk yang akan di-increment view-nya
    # Response:
    #   - Success: {status: 'success', views: X, is_products_hot: bool}
    #   - Error: {status: 'error', message: 'Product not found'}

    # Path untuk proxy image
    path('proxy-image/', views.proxy_image, name='proxy_image'),

    # Path untuk membuat products melalui flutter
    path('create-product-flutter/', views.create_product_flutter, name='create_product_flutter'),

    # Path untuk akses fungsi mendapatkan produk berdasarkan user yang login
    path('user-products-json/', views.get_user_products_json, name='user_products_json'),
    path('user-products-detail/', views.get_user_products_detail, name='user_products_detail'),
]