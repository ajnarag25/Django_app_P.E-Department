from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('buy.html', views.buy, name="buy"),
    path('reserve.html', views.reserve, name="reserve"),
    path('borrow.html', views.borrow, name="borrow"),

    path('login.html', views.login, name="login"),
    path('register.html', views.register, name="register"),
    path('admin.html', views.admin, name="admin"),
    
]
