from fastapi import APIRouter, HTTPException
from models.models import Nurse

router = APIRouter(prefix="/enfermeras", tags=["Enfermeras"])

Nurses = [{
    "id": 1,
    "cedula": "1234567890",
    "nombre": "Dr. Juan Perez",
    "email": "JuanPerez@gmail.com",
    "telefono": "189278"
},
{
    "id": 2,
    "cedula": "0987654321",
    "nombre": "Margarita BuenaVista",
    "email": "MargaritaB@gmail.com",
    "telefono": "12821901"
},
{
    "id": 3,
    "cedula": "4561237890",
    "nombre": "Luciana Hernandez",
    "email": "LuciH@gmail.com",
    "telefono": "2198121"
}
]


@router.get("/", status_code=200, description="Obtener todos los medicos")
async def getMedicos():
    return Medicos

@router.get("/{medico_id}", status_code=200, description="Obtener un medico por su ID")
async def getMedico(medico_id: int):
    for i in Medicos:
        if i["id"] == medico_id:
            return i
    raise HTTPException(status_code=404, detail="Medico not found")

@router.post("/", status_code=201, description="Crear un nuevo medico")
async def createMovie(medico : Medico):
    for i in Medicos:
        if i["cedula"] == medico.cedula:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    if len(Medicos) > 0:
        medico.id = Medicos[-1]["id"] + 1
    else:
        medico.id = 1
    Medicos.append(medico.model_dump())
    return medico

@router.put("/{medico_id}", status_code=200, description="Actualizar un medico por su ID")
async def updateMedico(medico_id: int, medico: Medico):
    found = False
    for i in Medicos:
        if i["id"] == medico_id:
            i["cedula"] = medico.cedula
            i["nombre"] = medico.nombre
            i["especialidad"] = medico.especialidad
            i["email"] = medico.email
            i["telefono"] = medico.telefono
            found = True
            return i
    if not found:
        raise HTTPException(status_code=404, detail="Medico not found")
    return 

@router.delete("/{medico_id}", status_code=200, description="Eliminar un medico por su ID")
async def deleteMedico(medico_id: int):
    found = False
    for i in Medicos:
        if i["id"] == id:
            Medicos.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found') 
    return Medicos
