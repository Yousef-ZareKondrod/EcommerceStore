from product.models import Product


class Cart():
    """
    a base cart class
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        adding users cart session data
        :param product:
        :return:
        """
        product_id = str(product.id)

        # if product_id not in self.cart:
        #     self.cart[product_id] = {
        #         'price': int(product.price),
        #         'qty': int(qty)
        #     }
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        product_id --> session data --> query database --> return products
        :return:
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        get the cart data and count the qty of theme
        :return:
        """
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        subtotal = sum(int(item['price']) * item['qty'] for item in self.cart.values())

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
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product, qty):
        """
        updating item from session data
        :param product_id:
        :param product_qty:
        :return:
        """
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
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
