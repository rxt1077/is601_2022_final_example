from django.db import models
from example_app.models import BakedGood
from django.forms import ModelForm

class Order(models.Model):
    baked_goods = models.ManyToManyField(BakedGood)
    instructions = models.TextField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['baked_goods', 'instructions']
