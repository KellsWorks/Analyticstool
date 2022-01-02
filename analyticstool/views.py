from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from _datetime import datetime


@api_view(['GET'])
def index():
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Server currently running on time' + date

    return Response(data=message, status=status.HTTP_200_OK)
