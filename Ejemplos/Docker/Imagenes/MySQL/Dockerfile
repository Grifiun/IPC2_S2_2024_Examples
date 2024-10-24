FROM mysql:latest

# Credenciales y nombre db
ENV MYSQL_ROOT_PASSWORD=password 
ENV MYSQL_DATABASE=mydb 

# En este directorio MySQL deben tener un archivo sql script (opcional)
COPY script.sql /docker-entrypoint-initdb.d/