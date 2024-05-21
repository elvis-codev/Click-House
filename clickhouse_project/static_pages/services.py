from .models import Usuario, Propiedad, Arrendatario, Arrendador

def crear_usuario(nombres, apellidos, rut, direccion, telefono, correo, tipo_usuario):
    return Usuario.objects.create(nombres=nombres, apellidos=apellidos, rut=rut, direccion=direccion, telefono=telefono, correo=correo, tipo_usuario=tipo_usuario)

def listar_propiedades_por_comuna(comuna):
    return Propiedad.objects.filter(comuna=comuna)

def generar_solicitud_arriendo(arrendatario_id, propiedad_id):
    arrendatario = Arrendatario.objects.get(id=arrendatario_id)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    arrendatario.propiedades_interes.add(propiedad)

def publicar_propiedad(arrendador_id, nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    arrendador = Arrendador.objects.get(id=arrendador_id)
    propiedad = Propiedad.objects.create(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, estacionamientos=estacionamientos, habitaciones=habitaciones, banos=banos, direccion=direccion, comuna=comuna, tipo_inmueble=tipo_inmueble, precio_arriendo=precio_arriendo)
    arrendador.propiedades_publicadas.add(propiedad)

def eliminar_propiedad(arrendador_id, propiedad_id):
    arrendador = Arrendador.objects.get(id=arrendador_id)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    arrendador.propiedades_publicadas.remove(propiedad)
    propiedad.delete()

def editar_propiedad(propiedad_id, nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    propiedad = Propiedad.objects.get(id=propiedad_id)
    propiedad.nombre = nombre
    propiedad.descripcion = descripcion
    propiedad.m2_construidos = m2_construidos
    propiedad.m2_totales = m2_totales
    propiedad.estacionamientos = estacionamientos
    propiedad.habitaciones = habitaciones
    propiedad.banos = banos
    propiedad.direccion = direccion
    propiedad.comuna = comuna
    propiedad.tipo_inmueble = tipo_inmueble
    propiedad.precio_arriendo = precio_arriendo
    propiedad.save()