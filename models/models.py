from pydantic import BaseModel, Field
from typing import Optional

class Medico(BaseModel):
    id: Optional[int] = None
    name: str
    especialidad: str
    email: str
    telefone: str

class PacienteBase(BaseModel): 
    name: str = Field(..., min_lenght = 3)
