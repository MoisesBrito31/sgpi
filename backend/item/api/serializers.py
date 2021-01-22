from rest_framework.serializers import ModelSerializer as model
from item.models import Item,Fabricante,Familia,Linha,Tipo

class TipoSerializer(model):
    class Meta:
        model = Tipo
        fields = '__all__'

class LinhaSerializer(model):
    class Meta:
        model = Linha
        fields = '__all__'

class FamiliaSerializer(model):
    class Meta:
        model = Familia
        fields = '__all__'

class FabricanteSerializer(model):
    class Meta:
        model = Fabricante
        fields = '__all__'

class ItensSerializer(model):
    class Meta:
        model = Item
        fields = '__all__'