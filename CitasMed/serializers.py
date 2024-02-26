from rest_framework import serializers
from .models import Usuario, PerfilAcceso, Reporte, MedicoPersonal, Paciente, ConsultaMedica, Facturacion, PlanCuentas, IntegracionContable, PrescripcionOrdenMedica, Certificado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PerfilAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilAcceso
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class MedicoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoPersonal
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__'

class PlanCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanCuentas
        fields = '__all__'

class IntegracionContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegracionContable
        fields = '__all__'

class PrescripcionOrdenMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescripcionOrdenMedica
        fields = '__all__'

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'
