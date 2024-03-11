# Anonymous Grafana
docker run -it --name=grafana -p 3000:3000 -v ${PWD}/ini/auth_anonymous_grafana.ini:/etc/grafana/grafana.ini  grafana/grafana:10.2.0-ubuntu

# JWT Grafana
docker run -it --name=grafana -p 3000:3000 -v ${PWD}/ini/jwt_grafana.ini:/etc/grafana/grafana.ini -v ${PWD}/JWT/jwks.json:/etc/grafana/jwks.json grafana/grafana:10.2.0-ubuntu

# Default Grafana
docker run -it --name=grafana -p 3000:3000 -v ${PWD}/ini/default_grafana.ini:/etc/grafana/grafana.ini grafana/grafana:10.2.0-ubuntu
