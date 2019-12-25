from django.template import Template, Context
from .templates.serializer import SERIALIZER
from .templates.apiview import API_URL, API_VIEW
import os.path


class BaseGenerator(object):
    """Базовый класс для генерации кода. При необходимости его
    основе можно создавать другие меняя шаблон template."""

    def __init__(self, config):
        self.config = config
        self.name = config.name
        self.app = config.models_module
        self.serializer_template = Template(SERIALIZER)
        self.models = self.get_model_names()
        self.serializers = self.get_serializer_names()
        self.view_template = Template(API_VIEW)
        self.url_template = Template(API_URL)

    def generate_serializers(self):
        """
        Запись сериалайзера в serializers.py.
        :return: результат работы функции
        """
        content = self.serializer_content()
        filename = 'serializers.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'Serializer generation cancelled'

    def generate_views(self):
        """
        Запись view в views.py.
        :return: результат работы функции
        """
        content = self.view_content()
        filename = 'views.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'View generation cancelled'

    def generate_urls(self):
        """
        Запись url в urls.py.
        :return: результат работы функции
        """
        content = self.url_content()
        filename = 'urls.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'Url generation cancelled'

    def serializer_content(self):
        """
        Генерация сожержимого для serializer.
        :return: content
        """
        context = Context({'app': self.name, 'models': self.models})
        return self.serializer_template.render(context)

    def view_content(self):
        """
        Генерация сожержимого для view.
        :return: content
        """
        context = Context({'app': self.name, 'models': self.models,
                           'serializers': self.serializers})
        return self.view_template.render(context)

    def url_content(self):
        """
        Генерация сожержимого для urls.
        :return: content
        """
        context = Context({'app': self.name, 'models': self.models})
        return self.url_template.render(context)

    def get_model_names(self):
        """
        Создание списка имен моделей приложения.
        :return: список имен моделей
        """
        return [model.__name__ for model in self.config.get_models()]

    def get_serializer_names(self):
        """
        Создание списка имен для сериалайзеров пл каждой модели.
        :return: список имен сериалайзеров
        """
        return[model + 'Serializer' for model in self.models]

    def write_file(self, content, filename):
        """
        Функция записи в файл.
        :param content: содерижмое для записи
        :param filename: имя файла
        :return: True при успешной записили или False при условии
         если оставляем предыдущую версию файла
        """
        name = os.path.join(os.path.dirname(self.app.__file__), filename)
        if os.path.exists(name):
            msg = "Do you want to overwrite %s? (y/n): " % filename
            prompt = input
            response = prompt(msg)
            if response != "y":
                return False
        new_file = open(name, 'w+')
        new_file.write(content)
        new_file.close()
        return True
