from django.urls import path
from . import views
#DIA 13 - importando una clase como vista
from .views import *

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('mozart/', views.paginaMozart, name='autor_mozart'),
    path('contacto/',views.contacto, name='contacto'),
    path('total/',views.total_partituras, name='total_partituras'),
    path('partituras/', PartituraListView.as_view(), name='lista_partituras'),   #Creando una clase como vista.
    path('partituras/nueva/', PartituraCreate.as_view(), name='crear_partitura'),
    path('partituras/<int:pk>/', PartituraDetalle.as_view(), name='detalle_partitura'), #ya es una clase
    path('partitura/<int:pk>/editar', PartituraUpdateView.as_view(), name='editar_partitura'),
    path('partitura/<int:pk>/borrar/',PartituraDeleteView.as_view(), name='borrar_partitura'),
    path('compositor/<int:pk>/borrar/',CompositorDeleteView.as_view(), name='borrar_compositor'),    #lo edite, elimine las variables de la url
    path('compositores/', CompositorListView.as_view(), name='lista_compositores'), #clase Propia
    path('compositor/nuevo/',CompositorCreateView.as_view(), name='crear_compositor'),
    path('compositores/<int:pk>', CompositorDetalle.as_view(), name='detalle_compositor'),  #Clase propia
    path('compositor/<int:pk>/editar', CompositorUpdateView.as_view(), name='editar_compositor'),
    path('generos/', views.lista_generos, name='lista_generos'),
]