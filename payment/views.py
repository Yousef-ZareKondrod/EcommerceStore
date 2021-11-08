import stripe as stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from card.card import Card
from order.models import Order, OrderItem

# from suds.client import Client




@login_required
def CardView(request):
    global orderitem
    card = Card(request)
    total = str(card.get_total_price())
    cardtotal = card.get_total_price()
    card = card.session.get('session_key')

    user_id = request.user.id


    order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                 address2='add2', total_paid=cardtotal, order_key='', billing_status=True)
    order_id = order.pk
    for item in card:
        orderitem = OrderItem.objects.create(order_id=order_id, product_id=item, price=card[item]['price'],
                                             quantity=card[item]['qty'])
    if order.pk and orderitem.pk:
        order_placed(request)
        return render(request, 'store/payment/orderplaced.html')
    else:
        return render(request, 'store/payment/notdone.html')


# MMERCHANT_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'  # Required
# ZARINPAL_WEBSERVICE = 'https://www.zarinpal.com/pg/services/WebGate/wsdl'  # Required
# amount = 1000  # Amount will be based on Toman  Required
# description = u'توضیحات تراکنش تستی'  # Required
# email = 'user@userurl.ir'  # Optional
# mobile = '09123456789'  # Optional
# CallbackURL = 'http://127.0.0.1:8000/verify/'
#
#
# def send_request(request):
#     client = Client(ZARINPAL_WEBSERVICE)
#     result = client.service.PaymentRequest(MMERCHANT_ID,
#                                            amount,
#                                            description,
#                                            email,
#                                            mobile,
#                                            CallbackURL)
#     if result.Status == 100:
#         return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
#     else:
#         return HttpResponse('Error')
#
#
# def verify(request):
#     client = Client(ZARINPAL_WEBSERVICE)
#     if request.GET.get('Status') == 'OK':
#         result = client.service.PaymentVerification(MMERCHANT_ID,
#                                                     request.GET['Authority'],
#                                                     amount)
#         if result.Status == 100:
#             return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
#         elif result.Status == 101:
#             return HttpResponse('Transaction submitted : ' + str(result.Status))
#         else:
#             return HttpResponse('Transaction failed. Status: ' + str(result.Status))
#     else:
#         return HttpResponse('Transaction failed or canceled by user')


def order_placed(request):
    card = Card(request)
    card.clear()
    return render(request, 'store/payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'store/payment/error.html'
