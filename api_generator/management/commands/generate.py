import sys

from django.core.management.base import AppCommand, CommandError
from api_generator.generator import BaseGenerator


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument('--serializers', dest='serializers',
                            action='store_true',
                            help='generate serializers only'),



    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You should provide an app to generate an API')

        generator = BaseGenerator(app_config)
        result = generator.generate_serializers()

        print(result)
