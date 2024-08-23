from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from board.models import ContactItem, TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        # fields = ['id', 'title', 'created_at', 'checked']
        fields = '__all__'
        read_only_fields = ['id'] # 'user'


class ContactItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactItem
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'color': {'required': False},
            'nr': {'required': False},
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Passwort wird vom `create_user` automatisch gehasht
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
