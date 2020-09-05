from django.urls import path
from .views import IndexView, ItemAdd, ItemEdit, ItemView,ItemDelete


urlpatterns = [
    path('', IndexView.as_view(), name='item'),
    path('/add',ItemAdd.as_view(),name='item_add'),
    path('/edit',ItemEdit.as_view(), name='item_edit'),
    path('/item',ItemView.as_view(),name='item_item'),
    path('/del', ItemDelete.as_view(),name='item_del'),
]