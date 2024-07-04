import requests
from constants import PATIENT_SERVICE_URL, DOCTOR_SERVICE_URL


def get_doctor_data(doctor_id):
    response = requests.get(f"{DOCTOR_SERVICE_URL}{doctor_id}/")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_patient_data(patient_id):
    response = requests.get(f"{PATIENT_SERVICE_URL}{patient_id}/")
    if response.status_code == 200:
        return response.json()
    else:
        return None
