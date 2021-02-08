from rest_framework.serializers import ModelSerializer as model
from cliente.models import Cargo, Cliente, Industria, Responsavel, Relacao
from item.models import Item

class CargoSerializer(model):
    class Meta:
        model = Cargo
        fields = '__all__'

class ClienteSerializer(model):
    class Meta:
        model = Cliente
        fields = '__all__'

class IndustriaSerializer(model):
    class Meta:
        model=Industria
        fields = '__all__'

class ResponsavelSerializer(model):
    class Meta:
        model = Responsavel
        fields = '__all__'

class RelacaoSerializer(model):
    class Meta:
        model = Relacao
        fields = '__all__'