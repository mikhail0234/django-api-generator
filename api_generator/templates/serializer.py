SERIALIZER = """from rest_framework.serializers import ModelSerializer
from {{ app }}.models import {{ models | join:', ' }}
{% for model in models %}

class {{ model }}Serializer(ModelSerializer):

    class Meta:
        model = {{ model }}
        fields = '__all__'
{% endfor %}"""
