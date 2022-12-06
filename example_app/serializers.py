from .models import BakedGood, Ingredient
from rest_framework import serializers

class BakedGoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BakedGood
        fields = ['name', 'desc', 'good_type', 'price', 'recipe', 'ingredients', 'baked_on']

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'desc']