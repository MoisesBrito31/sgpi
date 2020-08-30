from django.urls import path
from .views import IndexView, VaraView, VaraAdd, VaraEdit, VaraDelete, UsuarioView, UsuarioAdd, UsuarioDelete, UsuarioEdit, LoginView, Logout
from .views import ProcessoView, ProcessoAdd, ProcessoDelete, ProcessoEdit


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('usuario', UsuarioView.as_view(), name ='usuario'),
    path('usuario_add', UsuarioAdd.as_view(), name = 'usuario_add'),
    path('usuario_edit', UsuarioEdit.as_view(), name = 'usuario_edit'),
    path('usuario_delete', UsuarioDelete.as_view(), name = 'usuario_delete'),
    #path('vara', VaraView.as_view(), name ='vara'),
    #path('vara_add', VaraAdd.as_view(), name = 'vara_add'),
    #path('vara_edit', VaraEdit.as_view(), name = 'vara_edit'),
    #path('vara_delete', VaraDelete.as_view(), name = 'vara_delete'),
    #path('processo', ProcessoView.as_view(), name ='processo'),
    #path('processo_add', ProcessoAdd.as_view(), name = 'processo_add'),
    #path('processo_edit', ProcessoEdit.as_view(), name = 'processo_edit'),
    #path('processo_delete', ProcessoDelete.as_view(), name = 'processo_delete'),
]