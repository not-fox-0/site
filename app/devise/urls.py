from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('product_detail/<slug:slug>', views.product_view, name='products'),
    path('register', views.register, name='register'),
    path('signin', views.login, name='signin'),
    path('logout', views.logoutUser, name='logout')
]