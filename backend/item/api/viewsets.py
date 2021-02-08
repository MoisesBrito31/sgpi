from item.models import Item, Fabricante, Familia, Tipo, Linha
from .serializers import ItensSerializer, FabricanteSerializer, FamiliaSerializer
from .serializers import TipoSerializer, LinhaSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class LinhaViewSet(ModelViewSet):
    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class TipoViewSet(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class FamiliaViewSet(ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ItensViewSet(ModelViewSet):
    serializer_class = ItensSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Item.objects.all()
        fabri = self.request.query_params.get('fabricante',None)
        if fabri is not None:
            queryset = queryset.filter(fabricante=fabri)
        tipo = self.request.query_params.get('tipo',None)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        return queryset
    