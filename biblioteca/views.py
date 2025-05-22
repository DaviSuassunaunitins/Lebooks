from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Livros
from .forms import LivroForm

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('biblioteca')
        else:
            messages.error(request, 'Usuário ou senha inválidos...')
    return render(request, 'pag/login.html')

@never_cache
@login_required
def biblioteca(request):
    livros = Livros.objects.all().order_by('-created_at', '-update_at')
    return render(request, 'pag/admin.html', {'livros': livros})


def bibliotecaView(request):
    livros = Livros.objects.all().order_by('-created_at', '-update_at')
    return render(request, 'pag/biblioteca.html', {'livros': livros})

@never_cache
@login_required
def novoLivro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            livro = form.save()
            livro.save()
            return redirect('/biblioteca')
    else:
        form = LivroForm()
        return render(request, 'pag/novoLivro.html', {'form':form})

@never_cache
@login_required
def editLivro(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = LivroForm(instance=livro)

    if(request.method == 'POST'):
        form = LivroForm(request.POST, instance=livro)

        if(form.is_valid()):
            livro.save()
            return redirect('/biblioteca')
        else:
            return render(request, 'pag/editLivro.html', {'form':form, 'livro':livro})
    else: 
        return render(request, 'pag/editLivro.html', {'form':form, 'livro':livro})

def deleteLivro(request, id):
     tarefa = get_object_or_404(Livros, pk=id)
     tarefa.delete()
     return redirect('/biblioteca')

def listarLivros(request):
    buscarLivro = request.GET.get('Buscar')
    if buscarLivro:
        livros = Livros.objects.filter(título__icontains=buscarLivro)
    else:
        livros = Livros.objects.all()

    return render(request, 'pag/buscar.html', {'livros': livros})

def listarLivrosAdmin(request):
    buscarLivro = request.GET.get('Buscar')
    if buscarLivro:
        livros = Livros.objects.filter(título__icontains=buscarLivro)
    else:
        livros = Livros.objects.all()

    return render(request, 'pag/buscarAdmin.html', {'livros': livros})
