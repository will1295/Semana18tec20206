from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio_view,name="inicio"),
    path("login/",views.login_view,name="login"),
    path("registro/",views.registro_view,name="registro"),
    path("logout/",views.logout_view,name="logout"),
    path("carrito/",views.ver_carrito,name="ver_carrito"),
    path("carrito/agregar/<int:id>/<str:nombre>/<str:precio>/",
         views.agregar,name="agregar"),
    path("carrito/vaciar/",views.vaciar,name="vaciar"),
]