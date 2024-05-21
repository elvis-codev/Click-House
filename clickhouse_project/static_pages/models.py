from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # Agrega el campo id como una clave primaria automática
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    TIPO_USUARIO_CHOICES = [
        ('arrendador', 'Arrendador'),
        ('arrendatario', 'Arrendatario'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.id} - {self.nombres} {self.apellidos}"

class Propiedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=50)
    TIPO_INMUEBLE_CHOICES = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela'),
    ]
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ["nombre"]

class Arrendatario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    propiedades_interes = models.ManyToManyField(Propiedad)

    class Meta:
        verbose_name = "Arrendatario"
        verbose_name_plural = "Arrendatarios"
        ordering = ["usuario"]

class Arrendador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    propiedades_publicadas = models.ManyToManyField(Propiedad)

    class Meta:
        verbose_name = "Arrendador"
        verbose_name_plural = "Arrendadores"
        ordering = ["usuario"]
