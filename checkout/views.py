from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IrNo3B25QdTia8SkI6y9wq5VR3hTDquGJnPKjSniCZLUqXDAUMJLqCA7N4CZHtV7HvkCzvURGpYjgN2newA0ly400k4RYLzsY',
        'client_secret': 'client_secret_key',
    }

    return render(request, template, context)