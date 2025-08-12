from django.contrib import admin
from .models import Partitura, Compositor, Instrumento, Genero


# Register your models here.
#Los admin.site.register() se usan para registrar los modelos para mostrarlos en la web

#admin.site.register(Compositor)
#admin.site.register(Instrumento)
#admin.site.register(Partitura)


#Personalizando para mostrar diferentes categorias segun las propiedades de la clase.
class CompositorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'pais', 'fecha_de_nacimiento','numero_partituras')    #es una tupla que se usa para mostrar columnas de las propiedades en el objeto.

    list_filter = ('pais',)     #se usa para crear un orderby, es efectivo en propiedad que se comparten no en nombres o apellidos, crea filtros a la derecha.po
    
    search_fields = ('nombre', 'apellido')  #agg barra de busqueda que funciona por nombre o apellido en la parte superior.
    
    fieldsets = [('Informacion personal',{'fields': ['nombre', 'apellido','pais']}),
                 ('Fechas',{'fields':['fecha_de_nacimiento'],'classes':['collapse']}),
                 ]  #mas complicado, pero modifica el panel de creacion y modificacion de la web admin. su sintaxis es
                    #una lista [('nombreDeApartado', {'fields':['listaDeElementosaRecibir']}), etc] - se abre lista y una tupla con la informacion contenida, fields son los campos.
                    #'classes':['collapse'] hace que el grupo aparezca contraido por defecto, para informacion secundaria o no necesaria
    
      

    
    #Esta funcion devuelve el numero de partituras que tiene la clase Compositor, usa la propiedad related_name en foreignkey
    def numero_partituras(self,obj):    #obtiene un obj que es de la misma clase
        return obj.partituras.count()   #devuelve el obj.related_name.count() que es la funcion de cuenta de el query set
                    


admin.site.register(Compositor, CompositorAdmin)    # aca se registra en la web, se usa la clase original y la nuevaClase que la modifica.

class PartituraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'compositor', 'genero', 'instrumento')
    search_fields = ('nombre', 'genero','compositor__apellido') #se puede usar __propiedad para buscar en este caso en el apellido de compositor, la foreignkey
    list_filter = ('compositor','instrumento','genero')
    fieldsets = [('Informacion Principal',{'fields':['nombre','compositor','genero','instrumento']}),
                 ('Detalles de Publicacion',{'fields': ['fecha_creacion_partitura','editorial','fecha_publicacion','numero_opus','fecha_ingreso'],'classes':['collapse']})]

    readonly_fields = ('fecha_ingreso',)    #Esta propiedad hace que no se pueda editar.
    date_hierarchy =('fecha_publicacion')

admin.site.register(Partitura,PartituraAdmin)


class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre','familia']
    search_fields = ['nombre']
    
    list_filter = ['familia']
    
    
admin.site.register(Instrumento,InstrumentoAdmin)



# Dia 4 - reto - creando la clase para administrar en la DB y registrandola.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'epoca_principal')
    search_fields = ('nombre',)
    list_filter = ('epoca_principal',)
    
admin.site.register(Genero, GeneroAdmin)













