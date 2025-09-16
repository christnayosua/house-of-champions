from django.urls import path
from main.views import show_main, create_items, show_items, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    # Menambahkan path untuk create dan show items

    path('create-items/', create_items, name='create_items'),
    path('items/<str:id>/', show_items, name='show_items'),

    # Menambahkan path agar dapat mengakses data dalam bentuk XML dan JSON
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),

    # Menambahkan path agar dapat mengakses data dalam bentuk XML dan JSON berdasarkan ID
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
]
