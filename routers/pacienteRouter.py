from fastapi import APIRouter, HTTPException
from models.models import PatientBase, Patient, PatientCreate
from typing import List
import uuid

router = APIRouter(prefix = "/patient", tags = ["Patients"])

patients_db = []

@router.post(
    "/", 
    response_model = Patient, 
    summary = "Crear usuario de paciente",
    description = "Se agrega una nueva cuenta de paciente",
    tags = ["Patients"],
    responses = {
        201: {
            "Description" : "Usuario creado exitosamente"
        },
        400: {
            "descripcion": "Usuario ya existe"
        },
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
        documentID = patient.documentID,
        phoneNumber = patient.phoneNumber,
        password = patient.password
    )

    patients_db.append(patient_data)
    return  patient_data


@router.get(
    "/",
    response_model = List[Patient],
    summary = "Obtener lista de pacientes",
    description = "Se obtiene la lista de los pacientes",
    tags = ["Patients"],
    responses = {
        200: {
            "Description" : "Lista entregada correctamente"
        }
    }
)
def get_patients():
    patients = patients_db
    return patients

@router.get(
    "/{patient_id}",
    response_model = Patient,
    summary = "Obtener un paciente por id",
    description = "Se obtiene un paciente mediante su id",
    tags = ["Patients"],
    responses = {
            200: {
                "Description" : "paciente encontrado"
            },
            404: {
                "description" : "paciente no existe" 
            }
        }
    )
def get_patient(patient_id: str):
    for p in patients_db:
        if p.id == patient_id:
            return p
    
    raise HTTPException(
        status_code = 404,
        detail = "El paciente no existe"
    )
