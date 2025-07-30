from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('mozart/', views.paginaMozart, name='autor_mozart'),
    path('contacto/',views.contacto, name='contacto'),
    path('total/',views.total_partituras, name='total_partituras'),
    path('partituras/', views.lista_partituras, name='lista_partituras'),
    path('partituras/nueva/', views.crear_partitura, name='crear_partitura'),
    path('compositores/', views.lista_compositores, name='lista_compositores'),
    path('compositor/nuevo/',views.crear_compositor, name='crear_compositor'),
    path('generos/', views.lista_generos, name='lista_generos'),
    path('compositores/<int:pk>', views.detalle_compositor, name='detalle_compositor'),
    path('<int:pk>/', views.detalle_partitura, name='detalle_partitura'),
]