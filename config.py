import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/game_tracker')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv('REDIS_URL')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')