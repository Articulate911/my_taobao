# 引入views.py
from . import views
from django.urls import path

urlpatterns = [
    # path函数将url映射到视图
    path('commodity-list/', views.commodity_list, name='commodity_list'),
    path('commodity-detail/<int:id>/', views.commodity_detail, name='commodity_detail'),
    path('my-shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('my-order-form/', views.order_form, name='order_form'),
    path('my-order-form/<int:id>', views.order_form_detail, name='order_form_detail'),
    path('my-refund/', views.refund, name='refund'),
    path('follow/',views.follow, name='follow'),
    path('shop/<int:id>', views.shop, name='shop'),
    path('shop-list/<int:id>', views.shop_list, name='shop_list'),
]