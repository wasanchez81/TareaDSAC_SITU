from django.shortcuts import render
from .forms import PasajeroFormulario
from .forms import TarjetaFormulario
from .models import Pasajero
from .models import Tarjeta
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    data = {
        'form' : PasajeroFormulario(instance=pasajeros)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request,'pasajerosEdit.html',data)

def tarjetas(request):
    data = TarjetaFormulario()
    tarjetas = Tarjeta.objects.all()
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, Files=request.FILES)
        if formulario.is_valid():
            formulario.save()
    
    return render(request,"tarjetas.html",{"tarjetas":tarjetas, 'form':data})
