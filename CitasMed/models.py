from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    usu_cedula = models.CharField(max_length=20, unique=True)
    usu_nombre_completo = models.CharField(max_length=255)
    usu_numero_telefono = models.CharField(max_length=20)
    usu_correo_electronico = models.TextField()
    usu_direccion = models.TextField()

class PerfilAcceso(models.Model):
    perf_acc_nivel_acceso = models.CharField(max_length=50)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Reporte(models.Model):
    rep_tipo_reporte = models.CharField(max_length=100)
    rep_parametros = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class MedicoPersonal(models.Model):
    med_per_nombre_completo = models.CharField(max_length=255)
    med_per_credenciales = models.TextField()
    med_per_especialidades = models.TextField()
    med_per_horarios_consulta = models.TextField()
    med_per_informacion_contacto = models.TextField()
    reportes = models.ForeignKey(Reporte, on_delete=models.CASCADE, null=True, blank=True)

class Paciente(models.Model):
    pac_nombre_completo = models.CharField(max_length=255)
    pac_fecha_nacimiento = models.CharField(max_length=255)
    pac_genero = models.CharField(max_length=50)
    pac_direccion = models.TextField()
    pac_numero_telefono = models.CharField(max_length=20)
    pac_correo_electronico = models.EmailField(unique=True)
    pac_antecedentes_medicos = models.TextField(blank=True)
    pac_enfermedades = models.TextField(blank=True)
    pac_alergias = models.TextField(blank=True)
    pac_medicamentos_actuales = models.TextField(blank=True)
    medico_personal = models.ForeignKey(MedicoPersonal, on_delete=models.CASCADE)

class ConsultaMedica(models.Model):
    con_med_medico_personal = models.ForeignKey(MedicoPersonal, on_delete=models.CASCADE)
    con_med_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    con_med_diagnostico = models.TextField()
    con_med_recomendaciones = models.TextField()

class Facturacion(models.Model):
    fact_nombre_paciente = models.CharField(max_length=255)
    fact_numero_identificacion = models.CharField(max_length=20)
    fact_numero_poliza_seguro = models.CharField(max_length=20)
    fact_detalles_facturacion = models.TextField()
    fact_estado_pago = models.CharField(max_length=100)
    fact_metodo_pago = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class PlanCuentas(models.Model):
    plan_cue_fecha_transaccion =  models.CharField(max_length=255)
    plan_cue_tipo_transaccion = models.CharField(max_length=100)
    plan_cue_monto = models.DecimalField(max_digits=10, decimal_places=2)
    plan_cue_descripcion = models.TextField()
    plan_cue_numero_referencia = models.CharField(max_length=100)
    plan_cue_cuenta_destino = models.CharField(max_length=100)
    plan_cue_metodo_pago = models.CharField(max_length=100)
    plan_cue_categoria_gasto_ingreso = models.CharField(max_length=100)
    plan_cue_datos_proveedor_cliente = models.TextField()
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)

class IntegracionContable(models.Model):
    integ_cont_datos_financieros = models.TextField()
    plan_cuentas = models.ForeignKey(PlanCuentas, on_delete=models.CASCADE)

class PrescripcionOrdenMedica(models.Model):
    pres_ord_nombre_paciente = models.CharField(max_length=255)
    pres_ord_fecha_emision = models.DateField(default=timezone.now)
    pres_ord_detalles_prescripcion = models.TextField()
    pres_ord_estado_cumplimiento = models.CharField(max_length=100)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)

class Certificado(models.Model):
    cert_titulo = models.CharField(max_length=255)
    cert_emisor = models.CharField(max_length=255)
    cert_receptor = models.CharField(max_length=255)
    cert_fecha_emision =  models.CharField(max_length=255)
    cert_descripcion = models.TextField()