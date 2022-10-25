#!/bin/sh

# Удаляем все старые данные
python manage.py flush --no-input
# Выполняем миграции
python manage.py migrate
python manage.py makemigrations
python manage.py makemigrations core
python manage.py migrate
# собираем статику
python manage.py collectstatic
# загружаем тестовые данные
python manage.py loaddata example_data/user.json
python manage.py loaddata example_data/core.json
python manage.py loaddata example_data/taggit.json
# создаем супер-юзера
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

exec "$@"