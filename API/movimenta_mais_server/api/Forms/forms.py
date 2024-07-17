from django import forms
from ..models import Exame  

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ('cpf_idoso', 'title', 'file')  # Certifique-se de incluir todos os campos necessários

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf_idoso'].widget.attrs['readonly'] = True  # CPF deve ser apenas para leitura