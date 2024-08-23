from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import serializers

from board.models import ContactItem, TaskItem
from board.serializers import ContactItemSerializer, TaskItemSerializer, UserSerializer


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            logout(request)
            # Optionale zusätzliche Überprüfung, ob der Benutzer tatsächlich ausgeloggt ist
            if not request.user.is_authenticated:
                return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
            else:
                # Falls logout nicht erfolgreich war (eher ungewöhnlich)
                return Response({"error": "Logout failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            # Allgemeine Fehlerbehandlung
            print(f'Logout failed: {e}')
            return Response({"error": "Logout failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

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
            print('Task created with ID:', task.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        try:
            task = TaskItem.objects.get(pk=pk)
            serializer = TaskItemSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        try:
            task = TaskItem.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TaskItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    

class ContactView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # contacts = ContactItem.objects.filter(user=request.user)
        contacts = ContactItem.objects.all()
        serializer = ContactItemSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ContactItemSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            print('Contact created with ID:', contact.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('Serializer Error:', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        try:
            contact = ContactItem.objects.get(pk=pk)
        except ContactItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactItemSerializer(contact, data=request.data, partial=True)  # Teilweises Update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            contact = ContactItem.objects.get(pk=pk)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ContactItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserListView(APIView):
    permission_classes = [] #IsAuthenticated

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)