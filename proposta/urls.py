from django.urls import path
from .views import IndexView, PropostaAdd


urlpatterns = [
    path('', IndexView.as_view(), name='proposta'),
    path('/add',PropostaAdd.as_view(), name='proposta_add'),
    #path('/edit',PropostaEdit.as_view(), name='proposta_edit'),
    #path('/proposta',PropostaView.as_view(),name='proposta_proposta'),
    #path('/del', PropostaDelete.as_view(),name='proposta_del'),
    #path('/componente', ComponenteIndexView.as_view(), name='componente'),
    #path('/componente/add', ComponenteAdd.as_view(), name='componente_add'),
    #path('/componente/edit', ComponenteEdit.as_view(), name='componente_edit'),
    #path('/componente/del', ComponenteDelete.as_view(), name='componente_del'),
]
