from fastapi import APIRouter, HTTPException
from models.models import Cita
from routers.pacienteRouter import patients_db

router = APIRouter(prefix="/citas", tags=["Citas"])

Citas = [{
    "cita_id": 1,
    "fecha": "2023-10-01",
    "hora": "10:00",
    "medico_id": 1,
    "paciente_id": "12345678"
}
]

@router.get("/patient", status_code=200, description="Obtener citas por ID de paciente")
async def getCitasByPatient(nombre: str):
    for c in Citas:
        for p in patients_db:
            if p.name == nombre :
                return {"cita_id": c["cita_id"], "fecha": c["fecha"], "hora": c["hora"], "medico_id": c["medico_id"], "paciente_id": p.patient_id, "patient_name": p.name}
    raise HTTPException(status_code=404, detail="Citas not found for the given patient name")

@router.get("/", status_code=200, description="Obtener todas las citas")
async def getCitas():
    return Citas

@router.get("/{cita_id}", status_code=200, description="Obtener una cita por su ID")
async def getCitaByID(cita_id: int):
    for i in Citas:
        if i["cita_id"] == cita_id:
            return i
    raise HTTPException(status_code=404, detail="Cita not found")


@router.post("/", status_code=201, description="Crear una nueva cita")
async def createCita(cita : Cita):
    found = False
    for i in Citas:
        if i["cita_id"] == cita.cita_id:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    Citas.append(cita.model_dump())
    return cita

@router.put("/{cita_id}", status_code=200, description="Actualizar una cita por su ID")
async def updateCita(cita_id: int, cita: Cita):
    found = False
    for i in Citas:
        if i["cita_id"] == cita_id:
            i["fecha"] = cita.fecha
            i["hora"] = cita.hora
            i["medico_id"] = cita.medico_id
            i["paciente_id"] = cita.patient_id
            found = True
            return i
    if not found:
        raise HTTPException(status_code=404, detail="Cita not found")
    return

@router.delete("/{cita_id}", status_code=200, description="Eliminar una cita por su ID")
async def deleteCita(cita_id: int):
    found = False
    for i in Citas:
        if i["cita_id"] == cita_id:
            Citas.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="Cita not found")
    return {"detail": "Cita deleted"}

