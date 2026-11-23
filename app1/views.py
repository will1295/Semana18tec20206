from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


def registro_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("inicio")
    else:
        form = UserCreationForm()
    return render(request,"registro.html",{"form":form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            next_url = request.POST.get("next") or request.GET.get("next")
            return redirect(next_url or "inicio")
    else:
        form = AuthenticationForm(request)
    return render(request,"login.html",{"form":form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def inicio_view(request):
    return render(request,"inicio.html",{"usuario":request.user})



def ver_carrito(request):
    carrito = request.session.get("carrito",{})
    total = 0

    for producto in carrito.values():
        total += producto["precio"]*producto["cantidad"]
    return render(request,"carrito.html",{"carrito":carrito,"total":total})

def agregar(request,id,nombre,precio):
    carrito = request.session.get("carrito",{})
    key = str(id)

    if key in carrito:
        carrito[key]["cantidad"] +=1
    else:
        carrito[key] = {"nombre":nombre,"precio":float(precio)
                        ,"cantidad":1}
    request.session["carrito"] = carrito
    return redirect("ver_carrito")

def vaciar(request):
    request.session.pop("carrito",None)
    return redirect("ver_carrito")