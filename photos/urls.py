from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import UploadPhoto, GetAllPhotos, GetUserPhoto

urlpatterns = [
    path('upload_photo/', UploadPhoto.as_view()),
    path('all_photos/', GetAllPhotos.as_view()),
    path('photo/<int:user>/', GetUserPhoto.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)