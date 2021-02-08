from item.api.viewsets import ItensViewSet, FabricanteViewSet, FamiliaViewSet
from item.api.viewsets import TipoViewSet, LinhaViewSet
from cliente.api.viewsets import CargoViewSet, ResponsavelViewSet, RelacaoViewSet
from cliente.api.viewsets import IndustriaViewSet, ClienteViewSet
from rest_framework import routers

rota = routers.DefaultRouter()
rota.register('itens', ItensViewSet, basename='api_itens')
rota.register('itens-fabricante', FabricanteViewSet, basename='api_itens_fabricante')
rota.register('itens-familia', FamiliaViewSet, basename='api_itens_familia')
rota.register('itens-tipo', TipoViewSet, basename='api_itens_tipo')
rota.register('itens-linha', LinhaViewSet, basename='api_itens_linha')

rota.register('clientes',ClienteViewSet,basename='api_clientes')
rota.register('clientes-industria', IndustriaViewSet,basename='api_clientes_indu')
rota.register('clientes-relacao',RelacaoViewSet,basename='api_clientes_rela')
rota.register('clientes-cargo',CargoViewSet,basename='api_clientes_carg')
rota.register('clientes-responsavel',ResponsavelViewSet,basename='api_clientes_resp')

urlpatterns = rota.urls