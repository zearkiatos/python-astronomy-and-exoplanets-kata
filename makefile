docker-up:
	docker compose up --build -d
	docker exec -it python-astronomy-and-exoplanets-kata python consola_exoplanetas.py

docker-down:
	docker compose down