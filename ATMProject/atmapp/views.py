from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers
from .models import AtmPinRegister,Transaction
from .serializers import AtmPinRegisterSerializer
from rest_framework.response import Response
import ast
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
jwt_payload_handler=api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler=api_settings.JWT_ENCODE_HANDLER
# Create your views here.
class Loginview(APIView):
    def post(self,request):
        res=response.data
        token=request.get("token")
        username=request.get("username")
        password=request.get("password")
        try:
            user=User.objects.get(username=username)
        except:
            return Response("User not found")
        if not user.checkpassword(password):
            return Response("Incorrect password")
        payload=jwt_payload_handler(user)
        token=jwt_encode_handler(pay)
        firstname=user.first_name
        lastname=user.last_name
        return Response({"message":"Login successful","Firstname":firstname,"Lastname":lastname})

class AtmPinView(viewsets.ModelViewSet):
    queryset = AtmPinRegister.objects.all().order_by('-id')
    serializer_class=AtmPinRegisterSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = AtmPinRegisterSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            print(serialiser.data)
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
class pin_validate(APIView):
    def post(self,request):
        print(request.data)
        atmobj = AtmPinRegister.objects.get(cardnumber=request.data['card'])
        if atmobj:
            if atmobj.pin == request.data['pin']:
                return Response("Validation Successful")
            else:
                return Response('Incorrect PIN')
        else:
            return Response('Invalid Card Number')
            
        return Response("Validation Successful")
        
class deposit(APIView):
    def post(self,request):
        atmobj = AtmPinRegister.objects.get(cardnumber=request.data['card'])
        if atmobj:
            if atmobj.pin == request.data['pin']:
                amount = int(atmobj.balance)-int(request.data['amount'])
                atmobj.balance = amount
                atmobj.save()
                Transaction.objects.create(username = atmobj,transaction_method='deposit',transactionamount=request.data['amount'])
                return Response('Transaction Successful')
            else:
                return Response('Incorrect PIN')
        else:
            return Response('Invalid Card Number')
        
        
class withdraw(APIView):
    def post(self,request):
        print(request.data)
        atmobj = AtmPinRegister.objects.get(cardnumber=request.data['card'])
        if atmobj:
            if atmobj.pin == request.data['pin']:
                if int(request.data['amount']) > 20000:
                    return Response('Exceeded maximum withdrawal limit of Rs.20000')
                amount = int(atmobj.balance)+int(request.data['amount'])
                if amount>0:
                    atmobj.balance = amount
                    atmobj.save()
                    Transaction.objects.create(username = atmobj,transaction_method='deposit',transactionamount=request.data['amount'])
                    return Response('Transaction Successful')
                else:
                    return Response('Insufficient Balance')
            else:
                return Response('Incorrect PIN')
        else:
            return Response('Invalid Card Number')
        
        
        
            


