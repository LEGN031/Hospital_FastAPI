from fastapi import APIRouter, HTTPException
from models.models import Nurse

router = APIRouter(prefix="/enfermeras", tags=["Enfermeras"])

Nurses = [{
    "id": 1,
    "cedula": "1234567890",
    "nombre": "Ana Martinez",
    "email": "AnaMartinez@gmail.com",
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


@router.get("/", status_code=200, description="Obtener todos los Nurses")
async def getNurses():
    return Nurses

@router.get("/{Nurse_id}", status_code=200, description="Obtener un Nurse por su ID")
async def getNurse(Nurse_id: int):
    for i in Nurses:
        if i["id"] == Nurse_id:
            return i
    raise HTTPException(status_code=404, detail="Nurse not found")

@router.post("/", status_code=201, description="Crear un nuevo Nurse")
async def createNurse(Nurse : Nurse):
    for i in Nurses:
        if i["cedula"] == Nurse.cedula:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    if len(Nurses) > 0:
        Nurse.id = Nurses[-1]["id"] + 1
    else:
        Nurse.id = 1
    Nurses.append(Nurse.model_dump())
    return Nurse

@router.put("/{Nurse_id}", status_code=200, description="Actualizar un Nurse por su ID")
async def updateNurse(Nurse_id: int, Nurse: Nurse):
    found = False
    for i in Nurses:
        if i["id"] == Nurse_id:
            i["cedula"] = Nurse.cedula
            i["nombre"] = Nurse.nombre
            i["email"] = Nurse.email
            i["telefono"] = Nurse.telefono
            found = True
            return i
    if not found:
        raise HTTPException(status_code=404, detail="Nurse not found")
    return 

@router.delete("/{Nurse_id}", status_code=200, description="Eliminar un Nurse por su ID")
async def deleteNurse(Nurse_id: int):
    found = False
    for i in Nurses:
        if i["id"] == id:
            Nurses.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found') 
    return Nurses
