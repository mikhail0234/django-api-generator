# django-api-generator

Модуль для автоматической генерации REST API для всех моделей в Django приложении на основе Django Rest Framework

# Установка 

Скачать проект и настроить окружение и установить модуль

    $ git clone https://github.com/mikhail0234/django-api-generator
    $ cd drf-generators
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install requirements.txt
    $ python3 setup.py install
    
Изменить settings.py


    INSTALLED_APPS = (
        ...
        'rest_framework',
        'api_generator',
        'app',
        ...
    )

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20
    }


# Использование

**Пример:** Генерация serializers.py view.py urls.py


    $ python3 manage.py generate api 
где ``app`` это приложение, для которого генерируется код

дополнительные команды:
  
  ``--serializers``          Генерация только сериалайзеров.
  
  ``--views``                Генерация только Views.
  
  ``--urls``                 Герерация только Urls.


**Пример 2:** Генерация только serializers.py 

    $ python3 manage.py generate api --serializers

-------------------
