# Nombre del proyecto: comiqueria
# Nombre de la aplicación: comiqueriapp
# Alumno: Medina Eduardo Daniel
# Fecha: 07/02/2024
# Versión: TERCERA-PRE-ENTREGA 1.0


- Usuario y contraseña de SUPERUSUARIO:
    -Usuario: admin
    -Contraseña: 12345


# Esta aplicaión sirve para la busqueda de algun comic en especifico en una base de datos que contiene: -Clientes, -Comics, -Distribuidores.

- Los modelos utilizados en esta aplicación son:
    -Cliente
    -Comic 
    -Distribuidor

- el orden para la prueba de la aplicacion es:
    -Crear un nuevo cliente: localhost:8000/comiqueriapp/clienteForm
    -Crear un nuevo comic: localhost:8000/comiqueriapp/comicForm
    -Crear un nuevo distribuidor: localhost:8000/comiqueriapp/distribuidorForm


-Consultar en la db todos los datos guardados: 
    -Datos de clientes: localhost:8000/comiqueriapp/cliente
    -Datos de comics: localhost:8000/comiqueriapp/comic
    -Datos de distribuidor: localhost:8000/comiqueriapp/distribuidor

-Otra manera de consultar en la db todos los datos guardados:
    -Desde el menú, seleccionar la opción cliente
    -Desde el menú, seleccionar la opción comic
    -Desde el menú, seleccionar la opción distribuidor

-Busqueda de COMICS por un patron de nombre o letra perteneciente al comic a buscar:
    -localhost:8000/comiqueriapp/buscar

