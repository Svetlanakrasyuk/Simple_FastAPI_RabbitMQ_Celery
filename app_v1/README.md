# Simple_FastAPI_RabbitMQ_Celery

Запуск rabbitmq  в Docker:
docker run -d -p 5672:5672 rabbitmq

Запуск приложения:
uvicorn main:app --reload

Запуск Celery workera:
celery -A celery_main:app_celery worker --loglevel=INFO

Запуск Celery flower:
celery -A celery_main:app_celery flower

Запуск Celery beat:
celery -A tasks beat --loglevel=INFO

При изменении Item в excel файле Menu.xlsx, который расположен в /admin, автоматически изменяется информация в базе данных, каждые 10 секунд.
