
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',v.home),
    path('addUser',v.addUser),
    path('userlogin',v.Mylogin),
    path('logOut',v.logOut),
    path('checkimage',v.checkimage),
    path('editUser',v.editUser),
    path('getbyCategory',v.getbyCategory),
    path('searchPage',v.searchPage),
    path('Search',v.search),
    path('getCart',v.AddCart),
    path('cartList',v.cartList),
    path('productlist',v.productlist),
    path('ordered',v.ordered)

]
