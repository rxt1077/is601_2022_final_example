from django.shortcuts import render
from .models import OrderForm, Order
from django.http import HttpResponseRedirect
from django.urls import reverse

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total = 0
            for baked_good in form.cleaned_data['baked_goods']:
                total += baked_good.price
            form.instance.total_cost = total
            instance = form.save()
            return HttpResponseRedirect(reverse('info', args=[instance.id]))
    else:
        form = OrderForm()

    return render(request, 'pos/order.html', {'form': form})

def order_info(request, id):
    order = Order.objects.get(pk=id)
    return render(request, 'pos/order_info.html', {'order': order})