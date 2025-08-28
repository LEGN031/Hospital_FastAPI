from fastapi import APIRouter, HTTPException
from models.models import Medico

router = APIRouter(prefix="/medicos", tags=["Medicos"])

Medicos = [{
    "id": 1,
    "cedula": "1234567890",
    "nombre": "Dr. Juan Perez",
    "especialidad": "Cardiologia",
    "email": "JuanPerez@gmail.com",
    "telefono": "123456789"
},
{
    "id": 2,
    "cedula": "0987654321",
    "nombre": "Dra. Maria Gomez",
    "especialidad": "Neurologia",
    "email": "MariaGomez@gmail.com",
    "telefono": "987654321"
},
{
    "id": 3,
    "cedula": "4561237890",
    "nombre": "Dr. Carlos Ruiz",
    "especialidad": "Pediatria",
    "email": "CarlosRuiz@gmail.com",
    "telefono": "456123789"
}
]


@router.get("/", status_code=200)
async def getMedicos():
    return Medicos

@router.get("/{medico_id}", status_code=200)
async def getMedico(medico_id: int):
    for i in Medicos:
        if i["id"] == medico_id:
            return i
    raise HTTPException(status_code=404, detail="Medico not found")

@router.post("/", status_code=201)
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