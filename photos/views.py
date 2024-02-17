from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PhotoSerializer

from .models import Photo
from accounts.models import CustomUser


class UploadPhoto(APIView):
    def post(self, request):
        data = request.data
        data['user'] = self.request.user.id
        print(data['user'])
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetAllPhotos(APIView):
    def get(self, request):
        qs = Photo.objects.all()
        serializer = PhotoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetUserPhoto(APIView):
    def get(self, request, user):
        qs = Photo.objects.filter(user=user)
        serializer = PhotoSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)








