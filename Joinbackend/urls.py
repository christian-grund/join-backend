from django.contrib import admin
from django.urls import path
from board.views import ContactView, TaskView, LoginView, LogoutView, SignUpView, UserListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListView.as_view(), name='users'),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskView.as_view()),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('contacts/<int:pk>/', ContactView.as_view()),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
