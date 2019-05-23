from rest_framework import serializers
from shop.models import Product
# from django.contrib.auth.models import User
from users.models import UserProfile
from orders.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'priceVAT', 'image')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['phone', 'userphoto']


class UserSerializer(serializers.ModelSerializer):
    userprofile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'userprofile', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        profile_data = validated_data['userprofile']
        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,)
        user_obj.set_password(password)
        user_obj.save()
        UserProfile.objects.create(user=user_obj, **profile_data)
        return validated_data


class UserUpdateSerializer(serializers.ModelSerializer):
    userprofile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'userprofile', ]

    def update(self, instance, validated_data):
        profile_data = validated_data['userprofile']
        userprofile = instance.userprofile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        userprofile.phone = profile_data.get('phone', userprofile.phone)
        userprofile.userphoto = profile_data.get('userphoto', userprofile.userphoto)
        userprofile.save()

        return instance


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'owner', 'first_name', 'last_name',
                  'email', 'order_date', 'product', 'price', 'priceVAT', 'quantity']
