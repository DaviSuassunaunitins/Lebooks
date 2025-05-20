from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros
from .forms import LivroForm

def one(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def biblioteca(request):
    livros = Livros.objects.all().order_by('-created_at', '-update_at')
    return render(request, 'pag/biblioteca.html', {'livros': livros})

def livroView(request, id):
    livro = get_object_or_404(Livros, pk=id)
    return render(request, 'pag/livro.html', {'livro':livro})