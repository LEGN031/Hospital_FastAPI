# Sistema para hospital.

## **1. Información General**
- **Nombre del Proyecto**: Sistema Hospitalario
- **Versión del Sistema**: 1.0.0
- **Fecha de Creación**: 08/2025
- **Autor(es)**: Emanuel Medina Arboleda, Samuel Ortiz Bermudez, Julián Garcia Guevara
- **Propósito**: Proporcionar información técnica detallada sobre la instalación, configuración, funcionamiento y mantenimiento de la API REST desarrollada en FastAPI para la gestión hospitalaria.

---

## **2. Introducción**
### **2.1 Descripción del Sistema**
El sistema es una API RESTful desarrollada en FastAPI que permite la gestión de información hospitalaria. Maneja recursos como:
- Pacientes
- Médicos
- Enfermeras
- Citas médicas
- Facturas
- Registros de diagnósticos
Su propósito es centralizar y simplificar las operaciones del hospital, facilitando el acceso y administración de datos médicos.

### **2.2 Alcance**
El manual cubre:
- Instalación y configuración del sistema.
- Requisitos de hardware y software.
- Arquitectura y componentes principales.
- Operación del sistema y flujos de trabajo.
 
---

## **3. Requisitos del Sistema**
### **3.1 Requisitos de Hardware**
- Procesador: 2 núcleos mínimos.
- Memoria RAM: 2 GB mínimo.
- Espacio en Disco: 200 MB.
- Otros: Conexión a internet para instalar dependencias.

### **3.2 Requisitos de Software**
- Sistema Operativo: Windows, Linux o macOS.
- Lenguaje: Python 3.9 o superior.
- Frameworks: FastAPI, Uvicorn.
- Librerías: Pydantic, Typing.
- Otros: Git (opcional).

---

## **4. Instalación**
### **4.1 Descarga de Archivos**
git clone <URL_DEL_REPOSITORIO>

### **4.2 Instalación Paso a Paso**
1. Instalar dependencias: pip install -r requirements.txt
2. Ejecutar servidor: uvicorn main:app --reload

### **4.3 Configuración Inicial**
- El sistema no requiere configuración adicional de base de datos.
- Acceder a la documentación interactiva en:
  http://127.0.0.1:8000/docs (Swagger UI).
  http://127.0.0.1:8000/redoc (Redoc).

---

## **5. Arquitectura del Sistema**
### **5.1 Diagrama de Arquitectura**
 main.py ───► routers/
                ├── pacienteRouter.py
                ├── medicoRouter.py
                ├── enfermeraRouter.py
                ├── citaRouter.py
                ├── facturaRouter.py
                └── registroDiagnosticoRouter.py
           └── models/
                └── models.py
                

### **5.2 Componentes Principales**
- **main.py**: Punto de entrada de la aplicación.
- **routers/**: Contiene los endpoints organizados por entidad.
- **models/**: Define los modelos de datos (usando Pydantic).

---

## **6. Operación del Sistema**
### **6.1 Descripción General**
El sistema funciona como un servidor REST que permite realizar operaciones CRUD sobre entidades hospitalarias. Cada recurso tiene sus rutas específicas bajo el esquema:
-  /pacientes/ → Gestión de pacientes.
-  /medicos/ → Gestión de médicos.
-  /enfermeras/ → Gestión de enfermeras.
-  /citas/ → Gestión de citas.
-  /facturas/ → Gestión de facturas.
-  /diagnosticos/ → Registro de diagnósticos.

### **6.2 Flujos de Trabajo Principales**
1. **Gestión de Pacientes/Medicos/Enfermeras**:
-  Crear un paciente/medicos/enfermeras → POST (/patient),(/medicos) o (/enfermeras)
-  Consultar pacientes → GET (/patient),(/medicos) o (/enfermeras)
-  Editar paciente → PUT (/patient/{patient_id}),(/medicos/{id}) o (/enfermeras/{id})
-  Eliminar paciente → DELETE (/patient/{patient_id}),(/medicos/{id}) o (/enfermeras/{id})
  
2. **Gestión de Citas Médicas**:
-  Registrar cita → POST /citas/
-  Consultar citas → GET /citas/
-  Actualizar cita → PUT /citas/{id}
-  Cancelar cita → DELETE /citas/{id}

4. **Generación de Diagnosticos**:
-  Crear Diagnostico → POST /diagnostico/
-  Consultar diagnosticos → GET /diagnostico/
-  Consultar diagnosticos por tipo de diagnostico → GET /diagnostico/tipo
-  Consultar diagnostico por id → GET /diagnostico/{diagnostico_id}
-  Actualizar diagnostico → PUT /diagnostico/{diagnostico_id}
-  Eliminar diagnostico → DELETE /diagnostico/{diagnostico_id}

5. **Generación de Facturas**:
-  Crear factura → POST /Factura/
-  Consultar facturas → GET /Factura/
-  Consultar facturas por paciente → GET /Factura/patient
-  Actualizar facturas → PUT /Factura/{factura_id}
-  Eliminar facturas → DELETE /Factura/{factura_id}

---

# Ejemplos en PostMan

## Medicos
**POST**: Crear un nuevo medico en la db
<img width="1481" height="633" alt="image" src="https://github.com/user-attachments/assets/c19ee029-b83e-4419-9745-ccaa941aa30f" />

**GET**: Obtener todos los medicos de la db
<img width="1474" height="753" alt="image" src="https://github.com/user-attachments/assets/4b81f794-50a1-445f-8c16-b21fe8bedfab" />


## Pacientes

**POST**: Crear un nuevo paciente para la db
<img width="1481" height="524" alt="image" src="https://github.com/user-attachments/assets/f58d9192-0921-491a-88c1-dbb3e0a5bb2a" />

**GET**: Obtiene el paciente mediante id
<img width="1486" height="534" alt="image" src="https://github.com/user-attachments/assets/e5f22f53-890c-4b4b-afec-7565847b5251" />

## Enferemeras

**POST**: Crear una nueva enfermera
<img width="1479" height="617" alt="image" src="https://github.com/user-attachments/assets/9645ea44-513e-411b-adb5-a86593ce65b5" />

**DELETE**: Eliminar la informacion de la enfermera de la db
<img width="1478" height="779" alt="image" src="https://github.com/user-attachments/assets/57e33b74-b526-4c0a-920b-7d85bf4e4f3d" />
<img width="1471" height="607" alt="image" src="https://github.com/user-attachments/assets/37db3db2-2ec2-4006-85e0-d8603f0d3ba3" />

**PUT**: actualizar la informacion de la enferemera en la db
<img width="1475" height="622" alt="image" src="https://github.com/user-attachments/assets/c528e825-78c0-4957-a3ae-fe2f1a9cefa7" />





