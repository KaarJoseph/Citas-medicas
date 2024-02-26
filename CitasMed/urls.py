# En urls.py
from django.urls import path
from .views import (
    UsuarioListCreateView,
    UsuarioDetailView,
    PerfilAccesoListCreateView,
    PerfilAccesoDetailView,
    ReporteListCreateView,
    ReporteDetailView,
    MedicoPersonalListCreateView,
    MedicoPersonalDetailView,
    PacienteListCreateView,
    PacienteDetailView,
    ConsultaMedicaListCreateView,
    ConsultaMedicaDetailView,
    FacturacionListCreateView,
    FacturacionDetailView,
    PlanCuentasListCreateView,
    PlanCuentasDetailView,
    IntegracionContableListCreateView,
    IntegracionContableDetailView,
    PrescripcionOrdenMedicaListCreateView,
    PrescripcionOrdenMedicaDetailView,
    CertificadoListCreateView,
    CertificadoDetailView,
)

urlpatterns = [
    # Rutas para el modelo Usuario
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # Rutas para el modelo PerfilAcceso
    path('perfilacceso/', PerfilAccesoListCreateView.as_view(), name='perfilacceso-list-create'),
    path('perfilacceso/<int:pk>/', PerfilAccesoDetailView.as_view(), name='perfilacceso-detail'),

    # Rutas para el modelo Reporte
    path('reporte/', ReporteListCreateView.as_view(), name='reporte-list-create'),
    path('reporte/<int:pk>/', ReporteDetailView.as_view(), name='reporte-detail'),

    # Rutas para el modelo MedicoPersonal
    path('medicopersonal/', MedicoPersonalListCreateView.as_view(), name='medicopersonal-list-create'),
    path('medicopersonal/<int:pk>/', MedicoPersonalDetailView.as_view(), name='medicopersonal-detail'),

    # Rutas para el modelo Paciente
    path('paciente/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),

    # Rutas para el modelo ConsultaMedica
    path('consultamedica/', ConsultaMedicaListCreateView.as_view(), name='consultamedica-list-create'),
    path('consultamedica/<int:pk>/', ConsultaMedicaDetailView.as_view(), name='consultamedica-detail'),

    # Rutas para el modelo Facturacion
    path('facturacion/', FacturacionListCreateView.as_view(), name='facturacion-list-create'),
    path('facturacion/<int:pk>/', FacturacionDetailView.as_view(), name='facturacion-detail'),

    # Rutas para el modelo PlanCuentas
    path('plancuentas/', PlanCuentasListCreateView.as_view(), name='plancuentas-list-create'),
    path('plancuentas/<int:pk>/', PlanCuentasDetailView.as_view(), name='plancuentas-detail'),

    # Rutas para el modelo IntegracionContable
    path('integracioncontable/', IntegracionContableListCreateView.as_view(), name='integracioncontable-list-create'),
    path('integracioncontable/<int:pk>/', IntegracionContableDetailView.as_view(), name='integracioncontable-detail'),

    # Rutas para el modelo PrescripcionOrdenMedica
    path('prescripcionordenmedica/', PrescripcionOrdenMedicaListCreateView.as_view(), name='prescripcionordenmedica-list-create'),
    path('prescripcionordenmedica/<int:pk>/', PrescripcionOrdenMedicaDetailView.as_view(), name='prescripcionordenmedica-detail'),

    # Rutas para el modelo Certificado
    path('certificado/', CertificadoListCreateView.as_view(), name='certificado-list-create'),
    path('certificado/<int:pk>/', CertificadoDetailView.as_view(), name='certificado-detail'),
]
