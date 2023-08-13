import random
import string
from .serializers import UrlDataSerializer
from .models import UrlData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect


@api_view(['GET', 'POST'])
def urlShort(request):
    if request.method == 'POST':
        serializer = UrlDataSerializer(data=request.data)
        if serializer.is_valid():
            shorturl = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = serializer.validated_data["url"]
            new_url = UrlData(url=url, shorturl=shorturl)
            new_url.save()
            request.user.urlshort.add(new_url)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = UrlData.objects.all()
        serializer = UrlDataSerializer(data, many=True)
        return Response(serializer.data)

