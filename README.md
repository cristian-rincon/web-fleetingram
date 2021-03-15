# fleetingram

  
  
  ![fleetingram logo](http://35.238.121.114:8000/static/img/instagram.png)

MVP de aplicación social basada en instagram - web.

---
 
  

## Stack utilizado


- Python 3.7

- Django 3.1

- PostgreSql
  

Mayor información: cristian.o.rincon.b@gmail.com

2021

## Cosas por implementar

- Sistema de follow
- Sistema de likes
- Mejorar la interfaz

## Necesario para desplegar

1. Tener un bucket de google cloud.
2. Crear y descargar una cuenta de servicio con permisos para la lectura y escritura en el bucket. Esta credencial debe ir en la carpeta conf/ y se debe llamar credentials.json


### Como levantar el servicio con docker en local

Para levantar el servicio se debe usar el comando:

```bash
docker-compose up --build ## solo la primera vez
docker-compose up
```

Luego de esto, ingresa desde tu localhost al puerto 8000. (http://localhost:8000)
