from django.urls import path, include
from . import views
app_name = 'users'

urlpatterns = [
    #include the default auth urls(as we want to use django 's default login view )
    path('', include('django.contrib.auth.urls')),
    #registration page url
    path('register/', views.register, name='register')
]