from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('mainpage', views.index, name="index"),
    path('buy', views.buy, name="buy"),
    path('reserve', views.reserve, name="reserve"),
    path('borrow', views.borrow, name="borrow"),

    path('register', views.register, name="register"),
    path('admin.html', views.admin, name="admin"),
    path('student/<int:pk_id>/', views.student, name='student'),
]
