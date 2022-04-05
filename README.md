# Fuego de Quasar

Realizado por: Iván Unterberger Bauni

## Dirección del API REST

https://consigna-meli-nam6ndwjhq-rj.a.run.app/

## Como ejecutar

El servicio esta subido a un servidor de Google Cloud.
Se necesita de algun cliente HTTP libre como por ejemplo "Postman" para poder realizar consultas al servicio.

- El payload del mensaje se debe enviar en el body del request tal como se ve en la imagen a continuacion
![captura1](https://user-images.githubusercontent.com/18707501/161793265-bc07e483-cc83-4baf-b494-d3987bec1074.JPG)

- Una vez que se encuentre cargada la informacion de las comunicaciones hacia los 3 satelites se obtendra el resultado en el siguiente formato
![Captura2](https://user-images.githubusercontent.com/18707501/161794471-da4156a2-4087-42b6-bee3-bf7c5250a4c4.JPG)

- Una vez que se obtiene el resultado (ya sea exitoso o no) la informacion se purga, con lo cual se deberan realizar los 3 request nuevamente.

## Ejecución en entorno local

- En caso de que se opte levantar la aplicacion en un entorno local de debera de tener instalado python3
- Una vez instalado python se deberan correr los siguientes comandos en la carpeta raiz del proyecto:
  #### pip install numpy
  #### pip install flask-restful
  #### Estos comandos instalaran las librerias necesarias para poder ejecutar el servicio
- Una vez instalado procederemos a correr el comando "python main.py" para levantar el servicio (desde la carpeta raiz del proyecto) 

![Captura3](https://user-images.githubusercontent.com/18707501/161798422-af28cc39-3693-435a-ba71-cf7f45a3a313.JPG)

  #### La url del servicio será la que figura en la linea que dice "running on http://........"
