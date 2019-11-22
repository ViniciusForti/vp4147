from django.shortcuts import render, redirect
from .models import Cliente
from .form import FormCliente

# Create your views here.

def home(request):
    return render(request, 'website\index.html')

def listarCliente(request):
    dados = Cliente.objects.all();
    return render(request, 'website\listagem.html', {'clientes': dados})

def cadastrarCliente(request):
    form = FormCliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    else:
        return render(request, 'website\cadastro.html', {'form': form })

def atualizaCliente(request, pk):
    cliente=Cliente.objects.get(pk=pk)
    form = FormCliente(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    else:
        return render(request, 'website\cadastro.html', {'form': form})

def deleteCliente(request, pk):
    cliente=Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_listagem')
