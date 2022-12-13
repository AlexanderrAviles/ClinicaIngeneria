from django.db import models


class Rol(models.Model):
    tipo_usuario = models.IntegerField()


class Personal(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    mail = models.CharField(max_length=45)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)


class Sesion(models.Model):
    numero_sesion = models.IntegerField()
    objetivo_sesion = models.TextField(max_length=400)
    observacion = models.TextField(max_length=400)
    evolucion = models.TextField(max_length=600)
    alta_kinesiologica = models.CharField(max_length=255)


class Expediente(models.Model):
    habitos = models.CharField(max_length=255)
    alergias = models.CharField(max_length=255)
    cirugias = models.TextField(max_length=400)
    hospitalizaciones = models.CharField(max_length=255)
    antecedentes_morbidos = models.CharField(max_length=255)
    peso = models.FloatField()
    talla = models.FloatField()
    imc = models.FloatField()
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    so2 = models.IntegerField()
    presion_arterial = models.IntegerField()
    descripcion_dolor = models.TextField(max_length=600)
    
class Prevision(models.Model):
    nombre = models.CharField(max_length=15)
    
class Genero(models.Model):
    nombre =  models.CharField(max_length=15)


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    sexo = models.ForeignKey(Genero, on_delete= models.CASCADE)
    telefono = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    prevision = models.ForeignKey(Prevision, on_delete = models.CASCADE)
    diagnostico_medico = models.TextField(max_length=600)
    indicacion_medica = models.TextField(max_length=600)
    examenes = models.TextField(max_length=600,null=True)
    medicamentos = models.TextField(max_length=600,null=True)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE,null=True)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE,null=True)
    
class Cita(models.Model):
    fecha= models.DateTimeField()
    estado = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete = models.CASCADE)
    personal_rol = models.ForeignKey(Rol, on_delete = models.CASCADE)