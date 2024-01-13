SECRET_KEY=your_secret_key_here
DEBUG=True  # или False в продакшн окружении

DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432  # порт вашей базы данных

EMAIL_PORT=587
EMAIL_USE_SSL=False  # или True, в зависимости от вашего почтового провайдера
EMAIL_HOST=smtp.your_email_provider.com
TEST_EMAIL_LOGIN=your_email@example.com
TEST_EMAIL_PASSWORD=your_email_password

CACHE_ENABLED=True  # или False, если кэш не используется
CACHE_LOCATION=your_cache_location  # например, 'localhost:11211'

STRIPE_API=your_stripe_api_key
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
CELERY_TIMEZONE=your_timezone  # например, 'Europe/Moscow'
CELERY_TASK_TRACK_STARTED=True

bot_token=asdsadfgsfdhert
