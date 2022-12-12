from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms

# Create your views here.

def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'formulario':form, 'pessoa_formulario':pessoa_form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'formulario2':form, 'pessoa_formulario':pessoa_form}
            print('validou')
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {'formulario':form, 'pessoa_formulario':pessoa_form}
            return render(request, 'index.html', contexto)

