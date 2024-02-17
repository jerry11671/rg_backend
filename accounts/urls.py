from django.urls import path
from .views import CustomUserRegistration, GetAllUsers
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', CustomUserRegistration.as_view()),
    path('all_users/', GetAllUsers.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
