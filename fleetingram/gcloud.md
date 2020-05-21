# Desplegar Django en Gcloud

¡Hola! este es un breve resumen de cómo hacer el despliegue de la aplicación en Gcloud **App engine flexible**. Este pequeño instructivo está realizado utilizando el siguiente stack principal:

|Lenguaje     | Framework |Base de datos |Despliegue                |
|-------------|-----------|--------------|--------------------------|
| Python 3.7  |Django 2.2 |PostgreSQL	 |Gcloud App engine flexible|

- El manejador de dependencias que utilicé para todo el proyecto fué Pipenv, en caso de que lo deseen probar les dejo un link a la documentación para que puedan conocerlo.
[Pipenv - Documentación oficial](https://pipenv-es.readthedocs.io/es/latest/)

## Configurando el entorno local

Primero instalamos un par de dependencias en nuestro entorno de desarrollo, las cuales nos ayudarán a manejar los archivos estáticos (css, imagenes), para poder realizar el despliegue.

- gunicorn
- whitenoise
- pillow

Luego de esto hay unas configuraciones en local y en cloud que nos permitirán realizar el despliegue, estas te las mostraré en el siguiente  paso.

## Configurando el entorno  Gcloud

Lo primero que hice fué crear un proyecto en google cloud, te dejo un enlace a la documentación de google para que lo revises si aún no lo has hecho: 

[Entorno flexible App Engine](https://cloud.google.com/appengine/docs/flexible/)

Una vez has creado tu proyecto, es momento de realizar la creación de la base de datos en CloudSQL, en cuyo caso te dejo la documentación oficial del proceso para que lo puedas realizar:

[Ejecutar Django en el entorno Flexible de App Engine](https://cloud.google.com/python/django/flexible-environment?hl=es-419)

Si deseas ver el resultado final, puedes ingresar a : conexe.appspot.com

Si tienes alguna duda puntual te invito a dar follow en mi perfil de github y también me puedes escribir a : cristian.o.rincon.b@gmail.com

Espero haberte ayudado en tu proceso de aprendizaje. Feliz Día
