from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from board.models import TaskItem
from board.serializers import TaskItemSerializer, UserSerializer


# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]  # Erlaubt Zugriff für jeden Benutzer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    pass
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    #     return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class TaskView(APIView):
    authentication_classes = [] # TokenAuthentication
    permission_classes = [] # IsAuthenticated

    def get(self, request, format=None):
        # tasks = TaskItem.objects.filter(user=request.user)
        tasks = TaskItem.objects.all()
        serializer = TaskItemSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskItemSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            print('Task created with ID:', task.id)  # Debug-Ausgabe
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('Validation errors:', serializer.errors)  # Debug-Ausgabe
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

