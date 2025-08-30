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


@router.get("/buscar", status_code=200, description="Buscar medicos por especialidad")
def getMedicosByEspecialidad(especialidad: str):
    resultados = [m for m in Medicos if m["especialidad"].lower() == especialidad.lower()]
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron medicos con esa especialidad")
    return resultados

@router.get("/", status_code=200, description="Obtener todos los medicos")
async def getMedicos():
    return Medicos

@router.get("/{medico_id}", status_code=200, description="Obtener un medico por su ID")
async def getMedicoByID(medico_id: int):
    for i in Medicos:
        if i["medico_id"] == medico_id:
            return i
    raise HTTPException(status_code=404, detail="Medico not found")

@router.post("/", status_code=201, description="Crear un nuevo medico")
async def createMovie(medico : Medico):
    found = False
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
        if i["medico_id"] == medico_id:
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
        if i["medico_id"] == medico_id:
            Medicos.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found') 
    return Medicos

