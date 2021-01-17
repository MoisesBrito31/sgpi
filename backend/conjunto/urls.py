from django.urls import path
from .views import IndexView ,ConjuntoView, ConjuntoAdd, ConjuntoDelete, ConjuntoEdit
from .views import ComponenteIndexView, ComponenteAdd, ComponenteEdit, ComponenteDelete
from .views import RelacaoAlt, RelacaoAdd, RelacaoDel


urlpatterns = [
    path('', IndexView.as_view(), name='conjunto'),
    path('/add',ConjuntoAdd.as_view(),name='conjunto_add'),
    path('/edit',ConjuntoEdit.as_view(), name='conjunto_edit'),
    path('/conjunto',ConjuntoView.as_view(),name='conjunto_conjunto'),
    path('/del', ConjuntoDelete.as_view(),name='conjunto_del'),
    path('/componente', ComponenteIndexView.as_view(), name='componente'),
    path('/componente/add', ComponenteAdd.as_view(), name='componente_add'),
    path('/componente/edit', ComponenteEdit.as_view(), name='componente_edit'),
    path('/componente/del', ComponenteDelete.as_view(), name='componente_del'),
    path('/relacao/alt',RelacaoAlt.as_view(),name='relacao_alt'),
    path('/relacao/add',RelacaoAdd.as_view(),name='relacao_add'),
    path('/relacao/del',RelacaoDel.as_view(),name='relacao_del'),

]
