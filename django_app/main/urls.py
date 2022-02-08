from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginuser, name="login"),
    # path('administrator', views.administrator, name="administrator"),
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
    path('deleteborrow/<borrow_id>', views.deleteborrow, name="deleteborrow"),
    path('editequipment/<equipment_id>', views.editEquipment, name="editequipment"),
    path('deleteequipment/<equipment_id>', views.deleteequipment, name="deleteequipment"),
    path('success', views.SuccessPage, name="success"),
    path('transaction', views.Transaction, name="transaction"),
    path('success2', views.SuccessPage2, name="success2"),
    path('admin', views.admin, name="admin"),
    path('admin_buy', views.adminBuy, name="adminbuy"),
    path('admin_reserve', views.adminReserve, name="adminreserve"),
    path('admin_borrow', views.adminBorrow, name="adminborrow")
]
