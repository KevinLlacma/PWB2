# Utilizar la imagen oficial de MySQL
FROM mysql:8.0

# Configurar variables de entorno para la base de datos
ENV MYSQL_DATABASE=tienda \
    MYSQL_USER=tienda \
    MYSQL_PASSWORD=tienda \
    MYSQL_ROOT_PASSWORD=root

# Exponer el puerto 3306
EXPOSE 3306

# Utilizar un entrypoint script si es necesario
# COPY ./init.sql /docker-entrypoint-initdb.d/

# Comando para iniciar MySQL
CMD ["mysqld"]
