from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *
import re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class ClientRegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length = 16, min_length = 8, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    # To validate data received
    def validate(self, attrs):
        email = attrs.get('email', ' ')
        if not email_pattern.match(email):
            raise serializers.ValidationError('Please enter a valid email!')
        return attrs

    # To create a new client user
    def create(self, validated_data):
        validated_data['is_active'] = False
        validated_data['is_client'] = True
        return User.objects.create_user(**validated_data)    

class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=32,min_length=8,write_only = True)
    
    class Meta:
        model = User
        fields = ['email','password']

class VendorRegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length = 16, min_length = 8, write_only=True)

    class Meta:
        model = Vendor
        fields = ['name', 'email','password', 'phone_no', 'industry_category']

    # To validate data received
    def validate(self, attrs):
        email = attrs.get('email', ' ')
        if not email_pattern.match(email):
            raise serializers.ValidationError('Please enter a valid email!')
        return attrs

    # To create a vendor user
    def create(self, validated_data):
        validated_data['is_active'] = False
        validated_data['is_vendor'] = True
        return User.objects.create_user(**validated_data)  