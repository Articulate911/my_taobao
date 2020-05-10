from django.shortcuts import render
# from django.http import HttpResponse
from .models import Commodity, CommodityCatalog, ShoppingCart, \
    OrderForm, OrderFormCommodity, Follow, Shop, Refund, \
    Sells


def commodity_list(request):
    commodities = Commodity.objects.all()
    context = {'commodities':commodities}
    # return HttpResponse("Hello World!")
    return render(request, 'my_taobao/list.html', context)


def commodity_detail(request, id):
    commodity = Sells.objects.get(commodity__commodity_id=id)
    context = {'commodity':commodity}
    return render(request, 'my_taobao/detail.html', context)


def shopping_cart(request):
    commodities = [i.commodity for i in ShoppingCart.objects.filter(user=request.user.id)]
    context = {'commodities':commodities}
    return render(request, 'my_taobao/shopping-cart.html', context)


def order_form(request):
    orders = OrderForm.objects.filter(user=request.user.id)
    context = {'orders':orders}
    return render(request, 'my_taobao/order-form.html', context)


def order_form_detail(request, id):
    order = OrderForm.objects.get(order_form_id=id)
    commodities = OrderFormCommodity.objects.filter(order_form__order_form_id=id)
    total_price = 0
    for commodity in commodities:
        total_price = total_price + commodity.commodity_pc * commodity.commodity.price
    payment = total_price + order.freight
    context = {'order':order, 'commodities':commodities, 'total_price':total_price,'payment':payment}
    return render(request, 'my_taobao/order-form-detail.html', context)


def refund(request):
    refunds = Refund.objects.filter(user=request.user.id)
    context = {'refunds':refunds}
    return render(request, 'my_taobao/refund.html', context)


def follow(request):
    follows = Follow.objects.filter(user=request.user.id)
    context = {'follows':follows}
    return render(request, 'my_taobao/follow.html', context)


def shop(request, id):
    shop = Shop.objects.get(shop_id=id)
    context = {'shop':shop}
    return render(request, 'my_taobao/shop.html', context)


def shop_list(request, id):
    commodities = Sells.objects.filter(shop__shop_id=id)
    context = {'commodities':commodities}
    return render(request, 'my_taobao/shop-list.html', context)
