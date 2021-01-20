from item.models import Item
from .serializers import ItensSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ItensViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItensSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    