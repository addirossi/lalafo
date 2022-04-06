from django.shortcuts import render

# Create your views here.
#CRUD объявления
#проверка прав: редактировать и удалять объявление может только автор
#категории может создавать, удалять, редактировать только админ
# фильтрация, поиск, пагинация
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Advertisement
from .serializers import CreateAdSerializer, AdvertisementListSerializer


class CreateAdvertisementView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = CreateAdSerializer
    permission_classes = [IsAuthenticated]


class AdvertisementsListView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer


class AdvertisementDetailsView(RetrieveAPIView):
    pass


class UpdateAdvertisementView(UpdateAPIView):
    pass


class DeleteAdvertisementView(DestroyAPIView):
    queryset = Advertisement.objects.all()
