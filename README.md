# ConfigDB.py - Herramienta para Restaurar Base de Datos MSSQL

Este repositorio contiene un script de Python llamado `configdb.py` que facilita la restauración de una base de datos MSSQL. Antes de ejecutar el script seguir los pasos a continuación.

## Pasos Previos

### 1. Configuración del Entorno Virtual

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate  # en sistemas basados en Unix
venv\Scripts\activate      # en sistemas Windows
```

### 2. Instalación de Dependencias


```bash
pip install -r requirements.txt

```


### 3. Levantar el Servicio MSSQL con Docker Compose


(previamente setear las variables de entorno en .env)

```bash
docker-compose up -d


```


### 4. Restarurar la db

```bash

python configdb.py



```


Este script automatiza el proceso de restauración de la base de datos MSSQL. 