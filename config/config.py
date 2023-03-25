import os
from pathlib import Path

CONFIG_FILE = str(Path(__file__).parent.absolute()) + "/settings.yaml"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's!!!!!ecret-key123123123123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://star:star@localhost/star'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
