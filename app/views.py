

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from rest_framework import viewsets,status
from .serializers import RateListSerializer,FlatCurListSerializer,VarCurListSerializer,RateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import RateList
from rest_framework.authtoken.models import Token


class RateListViewSet(viewsets.ModelViewSet):
    serializer_class = RateListSerializer
    queryset = RateList.objects.all()
    authentication_classes= (TokenAuthentication,)

    @action(detail=False,methods=['GET'])
    def flat_currencies(self, request):
        response={"message":"It's working"}
        queryset= RateList.objects.values('flat_currency').distinct()
        serializer = FlatCurListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['GET'])
    def variable_currencies(self, request):
        if request.GET.get('flat_currrency'):
            queryset= RateList.objects.filter(flat_currency=request.GET.get('flat_currrency')).values('variable_currency').distinct()
            serializer = VarCurListSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response={"error":"The query is not proper"}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False,methods=['GET'])
    def rate(self, request):
        if request.GET.get('flat_currrency') and request.GET.get('variable_currency'):
            queryset= RateList.objects.filter(flat_currency=request.GET.get('flat_currrency'),variable_currency=request.GET.get('variable_currency')).values('rate').distinct()
            serializer = RateSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response={"error":"The query is not proper"}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
        
        
   

def index(request):
    context={}
   
    if request.user.is_authenticated:
        print("Auth")
        tokens = Token.objects.filter(user=request.user).values('key')
        for tok in tokens:
            print(tok['key'])
            token = tok['key']
        context['token'] = token

    else:
        print("Not Auth")
        redirect("/login")
        
    return render(request,'app/index.html',context)


def listTeachers(request):
    
    context={}
    if request.user.is_authenticated:
        print("Auth")
        tokens = Token.objects.filter(user=request.user).values('key')
        for tok in tokens:
            print(tok['key'])
            token = tok['key']
        context['token'] = token
        context['user_id']= request.user
    
    return render(request,'app/getToken.html',context)
