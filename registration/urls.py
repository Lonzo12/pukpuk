from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('vhod/', LoginUser.as_view(), name='login'),
    path('reg/', RegisterUser.as_view(), name = 'reg'),
    path('cart/', cartview,name='cart'),
    path('cart/sendmail', sendmail,name='sendmail'),
    path('cart/update/<int:item_id>/', update_cart, name='update_cart'),
    path('profile/', update_profile,name='profile'),
    path('aprofile/', add_product,name='aprofile'),
    path('logout/', logout_user,name='logout'),
    path('bron/', product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]