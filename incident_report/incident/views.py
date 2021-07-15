from django.core import serializers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import IncidentSerializer, UserSerializer
from .models import Incident
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate

@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def login(request, format=None):
    if 'username' not in request.data:
        return Response({
            "status": 401,
            "message": "Username is required."
        })
    if 'password' not in request.data:
        return Response({
            "status": 401,
            "message": "Password is required."
        })

    user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    if user is not None:
        token = Token.objects.filter(user_id=user.id).first()
        if token is None:
            token = Token.objects.create(user=user)

        result = UserSerializer(user).data
        result['token'] = token.key
        return Response({
            "status": 200,
            "user": result
        })
    return Response({
        "status": 401,
        "message": "Incorrect username or password."
    })


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
@api_view(['GET', 'POST'])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def incident(request, format=None):
    if request.method == 'GET':
        queryset = Incident.objects.all().order_by('-id')
        serializer = IncidentSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


