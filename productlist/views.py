from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from readtable.authentication import SpecialAuthentication
from rest_framework.authentication import BasicAuthentication

from user.models import *
import os
import ast

# 1: Render list as a html with xml format
# 2: Check custom Authentication of the user
# 3: Use basic auth with id and password
MAIN_URL = "https://127.0.0.1:8000"
CONTENT_TYPE ="application/xhtml+xml"

def checkUser(userName): #Check if the user has demo or full permission
    if userName.is_authenticated:
        user_attr = UserUserattribute.objects.get(user=userName)
        if user_attr.full_api_login:
            return "full"
        else:return ""
    else:return ""
    
def readfile(name): #read product list from txt and return as a dictionaty
   path = os.path.dirname(os.path.abspath(__file__))
   file = open(path+"/urunlist/"+name+".txt", "r",encoding="utf-8")
   contents = file.read()
   dictionary = ast.literal_eval(contents)
   file.close()
   return dictionary

class faoList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'faolist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/fao/"},content_type=CONTENT_TYPE)

class usdaList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'usdalist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/usda/"},content_type=CONTENT_TYPE)

class ufeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'ufelist')
        for i in queryset:
            print(i)
        return Response({'products': queryset,"url":MAIN_URL + "v1/ufe/"},content_type=CONTENT_TYPE)

class tufeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tufelist')
 
        return Response({'products': queryset,"url":MAIN_URL + "v1/tufe/"},content_type=CONTENT_TYPE)

class mapuretimlerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'mapuretimlerlist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/mapuretimler/"},content_type=CONTENT_TYPE)

class tuikList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tuiklist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/tuik/"},content_type=CONTENT_TYPE)

class tuikdirexternalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tuikdirexternallist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/tuikdirexternal/"},content_type=CONTENT_TYPE)

class tuikexternalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tuikexternallist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/tuikexternal/"},content_type=CONTENT_TYPE)

class tuikotsdirexternalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tuikotsdirexternallist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/tuikotsdirexternal/"},content_type=CONTENT_TYPE)

class tuikotsexternalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'tuikotsexternallist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/tuikotsexternal/"},content_type=CONTENT_TYPE)

class worldagricultureList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'list.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'worldagriculturelist')
        return Response({'products': queryset,"url":MAIN_URL + "v1/worldagriculture/"},content_type=CONTENT_TYPE)

class productpriceList(APIView):
    renderer_classes = [TemplateHTMLRenderer]# 1
    permission_classes = [SpecialAuthentication]# 2
    authentication_classes = [BasicAuthentication]# 3
    template_name = 'productlist.html'
    swagger_schema = None
    def get(self, request):
        queryset = readfile(checkUser(request.user)+'productlist')
        return Response({'products': queryset},content_type=CONTENT_TYPE)