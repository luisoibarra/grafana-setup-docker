# Grafana Setup

Configuración e instrucciones para el montaje del servicio de Grafana

## Para correr el servicio

1. Descargar imagen de Docker.
    - `docker pull grafana/grafana:10.2.0-ubuntu`

2. Abra una consola (se probó en PowerShell) en este directorio y corra una de las opciones provistas en `run_persistent_grafana.sh`

3. Configurar y conectar con base de datos.
    - Para conexión con base de datos local: En el host de Postgre poner `host.docker.internal:5432`.
    - Para conexión con base de datos: Poner host de la base de datos.

4. Empezar a crear dashborads.

### Visualización

1. Abrir un navegador en [http://localhost:3000](http://localhost:3000) (Asumiendo configuración por defecto y local)
2. Autenticarse como **admin** con contraseña **admin**
3. Crear un dashboard
4. Compartir el dashboard y pegar el iframe compartido en un [documento html](embedding.html)
5. Abrir el html con un navegador
