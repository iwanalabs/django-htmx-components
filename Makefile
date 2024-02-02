PROJECT_DIR=$(shell pwd)
SRC_DIR=$(PROJECT_DIR)/src
INPUT_DIR=$(PROJECT_DIR)/src/static/input
OUTPUT_DIR=$(PROJECT_DIR)/src/static/output

run:
	cd ${SRC_DIR} && poetry run python manage.py runserver 8000

generate-key-no-django:
	poetry run python -c 'import secrets; print(secrets.token_urlsafe(50))'

migrate:
	cd ${SRC_DIR} && poetry run python manage.py makemigrations && poetry run python manage.py migrate

tailwind:
	npx tailwindcss -i $(INPUT_DIR)/style.css -o $(OUTPUT_DIR)/style.css --watch -c tailwind.config.js --minify

collectstatic:
	cd ${SRC_DIR} && poetry run python manage.py collectstatic

redis:
	docker run --rm --name redis-server -p 6379:6379 -v ${PROJECT_DIR}/tmp:/data redis

clear-cache:
	cd $(SRC_DIR) && poetry run python manage.py clear_cache
