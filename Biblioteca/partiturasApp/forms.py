from django import forms
from .models import Partitura, PRUEBA, Compositor, Genero

class PartituraForm(forms.ModelForm):
    
    class Meta:
        model = Partitura
        fields = ("titulo",'compositor','instrumento','genero')


class CompositorForm(forms.ModelForm):
    
    class Meta:
        model = Compositor
        fields = '__all__'