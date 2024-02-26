import os
import django

# Reemplaza 'myproject.settings' con la ruta de tu archivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CitasMedicas.settings')
django.setup()

# En views.py

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import generics
from django.test import RequestFactory
from CitasMed.models import Usuario, PerfilAcceso, Reporte, MedicoPersonal, Paciente, ConsultaMedica, Facturacion, PlanCuentas, IntegracionContable, PrescripcionOrdenMedica, Certificado
from CitasMed.serializers import UsuarioSerializer, PerfilAccesoSerializer, ReporteSerializer, MedicoPersonalSerializer, PacienteSerializer, ConsultaMedicaSerializer, FacturacionSerializer, PlanCuentasSerializer, IntegracionContableSerializer, PrescripcionOrdenMedicaSerializer, CertificadoSerializer


#CRUD usuarios-----------------------------------------------------------------------------
class UsuarioListCreateView(generics.ListCreateAPIView):  
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# CRUD PerfilAccesoListCreateView-----------------------------------------------------------------------------
class PerfilAccesoListCreateView(generics.ListCreateAPIView):

    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer

class PerfilAccesoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer


# CRUD ReporteListCreateView-----------------------------------------------------------------------------
class ReporteListCreateView(generics.ListCreateAPIView):

    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


# CRUD MedicoPersonalListCreateView-----------------------------------------------------------------------------
class MedicoPersonalListCreateView(generics.ListCreateAPIView):

    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer


class MedicoPersonalDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MedicoPersonal.objects.all()
    serializer_class = MedicoPersonalSerializer


# CRUD PacienteListCreateView-----------------------------------------------------------------------------
class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


# CRUD ConsultaMedicaListCreateView-----------------------------------------------------------------------------
class ConsultaMedicaListCreateView(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class ConsultaMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer


# CRUD FacturacionListCreateView-----------------------------------------------------------------------------
class FacturacionListCreateView(generics.ListCreateAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

class FacturacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer


# CRUD PlanCuentasListCreateView-----------------------------------------------------------------------------
class PlanCuentasListCreateView(generics.ListCreateAPIView):

    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer


class PlanCuentasDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PlanCuentas.objects.all()
    serializer_class = PlanCuentasSerializer


# CRUD IntegracionContableListCreateView-----------------------------------------------------------------------------
class IntegracionContableListCreateView(generics.ListCreateAPIView):

    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer


class IntegracionContableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegracionContable.objects.all()
    serializer_class = IntegracionContableSerializer


# CRUD PrescripcionOrdenMedicaListCreateView-----------------------------------------------------------------------------
class PrescripcionOrdenMedicaListCreateView(generics.ListCreateAPIView):

    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer


class PrescripcionOrdenMedicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrescripcionOrdenMedica.objects.all()
    serializer_class = PrescripcionOrdenMedicaSerializer


# CRUD CertificadoListCreateView-----------------------------------------------------------------------------
class CertificadoListCreateView(generics.ListCreateAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer

class CertificadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer