from django.urls import path
from .views import AppointmentProxyView, PatientProxyView, DoctorProxyView, InfrastructureProxyView

urlpatterns = [
    path('appointments/', AppointmentProxyView.as_view(), name='appointments_proxy'),
    path('appointments/<int:appointment_id>/', AppointmentProxyView.as_view(), name='appointment_detail_proxy'),
    path('patients/', PatientProxyView.as_view(), name='patients_proxy'),
    path('patients/<int:patient_id>/', PatientProxyView.as_view(), name='patient_detail_proxy'),
    path('doctors/', DoctorProxyView.as_view(), name='doctors_proxy'),
    path('doctors/<int:doctor_id>/', DoctorProxyView.as_view(), name='doctor_detail_proxy'),
    path('infrastructure/', InfrastructureProxyView.as_view(), name='infrastructure_proxy'),
    path('infrastructure/<int:infrastructure_id>/', InfrastructureProxyView.as_view(), name='infrastructure_detail_proxy'),
]
