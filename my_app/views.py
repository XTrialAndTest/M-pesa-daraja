from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from rest_framework.views import APIView
import requests
from django.shortcuts import render


def business_payment(request):
    cl = MpesaClient()
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.business_payment(
        phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)


def promotion_payment(request):
    cl = MpesaClient()
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.business_payment(
        phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)


def salary_payment(request):
    phone_number = '0799979097'
    amount = 1
    transaction_desc = 'Description'
    occassion = 'Occassion'
    callback_url = 'https://api.darajambili.com/express-payment'
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
    callback_url = "https://vercel.com/xtrialandtest/todolist"
    response = cl.stk_push(phone_number, amount,
                           account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def callbackurl(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse(request)


def index(request):
    return HttpResponse('hello world')
