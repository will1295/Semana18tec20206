from django.test import TestCase
from django.urls import reverse

class CarritoTests(TestCase):
    def test_agregar_producto_a_sesion(self):
        url = reverse("agregar",args=[1,"Teclado","25.00"])
        response = self.client.get(url)

        self.assertRedirects(response,reverse("ver_carrito"))
        self.assertEqual(self.client.session["carrito"]["1"]
                         ["cantidad"],1)