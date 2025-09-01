from fastapi import APIRouter, HTTPException, status
from models.models import RegistroDiagnosticoCreate, Diagnostico, RegistroDiagnosticoUpdate
from routers.citaRouter import Citas
from typing import List
import uuid


router = APIRouter(prefix="/diagnostico", tags=["Diagnostico"])

Diagnosticos_db: List[Diagnostico] = []

#**Endpoint obtiene el diagnostico por tipo de diagnostico
@router.get(
    "/tipo", 
    response_model = RegistroDiagnosticoCreate, 
    summary = "Crear El resgistro del diagnostico de la cita",
    description = "Se crea el diagnostico obtenido durante la cita",
    tags = ["Diagnostico"],
    status_code = status.HTTP_201_CREATED,
)
async def get_diagnostico_by_type(tipo: str):
    for d in Diagnosticos_db:
        for t in d.diagnosticos:
            if t.Tipo.upper() == tipo.upper():
                return d
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No existe diagnostico con ese tipo"
    )

#**Endpoint crea diagnosticos para la db
@router.post(
    "/", 
    response_model = Diagnostico, 
    summary = "Crear El resgistro del diagnostico de la cita",
    description = "Se crea el diagnostico obtenido durante la cita",
    tags = ["Diagnostico"],
    status_code = status.HTTP_201_CREATED,
)
async def create_diagnostico(diagnostico: RegistroDiagnosticoCreate):
    for d in Diagnosticos_db:
        if diagnostico.cita_id == d.cita_id:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Ya existe diagnostico para esa cita"
            )

    for c in Citas: 
        if diagnostico.cita_id == c["cita_id"]:
            diagnostico_uuid = str(uuid.uuid4())

            diagnostico_data = Diagnostico(
                diagnostico_id = diagnostico_uuid,
                fecha = diagnostico.fecha,
                cita_id = diagnostico.cita_id,
                patient_id = diagnostico.patient_id,
                diagnosticos = diagnostico.diagnosticos,
                medico_id = diagnostico.medico_id
            )

            Diagnosticos_db.append(diagnostico_data)
            return diagnostico_data

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No existe la cita asignada al registro de diagnostico"
    )

#**Endpoint obtiene Todos los diagnosticos
@router.get(
    "/", 
    response_model = List[Diagnostico], 
    summary = "Obtiene todos los diagnosticos de la db",
    description = "Se obtiene los diagnosticos guardados en la db mediante paginacion",
    tags = ["Diagnostico"],
    status_code = status.HTTP_200_OK,
)
async def get_diagnosticos(skip: int = 0, limit: int = 10 ):
    diagnosticos = Diagnosticos_db
    return diagnosticos[skip: skip + limit]

#**Endpoint obtiene diagnostico por id 
@router.get(
    "/{diagnostico_id}", 
    response_model = Diagnostico, 
    summary = "Obtiene diganostico por id de diagnostico",
    description = "Se obtiene un diagnostico en especifico mediante ID",
    tags = ["Diagnostico"],
    status_code = status.HTTP_200_OK,
)
async def get_diagnostico(diagnostico_id: str):
    for d in Diagnosticos_db:
        if d.diagnostico_id == diagnostico_id:
            return d
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No existe diagnostico con esa ID"
    )

#**Endpoint actualiza los diagnosticos
@router.put(
    "/{diagnostico_id}", 
    response_model = Diagnostico, 
    summary = "Actualiza un diagnostico",
    description = "Se actualiza un diagnostico mediante su ID",
    tags = ["Diagnostico"],
    status_code = status.HTTP_201_CREATED,
)
async def update_diagnostico(update_diagnostico: RegistroDiagnosticoUpdate, diagnostico_id: str):
    for d in Diagnosticos_db:
        if d.diagnostico_id == diagnostico_id:
            
            if update_diagnostico.diagnosticos is not None:
                d.diagnosticos = update_diagnostico.diagnosticos
            if update_diagnostico.fecha is not None:
                d.fecha = update_diagnostico.fecha
            
            return d

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No existe diagnostico con esa ID"
    )

#**Endpoint elimina los diagnosticos mediante ID
@router.delete(
    "/{diagnostico_id}", 
    summary = "Elimina un diagnostico",
    description = "Se elimina un diagnostico mediante su ID",
    tags = ["Diagnostico"],
    status_code = status.HTTP_204_NO_CONTENT,
)
async def delete_diagnostico(diagnostico_id:str):
    for index, d in enumerate(Diagnosticos_db):
        if d.diagnostico_id == diagnostico_id:
            del Diagnosticos_db[index]
            return "Diagnostico eliminado"
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontro el diagnostico"
    )
    