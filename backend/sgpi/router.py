from item.api.viewsets import ItensViewSet, FabricanteViewSet, FamiliaViewSet
from item.api.viewsets import TipoViewSet, LinhaViewSet
from rest_framework import routers

rota = routers.DefaultRouter()
rota.register('itens', ItensViewSet, basename='api_itens')
rota.register('itens/fabricante', FabricanteViewSet, basename='api_itens_fabricante')
rota.register('itens/familia', FamiliaViewSet, basename='api_itens_familia')
rota.register('itens/tipo', TipoViewSet, basename='api_itens_tipo')
rota.register('itens/linha', LinhaViewSet, basename='api_itens_linha')

urlpatterns = rota.urls