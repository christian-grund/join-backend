from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from board.models import TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        # fields = ['id', 'title', 'created_at', 'checked']
        fields = '__all__'
        # read_only_fields = '__all__' # ['user']

class TaskItemViewSet(viewsets.ModelViewSet):
    serializer_class = TaskItemSerializer
    queryset = TaskItem.objects.all()
    permission_classes = [] # IsAuthenticated

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
