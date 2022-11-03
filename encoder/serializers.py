from rest_framework import serializers

from encoder.models import Rot


class RotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rot
        fields = '__all__'
