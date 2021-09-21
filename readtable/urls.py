from django.urls import path
from . import views
app_name = "readtable"

urlpatterns = [
    path('fao/', views.FaoView.as_view(), name = "fao"),
    path('usda/', views.UsdaView.as_view(), name = "usda"),
    path('mapuretimler/', views.MapUretimlerView.as_view(), name = "mapuretimler"),
    path('tufe/', views.TufeView.as_view(), name = "tufe"),
    path('ufe/', views.UfeView.as_view(), name = "ufe"),
    path('tuik/', views.TuikView.as_view(), name = "tuik"),
    path('tuikexternal/', views.TuikexternalView.as_view(), name = "tuikexternal"),
    path('tuikotsexternal/', views.TuikotsexternalView.as_view(), name = "tuikotsexternal"),
    path('tuikdirexternal/', views.TuikdirexternalView.as_view(), name = "tuikdirexternal"),
    path('tuikotsexternal/', views.TuikotsexternalView.as_view(), name = "tuikotsexternal"),
    path('tuikotsdirexternal/', views.TuikotsdirexternalView.as_view(), name = "tuikotsdirexternal"),
    path('worldagriculture/', views.WorldagricultureView.as_view(), name = "worldagriculture"),
    path('productprice/', views.ProductpriceView.as_view(), name = "productprice"),
]