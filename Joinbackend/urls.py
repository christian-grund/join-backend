from django.contrib import admin
from django.urls import path
from board.views import TaskView, LoginView, SignUpView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
