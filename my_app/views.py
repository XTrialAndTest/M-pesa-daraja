from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests
from django.shortcuts import render
from .models import *
from .serializers import *


def business_payment(request):
    cl = MpesaClient()
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://daraja-e9c3.onrender.com/api/callback'
    response = cl.business_payment(
        phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)


def promotion_payment(request):
    cl = MpesaClient()
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://daraja-e9c3.onrender.com/api/callback'
    response = cl.business_payment(
        phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)


def salary_payment(request):
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://daraja-e9c3.onrender.com/api/callback'
    response = cl.business_payment(
        phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)


def stk(request, *args, **kwargs):
    print(request.POST)
    cl = MpesaClient()
    phone_number = '0799979097'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = "https://daraja-e9c3.onrender.com/api/callback"
    response = cl.stk_push(phone_number, amount,
                           account_reference, transaction_desc, callback_url)
    print(response)
    return HttpResponse(response)


class Callback(CreateAPIView):
    queryset = Daraja.objects.all()
    serializer_class = DarajaSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print('+++++++++++', request.data)


def index(request):
    return HttpResponse('hello world')
