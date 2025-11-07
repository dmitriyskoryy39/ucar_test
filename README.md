# Установка и запуск приложения

1. Клонировать проект
git clone https://github.com/dmitriyskoryy39/ucar_test.git

2. Перейти в корневую папку проекта (ucar_test) и создать файл там .env cо след. содержимым :
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_DB='ucar_db'
POSTGRES_HOST=ucar-db
POSTGRES_PORT=5432
LOCAL_HOST=0.0.0.0
LOCAL_PORT=8007

3. Выполнить команду
docker compose up -d --build

4. Дождаться создания и запуска контейнеров, после чего перейти в swagger:
http://localhost:8007/docs


