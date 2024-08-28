from rest_framework import serializers
from django.contrib.auth.models import User

from board.models import ContactItem, TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'
        read_only_fields = ['id', 'user'] 


class ContactItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactItem
        fields = '__all__'
        read_only_fields = ['id', 'user']
        extra_kwargs = {
            'color': {'required': False},
            'nr': {'required': False},
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'id']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

