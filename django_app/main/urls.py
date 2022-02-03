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
    path('logout', views.logoutUser, name="logout"),
    path('editbuy/<buy_id>', views.editBuy, name="editbuy"),
    path('deletebuy/<buy_id>', views.deletebuy, name="deletebuy"),
    path('editreserve/<reserve_id>', views.editReserve, name="editreserve"),
    path('deletereserve/<reserve_id>', views.deletereserve, name="deletereserve"),
    path('editborrow/<borrow_id>', views.editBorrow, name="editborrow"),
    path('deleteborrow/<borrow_id>', views.deleteborrow, name="deleteborrow")
]
