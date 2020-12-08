from django.shortcuts import render, redirect
from .models import Denuncia
from .forms import DenunciaForm

def list_denuncias(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncias.html', {'denuncias': denuncias})

def create_denuncias(request):
    form = DenunciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_denuncias')
    return render(request, 'denuncias-form.html', {'form':form})

def update_denuncias (request, id):
    denuncias = Denuncia.objects.get(id=id)
    form = DenunciaForm(request.POST or None, instance=denuncias)

    if form.is_valid():
        form.save()
        return redirect('list_denuncias')

    return render (request, 'denuncias-form.html', {'form': form, 'denuncias':denuncias})

def delete_denuncias(request, id):
    denuncias = Denuncia.objects.get(id=id)
    if request.method == 'POST':
        denuncias.delete()
        return redirect('list_denuncias')
    return render(request, 'denuncias-delete.html',{'denuncias':denuncias})
