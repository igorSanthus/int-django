from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from  django.template import loader


def index(request):
   # print(dir(request))
    print(f"User-Agent:{request.headers['User-Agent']}")
    if str(request.user)=='AnonymousUser':
        teste="Usuario não logado"
    else:
        teste="Usuario  logado"

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django',
        'outro': 'Continue',
        'produtos':produtos,
        'logado':teste,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request,pk):
    #prod=Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod,
    }
    print(f"PK {pk}")
    return render(request,'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8', status=404)
    #return render(request,'404.html')

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8', status=500)
    #return render(request,'404.html')