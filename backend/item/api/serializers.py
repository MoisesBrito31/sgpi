from rest_framework.serializers import HyperlinkedModelSerializer as model
from item.models import Item

class ItensSerializer(model):
    class Meta:
        model = Item
        fields = ('id','nome','preco','descricao')