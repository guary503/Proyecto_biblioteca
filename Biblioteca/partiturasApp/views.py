from django.shortcuts import render, get_object_or_404, redirect  #Esto es del dia 7
from django.http import HttpResponse
from .models import Partitura, Compositor, Instrumento, PRUEBA, Genero
from .forms import PartituraForm, CompositorForm


# Create your views here.
def pagina_inicio(request):
    """Esta es la pagina de inicio de la seccion de partituras"""
    
    #html_respond = '<h1>Bienvenidos a la biblioteca de Partituras</h1><p>Esta es la pagina principal.</p>'
    #return HttpResponse(html_respond)
    
    return render(request, 'PartiturasApp/base.html')


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
    partituras = Partitura.objects.all()
    
    #creando el contexto, que es un diccionario con la key para llamar en la template y el value que es el valor obtenido
    contexto = {'partituras':partituras}

    #renderizar la plantilla con el contexto, toma 3 argumentos, el request, el str de el path de la template, y opcional el contexto
    return render(request, 'partiturasApp/partitura/lista_partituras.html', contexto)


def lista_compositores(request):
    """Este es mi segundo render, pero haciendolo solo"""
    #obtener los objetos
    compositores = Compositor.objects.all()
    #creando el contexto
    contexto = {'compositores':compositores}
    #retornando el render
    return render(request,'partiturasApp/compositor/lista_compositores.html',contexto) 


# dia 5 - reto - creando la view con render para servirla en urls.py
def lista_generos(request):  #crear o definir funcion
    #obtener los objetos
    generos = Genero.objects.all()
    #crear contexto
    contexto = {'generos':generos}
    #renderizar web con render y los argumentos
    return render(request, 'partiturasApp/partitura/lista_generos.html',contexto)


def detalle_partitura(request, pk):
    '''Esta vista muestra los detalles de una partitura especifica, identificada por su clave primaria (pk)'''
    #Para obtener los objetos ya no se utilizar class.objects.all(), si no que usamos get_object_or_404, porque si no la encuentra automaticamente genera un error 404.
    #su sintaxis es get_object_or_404(class, pk = ??)
    partituras = get_object_or_404(Partitura, pk = pk)
    
    #luego se crea el contexto normalmente
    contexto = {'partitura':partituras}
    return render(request, 'partiturasApp/partitura/detalle_partitura.html', contexto)


def detalle_compositor(request, pk):
    '''mi funcion de view para mostrar los detalles de el compositor, sin ayuda'''
    compositor = get_object_or_404(Compositor, pk = pk)
    contexto = {'compositor':compositor}
    return render(request, 'partiturasApp/compositor/detalle_compositor.html',contexto)


def crear_partitura(request):  
    '''Mi primera views creada con un form, obteniendo un parametro de url con ?'''   # dia 10, se debe verificar tambien
    if request.method == 'POST':
        form = PartituraForm(request.POST)  #se crea una instancia de el form para la informacion de el POST
        if form.is_valid():
            form.save()
            return redirect('lista_partituras') #me dio error por no poner un return en caso de si el form no es valido.
        
    else:
        #Esto es del dia 10, verificamos que se obtenga con get del Dict de la peticion GET, si no, se asigna None por default.
        compositor_id = request.GET.get('compositor_id', None) #Se debe tomar siempre el mismo nombre de la variable que envia en el GET el html. es muy importante.
        
        initial_data = {}   # aca se pre-llenaria el formulario con las sugerencias
        
        if compositor_id:   #si compositor_id no es None, osea obtuvo un valor, agg el id compositor
            initial_data['compositor'] = compositor_id  #se agg el id del compositor
            
        form = PartituraForm(initial=initial_data)   #Se crea una instancia de la clase # Aca aprendi a pasar el argumento initial= que es un diccionario con valores por default, si el campo es una foreignKey debes pasar el id del objeto, en este caso yo paso una variable que obtengo del html con GET, que me dice que compositor es para agg una partitura a ese compositor.

    contexto = {'form':form}    #se crea el contexto y se renderiza la plantilla
    print(request.POST)
    return render(request, 'partiturasApp/partitura/crear_partitura.html',contexto)



def crear_compositor(request):
    if request.method == 'POST':
        form_comp = CompositorForm(request.POST)
        if form_comp.is_valid():
            form_comp.save()
            return redirect('lista_compositores')
    else:    
        form_comp = CompositorForm()
    
    contexto = {'form':form_comp}
    return render(request,'partiturasApp/compositor/crear_compositor.html',contexto)



def actualizar_partitura(request, pk):
    partitura = get_object_or_404(Partitura, pk=pk) #se obtiene la partitura a actualizar
    if request.method == 'POST':    #si envia el formulario se actualizara si no es un get y solo se muestra.
        form = PartituraForm(request.POST, instance=partitura)  #se crea un form con el post, y con la instance que en este caso es el objeto a actualizar
        if form.is_valid(): #validacion
            form.save() #guardado
            return redirect('detalle_partitura', pk=partitura.pk)
    else:
        form = PartituraForm(instance=partitura)    #si solo es un get, usamos el objeto para la instance y que se pre llene con lo que ya tiene de informacion el objeto
    
    context = {'form':form,'partitura':partitura}
    return render(request, 'partiturasApp/partitura/edit_partitura.html',context)



def actualizar_compositor(request, pk):
    compositor = get_object_or_404(Compositor, pk=pk)
    if request.method == 'POST':
        form = CompositorForm(request.POST, instance=compositor)
        if form.is_valid():
            form.save()
            return redirect('detalle_compositor', pk=compositor.pk)
    else:
        form = CompositorForm(instance=compositor)
    context = {'form':form,'compositor':compositor}
    return render(request, 'partiturasApp/compositor/edit_compositor.html',context)


def borrar_objeto(request, pk, tipo_objeto):
    object = None
    template = 'partiturasApp/borrar.html'
    
    if tipo_objeto == 'partitura':
        object = get_object_or_404(Partitura, pk=pk)
        redirect_url = 'lista_partituras'
    elif tipo_objeto == 'compositor':
        object = get_object_or_404(Compositor, pk=pk)
        redirect_url = 'lista_compositores'
    else:
        return HttpResponse('<h1>Hubo un fallo</h1>')
    
    if request.method == 'POST':
        object.delete()
        return redirect(redirect_url)
    else:
        context = {'objeto':object,'tipo_objeto':tipo_objeto}
        return render(request, template, context)
            
            
    