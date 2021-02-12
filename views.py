from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET','POST'])
def firstView(request):
    return Response(data='This is simple Response')


class FirstRestApi(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data="This is Response from Class Based Api")

    def post(self,request,*args,**kwargs):
        return Response(data="This is Response from Class Based Api")

