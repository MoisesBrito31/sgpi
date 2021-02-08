from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cliente.models import Cargo, Responsavel, Relacao, Industria, Cliente
from .serializers import CargoSerializer, ResponsavelSerializer, RelacaoSerializer
from .serializers import IndustriaSerializer, ClienteSerializer


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class RelacaoViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Relacao.objects.all()
        empresa = self.request.query_params.get('empresa',None)
        if empresa is not None:
            queryset = queryset.filter(empresa=empresa)
        return queryset
    serializer_class = RelacaoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ResponsavelViewSet(ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class IndustriaViewSet(ModelViewSet):
    queryset = Industria.objects.all()
    serializer_class = IndustriaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)