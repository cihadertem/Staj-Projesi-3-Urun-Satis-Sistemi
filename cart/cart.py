from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, post, quantity=1, action=None):
        """
        Add a post to the cart or update its quantity.
        """
        id = post.id
        newItem = True
        if str(post.id) not in self.cart.keys():

            self.cart[post.id] = {
                'userid': self.request.user.id,
                'post_id': id,
                'name': post.title,
                'quantity': 1,
                'price': str(post.price),
                'image': post.post_image.url
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(post.id):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[post.id] = {
                    'userid': self.request,
                    'post_id': post.id,
                    'name': post.name,
                    'quantity': 1,
                    'price': str(post.price),
                    'image': post.post_image.url
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, post):
        """
        Remove a post from the cart.
        """
        post_id = str(post.id)
        if post_id in self.cart:
            del self.cart[post_id]
            self.save()

    def decrement(self, post):
        for key, value in self.cart.items():
            if key == str(post.id):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
