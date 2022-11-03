from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from encoder.models import Rot
from utils.coders import rot_encode


class RotCoderAPIView(APIView):

    def get(self, request):
        encode_string = rot_encode(-int(request.query_params['rot']))(request.query_params['string'])
        rot_code = Rot.objects.filter(rot=int(request.query_params['rot']))

        if rot_code.exists():
            rot_code.update(amount=F('amount') + 1)

        else:
            Rot.objects.create(rot=Rot.objects.get(rot=int(request.query_params['rot'])))

        return Response({'message': encode_string})

    def post(self, request):
        decode_string = rot_encode(int(request.data['rot']))(request.data['string'])
        rot_code = Rot.objects.filter(rot=int(request.data['rot']))

        if rot_code:
            rot_code.update(amount=F('amount') + 1)

        else:
            Rot.objects.create(rot=Rot.objects.get(rot=int(request.data['rot'])))

        return Response({'message': decode_string})


class RotStatusAPIView(APIView):

    def get(self, request):
        return Response(Rot.objects.all())
