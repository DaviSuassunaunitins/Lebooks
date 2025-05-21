from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.bibliotecaView, name='bibliotecaView'),
    # path('livro/<int:id>', views.livroView, name='livro-view'),
    path('edit/<int:id>', views.editLivro, name='edit-livro'),
    path('login', views.loginView, name='login' ),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('logout/', auth_views.LogoutView.as_view(next_page='bibliotecaView'), name='logout'),
]