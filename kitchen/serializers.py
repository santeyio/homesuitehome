from rest_framework import serializers
from .models import Store, Tag, Recipe, Ingredient, Package
from common.serializers import UserFlatSerializer
from common.models import Household

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'created',
            'updated',
            'created_by',
            'household',
            'name',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'created',
            'updated',
            'created_by',
            'household',
            'name',
        ]


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'created',
            'updated',
            'created_by',
            'household',
            'name',
            'tags',
            'ingredients',
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'created',
            'updated',
            'created_by',
            'household',
            'name',
            'sources',
            'in_stock',
            'to_buy',
            'recipes',
        ]


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'created',
            'updated',
            'created_by',
            'household',
            'name',
            'package',
            'quantity',
            'purchase_date',
            'ingredient',
        ]
