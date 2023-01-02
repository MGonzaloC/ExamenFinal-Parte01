from django.shortcuts import render, HttpResponse, redirect  



# Create your views here.

def inicio(request):   #saludo   
    return render( request,'inicio.html')

def integrantes(request):   #saludo   
    return render( request,'integrantes.html')

def crearcursos(request):   #saludo   
    return render( request,'crearcursos.html')

def crearproductos(request):   #saludo   
    return render( request,'crearproductos.html')


