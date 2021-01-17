from django.urls import path
from .views import IndexView, PropostaAdd, PropostaView, PropostaEdit, PropostaDelete
from .views import ItensAlt, ItensDel, ItensAdd
from .views import ConjuntosAlt, ConjuntosDel, ConjuntosAdd


urlpatterns = [
    path('', IndexView.as_view(), name='proposta'),
    path('/add',PropostaAdd.as_view(), name='proposta_add'),
    path('/edit',PropostaEdit.as_view(), name='proposta_edit'),
    path('/proposta',PropostaView.as_view(),name='proposta_proposta'),
    path('/del', PropostaDelete.as_view(),name='proposta_del'),
    path('/itens/alt',ItensAlt.as_view(),name='itens_alt'),
    path('/itens/del',ItensDel.as_view(), name='itens_del'),
    path('/itens/add',ItensAdd.as_view(), name='itens_add'),
    path('/conjuntos/alt',ConjuntosAlt.as_view(),name='conjuntos_alt'),
    path('/conjuntos/del',ConjuntosDel.as_view(),name='conjuntos_del'),
    path('/conjuntos/add',ConjuntosAdd.as_view(),name='conjuntos_add'),
    #path('/componente', ComponenteIndexView.as_view(), name='componente'),
    #path('/componente/add', ComponenteAdd.as_view(), name='componente_add'),
    #path('/componente/edit', ComponenteEdit.as_view(), name='componente_edit'),
    #path('/componente/del', ComponenteDelete.as_view(), name='componente_del'),
]
