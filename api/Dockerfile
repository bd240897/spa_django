# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /home/project/lms

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# чтобы работала pillow
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем содержимое текущей папки в контейнер
COPY . .
RUN pip install -r req.txt

#RUN python manage.py migrate

RUN chmod +x ./entrypoint.sh
COPY ./entrypoint.sh ./home/project/lms
ENTRYPOINT ["./entrypoint.sh"]

