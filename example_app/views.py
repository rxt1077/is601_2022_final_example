from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render 
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BakedGoodSerializer, IngredientSerializer

from .models import BakedGood, BakedGoodForm, Ingredient

def index(request):
    baked_goods = BakedGood.objects.all() 
    context = {'baked_goods': baked_goods} 
    return render(request, 'example_app/index.html', context)

def bake(request): 
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()

    return render(request, 'example_app/bake.html', {'form': form})

def ajax(request):
    baked_goods = BakedGood.objects.all()

    json_response = {}
    i = 0
    for baked_good in baked_goods:
        json_response[i] = baked_good.desc

    return JsonResponse(json_response)

class BakedGoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows baked goods to be viewed or edited.
    """
    queryset = BakedGood.objects.all()
    serializer_class = BakedGoodSerializer
    permission_classes = [permissions.AllowAny]

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]

def allauth(request):
    return render(request, 'example_app/allauth.html')