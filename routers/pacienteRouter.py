from fastapi import APIRouter, HTTPException
from models.models import PatientBase, Patient, PatientCreate
import uuid

router = APIRouter(prefix = "/patient", tags = ["Patients"])

patients_db: Patient = []

router.get(
        "/patient", 
        response_model = Patient, 
        summary = "Crear usuario de paciente",
        description = "Se agrega una nueva cuenta de paciente",
        tags = ["Patients"],
        responses = {
            201: {
                "Description" : "Usuario creado exitosamente"
            }
        }
    )
def create_patient(patient: PatientCreate):
    for p in patients_db:
        if p.documentID == patient.documentID:
            raise HTTPException(
                status_code = 404,
                detail = "Paciente existente"
            )
        
    patient_id = str(uuid.uuid4())
    patient_data = Patient(
        id = patient_id,
        name = patient.name,
        email = patient.email,
        ducumentID = patient.documentID,
        phoneNumber = patient.phoneNumber,
        password = patient.password
    )

    patients_db[patient_id] = patient_data.model_dump()
    return  patient_data
