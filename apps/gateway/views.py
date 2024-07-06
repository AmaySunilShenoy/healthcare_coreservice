from django.shortcuts import render
from utils.proxy import ProxyView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from service_registrar.mixins import ServiceAddressMixin
from django.http import HttpResponse

# Create your views here.



class AppointmentProxyView(ServiceAddressMixin, ProxyView):
    def dispatch(self, request, appointment_id=None):
        try:
            # self.get_service_address('appointments')
            if not self.url:
                self.url = 'http://localhost:8001/api/appointments/'

            if appointment_id:
                self.url = f'{self.url}{appointment_id}/'
            return self.proxy_request(request)
        except Exception as e:
            return self.response_from_exception(e)

class PatientProxyView(ServiceAddressMixin, ProxyView):
    def dispatch(self, request, patient_id=None):
        try:
            self.get_service_address('patients')
            if patient_id:
                self.url = f'{self.url}/{patient_id}/'
            return self.proxy_request(request)
        except Exception as e:
            return self.response_from_exception(e)
        
class DoctorProxyView(ServiceAddressMixin, ProxyView):
    def dispatch(self, request, doctor_id=None):
        try:
            self.get_service_address('doctors')
            if doctor_id:
                self.url = f'{self.url}/{doctor_id}/'
            return self.proxy_request(request)
        except Exception as e:
           return self.response_from_exception(e)
        
class InfrastructureProxyView(ServiceAddressMixin, ProxyView):
    def dispatch(self, request, infrastructure_id=None):
        try:
            self.get_service_address('infrastructure')
            if infrastructure_id:
                self.url = f'{self.url}/{infrastructure_id}/'
            return self.proxy_request(request)
        except Exception as e:
           return self.response_from_exception(e)

