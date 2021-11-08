from product.models import Product


class Card():
    """
    a base card class
    """

    def __init__(self, request):
        self.session = request.session
        card = self.session.get('session_key')
        if 'session_key' not in request.session:
            card = self.session['session_key'] = {}
        self.card = card

    def add(self, product, qty):
        """
        adding users card session data
        :param product:
        :return:
        """
        product_id = str(product.id)

        # if product_id not in self.card:
        #     self.card[product_id] = {
        #         'price': int(product.price),
        #         'qty': int(qty)
        #     }
        if product_id in self.card:
            self.card[product_id]['qty'] = qty
        else:
            self.card[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        product_id --> session data --> query database --> return products
        :return:
        """
        product_ids = self.card.keys()
        products = Product.products.filter(id__in=product_ids)
        card = self.card.copy()

        for product in products:
            card[str(product.id)]['product'] = product

        for item in card.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        get the card data and count the qty of theme
        :return:
        """
        return sum(item['qty'] for item in self.card.values())

    def get_total_price(self):
        subtotal = sum(int(item['price']) * item['qty'] for item in self.card.values())

        if subtotal == 0:
            shipping = int(0)

        else:
            shipping = int(11150)

        total = subtotal + shipping
        return total



    def delete(self, product):
        """
        deleting item from session data
        :param product:
        :return:
        """
        product_id = str(product)
        if product_id in self.card:
            del self.card[product_id]
            self.save()

    def update(self, product, qty):
        """
        updating item from session data
        :param product_id:
        :param product_qty:
        :return:
        """
        product_id = str(product)
        if product_id in self.card:
            self.card[product_id]['qty'] = qty
        self.save()

    def save(self):
        """
        saving the session
        :return:
        """
        self.session.modified = True

    def clear(self):
        del self.session['session_key']
        self.save()
