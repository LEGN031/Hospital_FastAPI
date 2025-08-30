from fastapi import APIRouter, HTTPException, status
from models.models import Patient, PatientCreate, PatientUpdate
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
    status_code = status.HTTP_201_CREATED,
)
async def create_patient(patient: PatientCreate) -> Patient:
    for p in patients_db:
        if p.documentID == patient.documentID:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Paciente existente"
            )
        
    Patient_id = str(uuid.uuid4())
    patient_data = Patient(
        patient_id = Patient_id,
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
    status_code = status.HTTP_200_OK
)
async def get_patients(skip: int = 0, limit: int = 15) -> List[Patient]:
    patients = patients_db
    return patients[skip: skip + limit]

@router.get(
    "/{patient_id}",
    response_model = Patient,
    summary = "Obtener un paciente por id",
    description = "Se obtiene un paciente mediante su id",
    tags = ["Patients"],
    status_code = status.HTTP_200_OK
    )
async def get_patient(Patient_id: str) -> Patient:

    for p in patients_db:
        if p.patient_id == Patient_id:
            return p
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "El paciente no existe"
    )

@router.put(
    "/{patient_id}",
    response_model = Patient,
    summary = "Actualiza un paciente por id",
    description = "Se actualizan los datos de un paciente buscado mediante el id",
    tags = ["Patients"],
    status_code = status.HTTP_201_CREATED
)
async def update_patient(patient_id: str, patient_update: PatientUpdate) -> Patient:
    for patient in patients_db:
        if patient.patient_id == patient_id:            
            
            if patient_update.name is not None:
                patient.name = patient_update.name
            if patient_update.email is not None:
                patient.email = patient_update.email
            if patient_update.documentID is not None:
                patient.documentID = patient_update.documentID
            if patient_update.phoneNumber is not None:
                patient.phoneNumber = patient_update.phoneNumber

            return patient
        
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No existe el paciente"
        )

@router.delete(
    "/{patient_id}",
    summary = "Elimina un paciente por id",
    description = "Se Eliminara el paciente de la base de datos mediante el id",
    tags = ["Patients"],
    status_code = status.HTTP_204_NO_CONTENT
)
async def delete_patient(patient_id: str):
    for index, p in enumerate(patients_db):
        if p.patient_id == patient_id:
            del patients_db[index]
            return "Paciente eliminado"
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontro el paciente"
    )
    