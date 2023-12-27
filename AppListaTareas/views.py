from django.shortcuts import render, redirect
from .models import Tarea

def listatareas(request):
    tareas = Tarea.objects.all()
    if request.method == 'POST':
        nueva_tarea=request.POST.get('nuevatarea')
        nueva_tarea1=Tarea(descripcion=nueva_tarea)
        nueva_tarea1.save()
        
    return render(request, 'listadetareas.html', {'tareas':tareas})

def eliminar(request, tarea_id):
    tarea=Tarea.objects.get(pk=tarea_id)
    if tarea:
        tarea.delete()
    return redirect('lista')