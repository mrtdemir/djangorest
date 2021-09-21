import json
from .serializer import *
from .models import *
from django.core.cache import cache,caches
from drf_yasg.utils import swagger_auto_schema
from user.models import *
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from .authentication import SpecialAuthentication
import os

def checkUser(userName):
    user_attr = UserUserattribute.objects.get(user=userName)
    if user_attr.full_api_login:return "full"
    else:return ""

def createButton(table):
    return '<a target="_blank" href="/list/'+table+'"><button>'+table+' - Ürünler XML Listesi</button></a>'

class FaoView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]

    queryset = Fao.objects.all()
    serializer_class = FaoSerializer

    @swagger_auto_schema(
        tags=["Üretim Verileri"],
        operation_id="FAO Dünya Tarımsal Üretim Verileri",
        operation_description=createButton('fao'),
        request_body=FaoSerializer, 
        responses={
            status.HTTP_200_OK: FaoResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = FaoSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])

            result = []
            datas = cache.get(checkUser(request.user)+'fao')
            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsdaView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]

    queryset = Usda.objects.all()
    serializer_class = UsdaSerializer

    @swagger_auto_schema(
        tags=["Üretim Verileri"],
        operation_id="USDA Dünya Tarımsal Üretim Verileri",
        operation_description=createButton('usda'),
        request_body=UsdaSerializer, 
        responses={
            status.HTTP_200_OK: UsdaResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = UsdaSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'usda')
            item = {'URUN_ID':urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class MapUretimlerView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = MapUretimler.objects.all()
    serializer_class = MapUretimlerSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="TÜİK Türkiye Tarımsal Üretim Verileri",
        operation_description=createButton('mapuretimler'),
        request_body=MapUretimlerSerializer, 
        responses={
            status.HTTP_200_OK: MapUretimlerResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = MapUretimlerSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'mapuretimler')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TufeView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tufe.objects.all()
    serializer_class = TufeSerializer

    @swagger_auto_schema(
        tags=["Fiyat Verileri"],
        operation_id="Tüfe Fiyatları",
        operation_description=createButton('tufe'),
        request_body=TufeSerializer, 
        responses={
            status.HTTP_200_OK: TufeResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TufeSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tufe')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UfeView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Ufe.objects.all()
    serializer_class = UfeSerializer

    @swagger_auto_schema(
        tags=["Fiyat Verileri"],
        operation_id="Üfe Fiyatları",
        operation_description=createButton('ufe'),
        request_body=UfeSerializer, 
        responses={
            status.HTTP_200_OK: UfeResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = UfeSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'ufe')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TuikView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tuik.objects.all()
    serializer_class = TuikSerializer

    @swagger_auto_schema(
        tags=["Üretim Verileri"],
        operation_id="Türkiye Üretim Verileri",
        operation_description=createButton('tuik'),
        request_body=TuikSerializer, 
        responses={
            status.HTTP_200_OK: TuikResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TuikSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tuik')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TuikexternalView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tuikexternal.objects.all()
    serializer_class = TuikexternalSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="Tüik Gts Dış Ticaret Verileri",
        operation_description=createButton('tuikexternal'),
        request_body=TuikexternalSerializer, 
        responses={
            status.HTTP_200_OK: TuikexternalResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TuikexternalSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tuikexternal')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TuikotsexternalView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tuikotsexternal.objects.all()
    serializer_class = TuikotsexternalSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="Tüik Ots Dış Ticaret Verileri",
        operation_description=createButton('tuikotsexternal'),
        request_body=TuikotsexternalSerializer, responses={
            status.HTTP_200_OK: TuikotsexternalResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TuikotsexternalSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tuikotsexternal')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TuikdirexternalView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tuikdirexternal.objects.all()
    serializer_class = TuikdirexternalSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="Tüik Gts Dir Kapsamlı Dış Ticaret Verileri",
        operation_description=createButton('tuikdirexternal'),
        request_body=TuikdirexternalSerializer, 
        responses={
            status.HTTP_200_OK: TuikdirexternalResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TuikdirexternalSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tuikdirexternal')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TuikotsdirexternalView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Tuikotsdirexternal.objects.all()
    serializer_class = TuikotsdirexternalSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="Tüik Ots Dir Kapsamlı Dış Ticaret Verileri",
        operation_description=createButton('tuikotsdirexternal'),
        request_body=TuikotsdirexternalSerializer, 
        responses={
            status.HTTP_200_OK: TuikotsdirexternalResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = TuikotsdirexternalSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'tuikotsdirexternal')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorldagricultureView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Worldagriculture.objects.all()
    serializer_class = WorldagricultureSerializer

    @swagger_auto_schema(
        tags=["Ticaret Verileri"],
        operation_id="Dünya Tarım ve Gıda Ticareti (UN)",
        operation_description=createButton('worldagriculture'),
        request_body=WorldagricultureSerializer, 
        responses={
            status.HTTP_200_OK: WorldagricultureResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = WorldagricultureSerializer(data=request.data)
        if serializer.is_valid():

            try:
                urun_id = int(serializer.validated_data['urun_id'].split()[0])
            except:
                urun_id = int(serializer.validated_data['urun_id'])
            datas = cache.get(checkUser(request.user)+'worldagriculture')

            item = {"URUN_ID":urun_id}
            [item.pop(key) for key,value in item.copy().items() if not value]
            data = [x for x in datas if item.items() <= x.items()]
            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductpriceView(views.APIView):
    permission_classes = [SpecialAuthentication]
    authentication_classes = [BasicAuthentication]
    queryset = Productprice.objects.all()
    serializer_class = ProductpriceSerializer

    @swagger_auto_schema(
        tags=["Fiyat Verileri"],
        operation_id="Ürün Fiyatları",
        operation_description=createButton('productprice'),
        request_body=ProductpriceSerializer, 
        responses={
            status.HTTP_200_OK: ProductpriceResultSerializer(many=True)
        })
    def post(self, request, format=None):
        serializer = ProductpriceSerializer(data=request.data)
        if serializer.is_valid():

            variety = serializer.validated_data['variety']
            year = serializer.validated_data['year']

            if checkUser(request.user) == "full":
                m_cache = caches['marketprice']
                path = os.path.dirname(os.path.abspath(__file__))
                file = open(path+"/cachelist.txt", "r",encoding="utf-8")
                cache_list = file.read()
                cache_list = json.loads(cache_list)
                cache_name = [item['CACHE_NAME'] for item in cache_list if item["VARIETY"] == variety]
                data = m_cache.get('marketprices'+cache_name[0]+str(year))
            else:
                datas = cache.get('marketprices')
                item = {"VARIETY":variety,"YEAR":year}
                [item.pop(key) for key,value in item.copy().items() if not value]
                data = [x for x in datas if item.items() <= x.items()]

            if data:
                message = "Successful"
                count = len(data)
            else:
                message = "NoResult"
                count = 0

            result = {
                'count':count,
                'error': '0',
                'message': message,
                'result': data,
            }
            return Response(status=status.HTTP_201_CREATED, data=result)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
