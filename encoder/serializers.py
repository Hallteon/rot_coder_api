from rest_framework import serializers

from rot_api.encoder.models import Rot


class RotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rot
        fields = '__all__'
