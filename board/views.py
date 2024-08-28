from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from board.models import ContactItem, TaskItem
from board.serializers import ContactItemSerializer, TaskItemSerializer, UserSerializer
import logging
logger = logging.getLogger(__name__)


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    return authenticate(username=user.username, password=password)

class LoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if email == "guest@web.de" and password == "Admin123":
            # Authentifiziere den Gast-User
            user = authenticate(username='guest', password='Admin123')

        if not email or not password:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=user.username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
        

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            logout(request)
            if not request.user.is_authenticated:
                return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Logout failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f'Logout failed: {e}')
            return Response({"error": "Logout failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class TaskView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        tasks = TaskItem.objects.filter(user=request.user)
        serializer = TaskItemSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        try:
            task = TaskItem.objects.get(pk=pk, user=request.user)
            serializer = TaskItemSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        try:
            task = TaskItem.objects.get(pk=pk, user=request.user)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TaskItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    

class ContactView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        contacts = ContactItem.objects.filter(user=request.user)
        serializer = ContactItemSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            contact = ContactItem.objects.get(pk=pk, user=request.user)
        except ContactItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ContactItemSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            contact = ContactItem.objects.get(pk=pk, user=request.user)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ContactItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserListView(APIView):
    permission_classes = [] 

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

class CurrentUserView(APIView):
    permission_classes = []  
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
            return Response({
                "username": user.username,
                "email": user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "No user is logged in"
            }, status=status.HTTP_401_UNAUTHORIZED)