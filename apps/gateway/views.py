from django.shortcuts import render
from utils.proxy import ProxyView
from constants import APPOINTMENT_SERVICE_URL, PATIENT_SERVICE_URL, DOCTOR_SERVICE_URL, INFRASTRUCTURE_SERVICE_URL
# Create your views here.



class AppointmentProxyView(ProxyView):
    def get(self, request, appointment_id=None):
        service_url = f"{APPOINTMENT_SERVICE_URL}{appointment_id}/" if appointment_id else APPOINTMENT_SERVICE_URL
        return self.proxy_request(request, service_url)

class PatientProxyView(ProxyView):
    def get(self, request, patient_id=None):
        service_url = f"{PATIENT_SERVICE_URL}{patient_id}/" if patient_id else PATIENT_SERVICE_URL
        return self.proxy_request(request, service_url)

class DoctorProxyView(ProxyView):
    def get(self, request, doctor_id=None):
        service_url = f"{DOCTOR_SERVICE_URL}{doctor_id}/" if doctor_id else DOCTOR_SERVICE_URL
        return self.proxy_request(request, service_url)
    
class InfrastructureProxyView(ProxyView):
    def get(self, request, infrastructure_id=None):
        service_url = f"{INFRASTRUCTURE_SERVICE_URL}{infrastructure_id}/" if infrastructure_id else INFRASTRUCTURE_SERVICE_URL
        return self.proxy_request(request, service_url)
