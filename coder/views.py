from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from coder.models import Rot
from coder.serializers import RotSerializer
from utils.coders import rot_encode


class RotCoderAPIView(APIView):

    def get(self, request):
        encode_string = rot_encode(-int(request.query_params['rot']))(request.query_params['message'])
        rot_code = Rot.objects.filter(rot=int(request.query_params['rot']))

        if list(rot_code):
            rot_code.update(usages=F('usages') + 1)

        else:
            Rot.objects.create(rot=int(request.data['rot']))

        return Response({'message': encode_string})

    def post(self, request):
        decode_string = rot_encode(int(request.data['rot']))(request.data['message'])
        rot_code = Rot.objects.filter(rot=int(request.data['rot']))

        if list(rot_code):
            rot_code.update(usages=F('usages') + 1)

        else:
            Rot.objects.create(rot=int(request.data['rot']))

        return Response({'message': decode_string})


class RotStatusListAPIView(ListAPIView):
    queryset = Rot.objects.all()
    serializer_class = RotSerializer
