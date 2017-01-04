# Asignacion de Horario:

Es un software destinado a la creación y gestión de horario para un carrera universitaria.

Construido en DJANGO 1.10, usando como motor de base de datos postgreSQL.

Para utilizar:

Cree un entorno virtual para Python3

	$ virtualenv -p python3 .

Acceda al entorno virtual de Python3:

	$ source ./bin/activate

Instale las dependencias usando pip:

	pip install django>=1.10.5 django_extensions django-bootstrap3 simplejson psycopg2

Edite con los parametros necesarios el settings.py del proyecto y por último corra el servidor web de Django usando:

	$ python manage runserver

Crear un usuario para acceder al sistema:

	$ python manage createsuperuser


