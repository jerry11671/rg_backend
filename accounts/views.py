from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import RegistrationSerializer

class CustomUserRegistration(APIView):
    def post(self, request):
        data = self.request.data
        email = data['email']
        password = data['password']
        new_pass = ""

        try:
            user_obj = CustomUser.objects.get(email=email)
            new_pass = user_obj.password
        except CustomUser.DoesNotExist:
            pass

        # if not CustomUser.objects.filter(email=email, password=password).exists():
        if not check_password(password, new_pass):
            serializer = RegistrationSerializer(data=data)
            if serializer.is_valid():
                password = serializer.validated_data['password']
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response({'message': 'Account created',
                                 'data': serializer.data,
                                 'acess': str(refresh.access_token),
                                 }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        existing_user = CustomUser.objects.get(email=email)
        exist_serializer = RegistrationSerializer(existing_user)
        refresh = RefreshToken.for_user(existing_user)
        return Response({
            'message': 'You already have an account',
            'data': exist_serializer.data,
            'access':  str(refresh.access_token),
        })
    

class GetAllUsers(APIView):
    def get(self, request):
        qs = CustomUser.objects.all()
        serializer = RegistrationSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)