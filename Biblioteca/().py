# coding: utf-8
from partiturasApp.models import Compositor, Partitura, Instrumento
Partitura.objects.all()
Compositor.objects.all()
autor1 = Compositor(nombre = 'chopin', apellido = ' selonski')
autor1
autor2 = Compositor(nombre = 'mozart',apellido='mozzila',pais='suecia')
autor2
autor1
autor1.pais
autor1.save()
autor2.save()
Compositor.objects.all()
Instrumento.objects.all()
piano = Instrumento(nombre='piano')
piano
piano.save()
clarinete = Instrumento(nombre='clarinete',familia='madera')
clarin
clarinete
clarinete.save()
partitura1 = Partitura(titulo = 'Sonata de david', Compositor = autor1, instrumento = piano, fecha_publicacion ='12/05/1867',genero = 'sonata)
partitura1 = Partitura(titulo = 'Sonata de david', Compositor = autor1, instrumento = piano, fecha_publicacion ='12/05/1867',genero = 'sonata')
partitura1 = Partitura(titulo = 'Sonata de david', compositor = autor1, instrumento = piano, fecha_publicacion ='12/05/1867',genero = 'sonata')
partiura1.save()
partitura1.save()
partitura1 = Partitura(titulo = 'Sonata de david', compositor = autor1, instrumento = piano, fecha_publicacion ='1967-05-12',genero = 'sonata')
partitura1.save()
partitura1
Parti
Partitura.objects.all()
bach = Compositor.objects.get(nombre='bach')
bach = Compositor.objects.get(__icontains='bach')
bach = Compositor.objects.get(nombre__icontains='bach')
bach = Compositor.objects.get(nombre__icontains or apellido__icontains='bach')
bach = Compositor.objects.get(apellido__icontains='bach')
bach
autor1
chopin = autor1
chopin
autor2
mozart = autor2
bach
chopin
mozart
mozart
chopin
bach
betoven
betoben
beto = Compositor.objects.get(id=4)
beto
beto = Compositor.objects.get(id=2)
beto
piano
piano.familia = 'armonico'
piano
piano.saave()
piano.save()
Instrumento.objects.get(id=1).fecha_publicacion = 1840-02-23
Partitura.objects.get(id=1).fecha_publicacion = 1840-02-23
Partitura.objects.get(id=1).fecha_publicacion = 1840-2-23
