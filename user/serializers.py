from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True}
        }

    def validate(self, data):
        # Validate name length
        if len(data['name']) < 3:
            raise serializers.ValidationError({"name": "Name must be at least 3 characters long"})

        # Validate password length
        if len(data['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long"})

        # Check if email already exists
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists"})

        return data

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
