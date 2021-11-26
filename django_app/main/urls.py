from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.request_logout, name='logout'),

    path('buy/', views.buy, name="buy"),
    path('reserve/', views.reserve, name="reserve"),
    path('borrow/', views.borrow, name="borrow"),

    #path('register', views.register, name="register"),
    path('admin.html', views.admin, name="admin"),
    path('student/<int:pk_id>/', views.student, name='student')
]
