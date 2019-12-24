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

        parser.add_argument('--views', dest='views', action='store_true',
                            help='generate views only'),

        parser.add_argument('--urls', dest='urls', action='store_true',
                            help='generate urls only'),

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You should provide an app to generate an API')

        generator = BaseGenerator(app_config)
        result = generator.generate_serializers()
        result += generator.generate_views()
        result += generator.generate_urls()

        print(result)
