from django.shortcuts import render
from django.views.generic import View
from .forms import UsuarioForm
from .models import Usuario


class LoginView(View):
    context = {
        'titulo':'Login',
        'user': '',
        'msg': 'ok',
        'dados' : '',
    }
    def get(self, request):
        self.context['msg'] = 'ok'
        return render(request, 'login.html', self.context)

    def post(self, request):
        try:
            us = request.POST['email']
            sh = request.POST['senha']
            try:
                alvo = request.COOKIES['redirect']
            except:
                alvo = '/'
            use = Usuario.objects.get(email=us, senha=sh)
            use.loggin()
            use.save()
            response = HttpResponseRedirect(alvo)
            set_cookie(response, 'userID',use.token)
            return response
        except:
            self.context['msg'] = 'falha'
            return render(request, 'login.html', self.context)

