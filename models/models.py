from pydantic import BaseModel
from typing import Optional

class Medico(BaseModel):
    id: Optional[int] = None
    cedula: str
    nombre: str
    especialidad: str
    email: str
    telefono: str