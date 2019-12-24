from django.template import Template, Context
from .templates.serializer import SERIALIZER
from .templates.apiview import API_URL, API_VIEW
import os.path


class BaseGenerator(object):

    def __init__(self, config):
        self.config = config
        self.name = config.name
        self.app = config.models_module
        self.serializer_template = Template(SERIALIZER)
        self.models = self.get_model_names()
        self.serializers = self.get_serializer_names()
        self.view_template = Template(API_VIEW)
        self.url_template = Template(API_URL)

    def generate_serializers(self, ):
        content = self.serializer_content()
        filename = 'serializers.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'Serializer generation cancelled'

    def generate_views(self):
        content = self.view_content()
        filename = 'views.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'View generation cancelled'

    def generate_urls(self):
        content = self.url_content()
        filename = 'urls.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'Url generation cancelled'

    def serializer_content(self, ):
        context = Context({'app': self.name, 'models': self.models})
        return self.serializer_template.render(context)

    def view_content(self):
        context = Context({'app': self.name, 'models': self.models,
                           'serializers': self.serializers})
        return self.view_template.render(context)

    def url_content(self):
        context = Context({'app': self.name, 'models': self.models})
        return self.url_template.render(context)

    def get_model_names(self):
        return [model.__name__ for model in self.config.get_models()]

    def get_serializer_names(self):
        return[model + 'Serializer' for model in self.models]

    def write_file(self, content, filename):
        name = os.path.join(os.path.dirname(self.app.__file__), filename)
        if os.path.exists(name):
            msg = "Are you sure you want to overwrite %s? (y/n): " % filename
            prompt = input  # python3
            response = prompt(msg)
            if response != "y":
                return False
        new_file = open(name, 'w+')
        new_file.write(content)
        new_file.close()
        return True

