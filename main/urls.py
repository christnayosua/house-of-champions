from django.urls import path
from main.views import show_main, create_items, show_items, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    # Menambahkan path untuk create dan show items

    path('create-items/', create_items, name='create_items'),
    path('items/<str:id>/', show_items, name='show_items'),
]
