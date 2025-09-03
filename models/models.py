from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Medico(BaseModel):
    medico_id: Optional[int] = None
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
    patient_id: str 
     

class Nurse (BaseModel):
    nurse_id: Optional[int] = None
    cedula: str
    nombre: str
    email: str
    telefono: str

class Cita(BaseModel):
    cita_id: Optional[int] = None
    patient_id: str
    medico_id: int
    fecha: str
    hora: str
class ListaDiagnostico(BaseModel):
    Tipo: str
    descripcion: str

class RegistroDiagnosticoCreate(BaseModel):
    diagnosticos: List[ListaDiagnostico] = Field(..., description = "Lista de diagnosticos encontrados durante la cita")
    fecha: datetime = Field(..., description = "Fecha del registro del diagnostico")
    cita_id: int = Field(..., description = "Id de la cita del paciente")
    medico_id: str = Field(..., description = "Id Medico que atendio la cita")
    patient_id: str = Field(..., description = "Id del paciente deuño de la cita")

class RegistroDiagnosticoUpdate(BaseModel):
    diagnosticos: List[ListaDiagnostico] = Field(None, description = "Lista de diagnosticos encontrados durante la cita")
    fecha: datetime = Field(None, description = "Fecha del registro del diagnostico")

class Diagnostico(RegistroDiagnosticoCreate):
    diagnostico_id: str = Field(..., description = "Id de la cita del paciente")
class Factura(BaseModel):
    factura_id: Optional[int] = None
    fecha: str
    hora: str
    medico_id: int
    patient_id: str
    diagnostico: str
    total: float