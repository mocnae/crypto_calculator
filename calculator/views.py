from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Currency
from .serializers import *


@api_view(['GET'])
def currencys_list(request):
    if request.method == 'GET':
        qs = Currency.objects.all()
        serializer = CurrencySerializer(qs, context={'request': request}, many=True)
        return Response({'data': serializer.data})
