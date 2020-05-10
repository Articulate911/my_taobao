from django.contrib import admin

# Register your models here.
from .models import Commodity, CommodityCatalog, Follow,\
    OrderForm, OrderFormCatalog, OrderFormCommodity, Refund,\
    Sells, Shop, ShoppingCart

admin.site.register([Commodity, CommodityCatalog, Follow,\
    OrderForm, OrderFormCatalog, OrderFormCommodity, Refund,\
    Sells, Shop, ShoppingCart])