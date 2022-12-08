from django.contrib import admin
from django.urls import path
from Purchase.views import homepage,purchase_contract_list,purchase_contract_add, approve, delete_contract, edit_contract, login, logout,reject,send_mail_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="home"),
    path('purchase-contract-list',purchase_contract_list,name="purchase_contract_list"),
    path('purchase-contract-add',purchase_contract_add,name="Purchase Contract Add"),
    path('approve/<str:id>',approve,name="approve"),
    path('delete/<str:id>',delete_contract),
    path('edit/<str:id>',edit_contract,name="edit_contract"),
    path('reject/<str:id>',reject,name="reject"),
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
    path('sendmail',send_mail_main,name="send_mail_main"),
]
