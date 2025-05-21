from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.bibliotecaView, name='bibliotecaView'),
    path('edit/<int:id>', views.editLivro, name='edit-livro'),
    path('login', views.loginView, name='login' ),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('logout', auth_views.LogoutView.as_view(next_page='bibliotecaView'), name='logout'),
    path('novoLivro', views.novoLivro, name='novo-livro'),
    path('delete/<int:id>', views.deleteLivro, name='deleteLivro'),
    path('lista/', views.listarLivros, name='listar_livros'),
    path('listaAdmin/', views.listarLivrosAdmin, name='listar_livros_admin'),
]