from webbrowser import get
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Data

def index(request):

    servicos = Data.objects.all()

    dados= {
        'servicos' : servicos
    }
    return render(request, 'index.html', dados)

def servico(request, servico_id):
    servico = get_object_or_404(Data, pk=servico_id)
    
    servico_a_exibir = {
        'servico' : servico
    }
    return render(request, 'servico.html', servico_a_exibir)

