from django import forms
from .models import Partitura, PRUEBA, Compositor, Genero

class PartituraForm(forms.ModelForm):
    
    class Meta:
        model = Partitura
        fields = '__all__'


class CompositorForm(forms.ModelForm):
    
    class Meta:
        model = Compositor
        fields = '__all__'
        
class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = '__all__'
        
