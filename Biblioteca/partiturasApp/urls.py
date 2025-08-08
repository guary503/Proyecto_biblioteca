from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('mozart/', views.paginaMozart, name='autor_mozart'),
    path('contacto/',views.contacto, name='contacto'),
    path('total/',views.total_partituras, name='total_partituras'),
    path('partituras/', views.lista_partituras, name='lista_partituras'),
    path('partituras/nueva/', views.crear_partitura, name='crear_partitura'),
    path('partituras/<int:pk>/', views.detalle_partitura, name='detalle_partitura'),
    path('partitura/<int:pk>/editar', views.actualizar_partitura, name='editar_partitura'),
    path('borrar/<int:pk>/<str:tipo_objeto>/',views.borrar_objeto, name='borrar_objeto'),
    path('compositores/', views.lista_compositores, name='lista_compositores'),
    path('compositor/nuevo/',views.crear_compositor, name='crear_compositor'),
    path('compositores/<int:pk>', views.detalle_compositor, name='detalle_compositor'),
    path('compositor/<int:pk>/editar', views.actualizar_compositor, name='editar_compositor'),
    path('generos/', views.lista_generos, name='lista_generos'),
]