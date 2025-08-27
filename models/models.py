from pydantic import BaseModel
from typing import Optional

class Medico(BaseModel):
    id: Optional[int] = None
    name: str
    especialidad: str
    email: str
    telefone: str