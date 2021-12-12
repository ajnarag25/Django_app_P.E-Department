from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginuser, name="login"),
    path('administrator', views.administrator, name="administrator"),
    path('mainpage', views.index, name="index"),
    path('buy', views.buy, name="buy"),
    path('reserve', views.reserve, name="reserve"),
    path('borrow', views.borrow, name="borrow"),
    path('register', views.register, name="register"),
    path('student/<student_id>/', views.student, name='student'),

    path('logout', views.logoutUser, name="logout"),

    path('delete_student/<student_id>', views.delete_student, name="delete_student")
]
