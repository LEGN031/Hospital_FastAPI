from fastapi import APIRouter, HTTPException
from models.models import Factura
from routers.pacienteRouter import patients_db

router = APIRouter(prefix="/Factura", tags=["Factura"])

factura_db = [{
    "factura_id": 1,
    "fecha": "2024-12-27",
    "hora": "15:45",
    "medico_id": 1,
    "paciente_id": "777",
    "diagnostico": "Consulta general",
    "total": 1000123.0
}
]

@router.get("/patient", status_code=200, description="Obtener Factura por ID de paciente")
async def getFacturaByPatient(nombre: str):
    for c in factura_db:
        for p in patients_db:
            if p.name == nombre :
                return {"factura_id": c["factura_id"], "fecha": c["fecha"], "hora": c["hora"],"diagnostico": c["diagnostico"] , "total": c["total"],"medico_id": c["medico_id"], "paciente_id": p.patient_id, "patient_name": p.name}
    raise HTTPException(status_code=404, detail="Factura not found for the given patient name")

@router.get("/", status_code=200, description="Obtener todas las Factura")
async def getFactura():
    return factura_db

@router.get("/{factura_id}", status_code=200, description="Obtener una factura por su ID")
async def getfacturaByID(factura_id: int):
    for i in factura_db:
        if i["factura_id"] == factura_id:
            return i
    raise HTTPException(status_code=404, detail="factura not found")


@router.post("/", status_code=201, description="Crear una nueva factura")
async def createfactura(factura : Factura):
    found = False
    for i in factura_db:
        if i["factura_id"] == factura.factura_id:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    factura_db.append(factura.model_dump())
    return factura

@router.put("/{factura_id}", status_code=200, description="Actualizar una factura por su ID")
async def updatefactura(factura_id: int, factura: Factura):
    found = False
    for i in factura_db:
        if i["factura_id"] == factura_id:
            i["fecha"] = factura.fecha
            i["hora"] = factura.hora
            i["medico_id"] = factura.medico_id
            i["paciente_id"] = factura.patient_id
            i["diagnostico"] = factura.diagnostico
            i["total"] = factura.total
            found = True
            return i
    if not found:
        raise HTTPException(status_code=404, detail="factura not found")
    return

@router.delete("/{factura_id}", status_code=200, description="Eliminar una factura por su ID")
async def deletefactura(factura_id: int):
    found = False
    for i in factura_db:
        if i["factura_id"] == factura_id:
            factura_db.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="factura not found")
    return {"detail": "factura deleted"}

