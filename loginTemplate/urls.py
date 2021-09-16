from django.contrib import admin
from django.urls import path , include
from accounts import views as v
from main import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/home/' , views.home , name = 'home'),
    path('', v.register , name='register'),
    path('' , include('django.contrib.auth.urls') , name = 'login'),
]
