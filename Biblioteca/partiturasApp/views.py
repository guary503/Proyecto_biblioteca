from django.shortcuts import render, get_object_or_404  #Esto es del dia 7
from django.http import HttpResponse
from .models import Partitura, Compositor, Instrumento, PRUEBA, Genero
from .forms import PartituraForm, CompositorForm


# Create your views here.
def pagina_inicio(requests):
    """Esta es la pagina de inicio de la seccion de partituras"""
    
    html_respond = '<h1>Bienvenidos a la biblioteca de Partituras</h1><p>Esta es la pagina principal.</p>'
    return HttpResponse(html_respond)


def paginaMozart(request):
    """Esta es la pagina acerca de Mozart."""
    
    html_respond = '''<h1>Bienvenidos a la pagina "acerca de" Mozart</h1>
    <h3>Resumen de Datos</h3>
    <p>Luego de mostrar los datos esta la biografica de mozart</p>
    '''
    return HttpResponse(html_respond)


def contacto(request):
    return HttpResponse('<p>Luis.guaryto@gmail.com</p>')


def total_partituras(request):
    num_partituras = Partitura.objects.count()
    
    return HttpResponse(f'<p>Actualmente tenemos {num_partituras} partituras en la biblioteca')


def lista_partituras(request):
    '''Mi primer funcion con render, usando templates y contexto'''
    
    #Obtener los datos de los objetos en la BD de la clase Partituras.
    partituras = Partitura.objects.all().order_by('titulo')
    
    #creando el contexto, que es un diccionario con la key para llamar en la template y el value que es el valor obtenido
    contexto = {'partituras':partituras}

    #renderizar la plantilla con el contexto, toma 3 argumentos, el request, el str de el path de la template, y opcional el contexto
    return render(request, 'partiturasApp/lista_partituras.html', contexto)


def lista_compositores(request):
    """Este es mi segundo render, pero haciendolo solo"""
    #obtener los objetos
    compositores = Compositor.objects.all()
    #creando el contexto
    contexto = {'compositores':compositores}
    #retornando el render
    return render(request,'partiturasApp/lista_compositores.html',contexto) 


# dia 5 - reto - creando la view con render para servirla en urls.py
def lista_generos(request):  #crear o definir funcion
    #obtener los objetos
    generos = Genero.objects.all()
    #crear contexto
    contexto = {'generos':generos}
    #renderizar web con render y los argumentos
    return render(request, 'partiturasApp/lista_generos.html',contexto)


def detalle_partitura(request, pk):
    '''Esta vista muestra los detalles de una partitura especifica, identificada por su clave primaria (pk)'''
    #Para obtener los objetos ya no se utilizar class.objects.all(), si no que usamos get_object_or_404, porque si no la encuentra automaticamente genera un error 404.
    #su sintaxis es get_object_or_404(class, pk = ??)
    partituras = get_object_or_404(Partitura, pk = pk)
    
    #luego se crea el contexto normalmente
    contexto = {'partitura':partituras}
    return render(request, 'partiturasApp/detalle_partitura.html', contexto)


def detalle_compositor(request, pk):
    '''mi funcion de view para mostrar los detalles de el compositor, sin ayuda'''
    compositor = get_object_or_404(Compositor, pk = pk)
    contexto = {'compositor':compositor}
    return render(request, 'partiturasApp/detalle_compositor.html',contexto)


def crear_partitura(requests):  # dia 9 - creando un form, primero se importa desde .form la clase creada con form.ModelForm.
    '''Mi primera views creada con un form, es de prueba'''
    form = PartituraForm(initial={'genero':'clasico','instrumento':Instrumento.objects.get(id=3)})   #Se crea una instancia de la clase # Aca aprendi a pasar el argumento initial= que es un diccionario con valores por default, si el campo es una foreignKey debes pasar el objeto, en este caso yo paso instrumento con id=3 y funciona

    contexto = {'form':form}    #se crea el contexto y se renderiza la plantilla

    print(requests.POST)
    return render(requests, 'partiturasApp/crear_partitura.html',contexto)


def crear_compositor(requests):
    form_comp = CompositorForm()
    contexto = {'form':form_comp}

    print(requests.POST)
    return render(requests,'partiturasApp/crear_compositor.html',contexto)