from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from cart.card import Card
from product.models import Product


def card_summary(request):
    card = Card(request)
    return render(request, 'store/card/summary.html', {'card': card})


def card_add(request):
    card = Card(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        card.add(product=product, qty=product_qty)

        cardqty = card.__len__()
        response = JsonResponse({'qty': cardqty})
        return response


def card_delete(request):
    card = Card(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        card.delete(product=product_id)

        cardqty = card.__len__()
        cardtotal = card.get_total_price()
        response = JsonResponse({'qty': cardqty, 'subtotal': cardtotal})
        return response


def card_update(request):
    card = Card(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        card.update(product=product_id, qty=product_qty)

        cardqty = card.__len__()
        cardtotal = card.get_total_price()
        response = JsonResponse({'qty': cardqty, 'subtotal': cardtotal})
        return response
