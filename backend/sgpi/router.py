from item.api.viewsets import ItensViewSet
from rest_framework import routers

rota = routers.DefaultRouter()
rota.register('itens', ItensViewSet, basename='api_itens')

urlpatterns = rota.urls