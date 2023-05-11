from celery import Celery

from app.config import settings

# print(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0",)

celery = Celery(
    'tasks',
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=['app.tasks.tasks']
)