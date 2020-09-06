from django.urls import path
from .views import IndexView, ClienteAdd, ClienteView, ClienteEdit, ClienteDelete


urlpatterns = [
    path('', IndexView.as_view(), name='cliente'),
    path('/add',ClienteAdd.as_view(),name='cliente_add'),
    path('/edit',ClienteEdit.as_view(), name='cliente_edit'),
    path('/cliente',ClienteView.as_view(),name='cliente_cliente'),
    path('/del', ClienteDelete.as_view(),name='cliente_del'),
]