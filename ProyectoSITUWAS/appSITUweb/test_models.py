from django.test import TestCase

from appSITUweb.models import Pasajero

# Create your tests here.
class PasajeroModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Pasajero.objects.create(cedula='1104013188',nombre='Wilson', apellido='Sanchez',email='wasanchez@gmail.com')

    def test_cedula_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label = pasajero._meta.get_field('cedula').verbose_name
        self.assertEquals(field_label,'cedula')

    def test_nombre_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label = pasajero._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_apellido_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label = pasajero._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label,'apellido')

    def test_apellido_label(self):
        pasajero=Pasajero.objects.get(id=1)
        field_label = pasajero._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')

    def test_cedula_max_length(self):
        pasajero=Pasajero.objects.get(id=1)
        max_length = pasajero._meta.get_field('cedula').max_length
        self.assertEquals(max_length,10)
