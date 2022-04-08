from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertisement.views import AdvertisementViewSet, CategoriesViewSet

router = DefaultRouter()
router.register('', AdvertisementViewSet)
router.register('categories', CategoriesViewSet)

urlpatterns = [
    # path('', AdvertisementsListView.as_view()),
    # path('create/', CreateAdvertisementView.as_view()),
    # path('delete/<int:pk>/', DeleteAdvertisementView.as_view()),
    # path('details/<int:pk>/', AdvertisementDetailsView.as_view()),
    # path('update/<int:pk>/', UpdateAdvertisementView.as_view()),
    # path('', AdvertisementViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('<int:pk>/', AdvertisementViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }))
    path('', include(router.urls))
]
