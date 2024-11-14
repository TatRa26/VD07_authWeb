import os

class Config:
    # Секретный ключ для сессий
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

    # Настройки для подключения к базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключаем отслеживание изменений
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # Опционально, если вы хотите использовать PostgreSQL, замените строку выше на:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase'

    # Для использования MySQL:
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/mydatabase'
