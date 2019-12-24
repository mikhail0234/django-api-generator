from django.template import Template, Context
from .templates.serializer import SERIALIZER
import os.path


class BaseGenerator(object):

    def __init__(self, config):
        self.config = config
        self.name = config.name
        self.app = config.models_module
        self.serializer_template = Template(SERIALIZER)
        self.models = self.get_model_names()
        self.serializers = self.get_serializer_names()

    def generate_serializers(self, ):
        content = self.serializer_content()
        filename = 'serializers.py'
        if self.write_file(content, filename):
            return '  - writing %s' % filename
        else:
            return 'Serializer generation cancelled'

    def serializer_content(self, ):
        context = Context({'app': self.name, 'models': self.models})
        return self.serializer_template.render(context)

    def get_model_names(self):
        lst = []
        for model in self.config.get_models():
            lst.append(model.__name__)
        return lst

    def get_serializer_names(self):
        return[m + 'Serializer' for m in self.models]

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

