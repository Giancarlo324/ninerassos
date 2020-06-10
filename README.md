# Niñeras SOS

Proyecto de la universidad sobre niñeras sos.

**Instalación:** 

Necesitan tener instalado python, versión más reciente **obligatorio.**

Instalar pip **obligatorio**, se usará para descargar las dependencias, independiente de cual sea su sistema operativo, los comandos serán igual, necesitan instalar pip.

Ejecutar requirements.txt con el siguiente comando: **pip install -r requirements.txt**.

Abrir una terminal y ubicarse dentro del directorio del proyecto, ejecutar los siguientes comandos:

python manage.py makemigrations blog
python manage.py makemigrations usuario

python manage.py migrate

python manage.py createsuperuser (Crear su respectivo usuario).

**El siguiente comando se lo ejecutará siempre para ejecutar el programa**

python manage.py runserver

Se recomienda trabajar con Visual Studio Code e instalar el complemento de Github. (Para editores del código).