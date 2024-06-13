from pydantic import BaseModel

class UserRequestModel(BaseModel):
    nombre: str
    password: str
    
class UserResponseModel(UserRequestModel):
    nombre: str
    
class ClienteRequestModel(BaseModel):
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    
    class Config:
        orm_mode = True

class ClienteResponseModel(BaseModel):
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    
    class Config:
        orm_mode = True
        from_attributes = True 
    

class AutoRequestModel(BaseModel):
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    
    class Config:
        orm_mode = True

class AutoResponseModel(BaseModel):
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int

class FacturaRequestModel(BaseModel):
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    fecha: str
    hora: str
    
    class Config:
        orm_mode = True

class FacturaResponseModel(BaseModel):
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    fecha: str
    hora: str


