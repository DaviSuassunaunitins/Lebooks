from django import forms

from .models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('título', 'autor', 'páginas', 'ano', 'gênero_1', 'gênero_2', 'gênero_3', 'disponível')