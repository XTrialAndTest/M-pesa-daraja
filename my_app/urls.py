from django.urls import path
from .views import *


urlpatterns = [
    path('home', index, name='index'),
    path('business', business_payment, name='business_payment'),
    path('salary', salary_payment, name='salary_payment'),
    path('promotion', promotion_payment, name='promotion_payment'),
    path('stk', stk, name='stk'),
    path('callback', callbackurl, name='callback'),

]
