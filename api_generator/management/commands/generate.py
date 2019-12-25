from django.core.management.base import AppCommand, CommandError
from api_generator.generator import BaseGenerator


class Command(AppCommand):
    help = 'Generates Django Rest Framework API Views' \
           ' and Serializers, URLs for a Django app'

    args = "[appname ...]"

    def add_arguments(self, parser):
        """
        Добавление дополнительных команд для работы с модулем.
        :param parser:
        :return:
        """
        super(Command, self).add_arguments(parser)

        parser.add_argument('--serializers', dest='serializers',
                            action='store_true',
                            help='generate serializers only'),

        parser.add_argument('--views', dest='views', action='store_true',
                            help='generate views only'),

        parser.add_argument('--urls', dest='urls', action='store_true',
                            help='generate urls only'),

    def handle_app_config(self, app_config, **options):
        """
            Определение дополнительных команд для работы с модулем.
            :param app_config: конфигурация приложения
            :param options: дополнительные команды
            :return:
        """

        if app_config.models_module is None:
            raise CommandError('You should provide an app to generate an API')

        generator = BaseGenerator(app_config)
        views = options['views'] if 'views' in options else False
        urls = options['urls'] if 'urls' in options else False
        serializers = options['serializers'] if 'serializers' in\
                                                options else False

        if serializers:
            result = generator.generate_serializers()
        elif views:
            result = generator.generate_views()
        elif urls:
            result = generator.generate_urls()
        else:
            result = generator.generate_serializers()
            result += generator.generate_views()
            result += generator.generate_urls()

        print(result)
