PROJECT_DIR=$(shell pwd)
PACKAGE_DIR=$(PROJECT_DIR)/src
INPUT_DIR=$(PROJECT_DIR)/src/static/input
OUTPUT_DIR=$(PROJECT_DIR)/src/static/output

.PHONY: wheel

wheel:
	poetry build --format wheel

run-django:
	cd ${PACKAGE_DIR} && poetry run python manage.py runserver 5000

run-pyodide:
	make wheel && python3 -m http.server

migrate:
	rm ${PACKAGE_DIR}/db.sqlite3 && cd $(PACKAGE_DIR) && find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && poetry run python manage.py makemigrations && poetry run python manage.py migrate

tailwind:
	npx tailwindcss -i $(INPUT_DIR)/style.css -o $(OUTPUT_DIR)/style.css --watch -c tailwind.config.js --minify
