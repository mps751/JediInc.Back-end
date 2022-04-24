from rest_framework import serializers
from .models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ('ProjectID',
                  'ProjectName',
                  'ProjectBeginning',
                  'ProjectEnd',
                  'Value',
                  'Risk',
                  'Participants')