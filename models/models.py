from pydantic import BaseModel, Field
from typing import Optional

class Medico(BaseModel):
    id: Optional[int] = None
    cedula: str
    nombre: str
    especialidad: str
    email: str
    telefono: str
    
class PatientBase(BaseModel): 
    name: str = Field(..., min_lenght = 3, description = "nombre del paciente")
    email: str = Field(..., min_length = 10, description = "Correo del paciente")
    documentID: str = Field(..., description = "Numero de documento de identificacion del paciente")
    phoneNumber: str = Field(..., description = "Numero de contacto del paciente")

class PatientUpdate(BaseModel): 
    name: str = Field(None, min_lenght = 3, description = "nombre del paciente")
    email: str = Field(None, min_length = 10, description = "Correo del paciente")
    documentID: str = Field(None, description = "Numero de documento de identificacion del paciente")
    phoneNumber: str = Field(None, description = "Numero de contacto del paciente")

class PatientCreate(PatientBase):
    password: str = Field(..., description = "Contraseña del paciente")

class Patient(PatientBase):
    id: str 
