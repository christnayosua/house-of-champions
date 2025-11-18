from django.urls import path
from authentication.views import login, logout, register

app_name = 'authentication'

urlpatterns = [
    # Akses views login untuk autentikasi 
    path('login/', login, name='login'),
    # Akses views register
    path('register/', register, name='register'),
    # Akses views logout
        path('logout/', logout, name='logout')
]