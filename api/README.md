
### работа с unicode в урлах
https://stackoverflow.com/questions/16566069/url-decode-utf-8-in-python
    
    user urllib.parse.unquote()
    refactor path from slug to str

### проблема teggit переает название тега а не его slug
>вопрос stackoverflow
> 
>https://stackoverflow.com/questions/68285939/get-all-elements-that-contain-a-specific-tag-in-django-rest-framework

>дока джанги    
> 
>https://docs.djangoproject.com/en/4.1/topics/http/urls/

>utf-8 decoder online
> 
> https://www.online-decoder.com/ru

### первоначальные миграции
    python manage.py migrate
    python manage.py makemigrations
    python manage.py makemigrations core
    python manage.py migrate

### сохранение исходныз данных
    # порядок не важен
    python -Xutf8 manage.py dumpdata auth.user --indent 2 > example_data/user.json
    python -Xutf8 manage.py dumpdata core --indent 2 > example_data/core.json
    python -Xutf8 manage.py dumpdata taggit --indent 2 > example_data/taggit.json

### загрузка исзодныз данных
    # порядок важен user > core > taggit
    python manage.py loaddata example_data/user.json
    python manage.py loaddata example_data/core.json
    python manage.py loaddata example_data/taggit.json

### superuser 
    username - amid
    password - 1
