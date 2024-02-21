PROJECT_DIR=$(shell pwd)
SRC_DIR=$(PROJECT_DIR)/src
INPUT_DIR=$(PROJECT_DIR)/src/static/input
OUTPUT_DIR=$(PROJECT_DIR)/src/static/output

run:
	cd ${SRC_DIR} && poetry run python manage.py runserver 8000

generate-key:
	poetry run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

migrate:
	cd ${SRC_DIR} && poetry run python manage.py makemigrations && poetry run python manage.py migrate

tailwind:
	npx tailwindcss -i $(INPUT_DIR)/style.css -o $(OUTPUT_DIR)/style.css --watch -c tailwind.config.js --minify

collectstatic:
	cd ${SRC_DIR} && poetry run python manage.py collectstatic

compress:
	cd ${SRC_DIR} && poetry run python manage.py compress --force

redis:
	docker run --rm --name redis-server -p 6379:6379 -v ${PROJECT_DIR}/tmp:/data redis

clear-cache:
	cd $(SRC_DIR) && poetry run python manage.py clear_cache
