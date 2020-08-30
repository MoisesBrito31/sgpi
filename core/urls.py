from django.urls import path
from .views import IndexView, LoginView, Logout
from .views import UsuarioView, UsuarioAdd, UsuarioDelete, UsuarioEdit



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('usuario', UsuarioView.as_view(), name ='usuario'),
    path('usuario_add', UsuarioAdd.as_view(), name = 'usuario_add'),
    path('usuario_edit', UsuarioEdit.as_view(), name = 'usuario_edit'),
    path('usuario_delete', UsuarioDelete.as_view(), name = 'usuario_delete'),
]