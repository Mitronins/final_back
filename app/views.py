from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Test
from app.serializers import TestSerializer, UserSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class NoCSRFView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)


class TestView(NoCSRFView):
    def get(self, request):
        tests = Test.objects.all()

        return Response(data={
            'data': TestSerializer(tests, many=True).data
        })

class UserView(NoCSRFView):
    def get(self, request):
        user = request.user

        return Response(data={
            'data': UserSerializer(user).data
        })


class LoginView(NoCSRFView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.get(username=username)
        if username and password:
            login(request, user)
            return Response()
