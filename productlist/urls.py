from django.urls import path
from .views import *
app_name="list"

urlpatterns = [
    path("fao/",faoList.as_view(),name="fao"),
    path("mapuretimler/",mapuretimlerList.as_view(),name="mapuretimler"),
    path("tufe/",tufeList.as_view(),name="tufe"),
    path("tuik/",tuikList.as_view(),name="tuik"),
    path("tuikdirexternal/",tuikdirexternalList.as_view(),name="tuikdirexternal"),
    path("tuikexternal/",tuikexternalList.as_view(),name="tuikexternal"),
    path("tuikotsdirexternal/",tuikotsdirexternalList.as_view(),name="tuikotsdirexternal"),
    path("tuikotsexternal/",tuikotsexternalList.as_view(),name="tuikotsexternal"),
    path("ufe/",ufeList.as_view(),name="ufe"),
    path("usda/",usdaList.as_view(),name="usda"),
    path("worldagriculture/",worldagricultureList.as_view(),name="worldagriculture"),
    path("productprice/",productpriceList.as_view(),name="productprice"),
]