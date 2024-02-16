from celery import Celery

app_celery = Celery('celery_main',
                    broker='amqp://localhost',
                    backend='rpc://',
                    include=['tasks'])

app_celery.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'tasks.parse_item',
        'schedule': 10.0
    }
}
if __name__ == '__main__':
    app_celery.start()
