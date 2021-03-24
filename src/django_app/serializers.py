from rest_framework import serializers
from .models import User, Item
from django.contrib.auth.hashers import make_password

class ItemObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id', 
            'nickname', 
            'brand', 
            'model_name',
            'model_year',  
            'item_type', 
            'condition', 
            'image_url',
            'rating', 
        )

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'hometown'
        )

class ItemSerializer(serializers.ModelSerializer):
    # user = UserObjectSerializer(many=False)

    class Meta:
        model = Item
        fields = (
            'id', 
            'nickname', 
            'brand', 
            'model_name',
            'model_year',  
            'item_type', 
            'condition', 
            'rating',
            'image_url',
            "user" 
        ) 

class UserSerializer(serializers.ModelSerializer):
    # items = serializers.StringRelatedField(many=True)
    items = ItemObjectSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'items'
        )
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
        )

        user.save()
        return user






