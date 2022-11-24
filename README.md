# ProyectoFinal

Alumnos: Leandro Ruiz, Leandro Padovani

## Descripción:

El blog consiste en la publicación de travesías deportivas, las cuales el administrador publica.
Los competidores podrán registrarse, especificando en cuales de las travesias quiere participar.

## Configuraciones iniciales:

Para comenzar con el desarrollo se siguieron algunos pasos iniciales descriptos a continuación:
- 1- Se creó el siguiente repositorio en GitHub https://github.com/Leandrorb98/UNO.git.
- 2- Se clonó el repositorio en los servidores locales de trabajo. (git clone https://github.com/Leandrorb98/UNO.git .)
- 3- Se verificó la instalación del framework Django. (pip install django)
- 4- Se comenzó un nuevo proyecto en el Visual Studio Code. En este caso en unofinal. (django-admin startproject unofinal)
- 5- Se hace una migración inicial de la base de datos. (python manage.py migrate)
- 6- Se verifica que el proyecto funciona con las configuraciones iniciales. (python manage.py runserver)
- 7- En el arbol de trabajo del Visual Studio Code, se crea la aplicación blog. (python manage.py startapp blog)
- 8- Se da comienzo al desarrollo

## Descripción funcional del Blog:

El Blog cuenta con varias características entre las cuales podemos mencionar:
- Registro de usuarios y perfiles
- Logueo de usuarios
- Alta, baja y modificación de posteos, que incluyen autor, fecha de posteo, título y contenido.
- Interfaz amigable gracias a la utilización de componentes de Bootstrap
- Presentación de posteos mediante vista general y vista de detalles
- Acceso a panel de administración mediante http://127.0.0.1:8000/admin/. El administrador podrá dar de alta travesías, modificarlas o eliminarlas. Para esto deberá acreditar su identidad previamente.

- Se puede ver el video descriptivo en youtube.

## Navegación del Blog:
- La barra superior izquierda cuenta con un enlace "Home" desde el cual se accede a la página inicial. Adicionalmente se dispone de un enlace "About" a través del cual se puede tomar contacto con los desarrolladores.
- La barra superior derecha cuenta con un enlace "Login" destinado al logueo de usuarios. También se cuenta con la opción "Register" utilizada para registrar a los usuarios. El usuario deberá darse de alta, completando los campos solicitados.
- En el cuerpo del Blog, puede accederse a los distintos posteos.