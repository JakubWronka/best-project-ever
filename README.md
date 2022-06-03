## Django blog application
#### A Django app built with Django Rest Framework and PostgreSQL.
Run the project with default settings:
```bash
docker-compose up --build
```
Useful commands:
* Get the list of Docker containers:
	```
	docker ps
	```
* Get inside the container with Python environment:
	```
	docker exec -it <container_id> /bin/bash
	```
* Get inside the container with the PostgreSQL database:
	```
	docker exec -it <container_id> psql -U <username> -W <db_name>
	```
	In case of this project:
	```
	docker exec -it <container_id> psql -U best_project_ever_db_user_01 -W best_project_ever_db_01
	```
