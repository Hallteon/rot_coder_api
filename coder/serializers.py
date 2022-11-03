from rest_framework import serializers
from coder.models import Rot


class RotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rot
        fields = ['rot', 'usages']
