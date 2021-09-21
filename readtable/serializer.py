from rest_framework import serializers
from .models import *

class FaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fao
        fields = "__all__"
        
class UsdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usda
        fields = "__all__"

class MapUretimlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapUretimler
        fields = "__all__"

class TufeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tufe
        fields = "__all__"

class UfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ufe
        fields = "__all__"

class TuikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuik
        fields = "__all__"

class TuikexternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuikexternal
        fields = "__all__"

class TuikdirexternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuikdirexternal
        fields = "__all__"

class TuikotsexternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuikotsexternal
        fields = "__all__"

class TuikotsdirexternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuikotsdirexternal
        fields = "__all__"

class WorldagricultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldagriculture
        fields = "__all__"

class ProductpriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productprice
        fields = "__all__"

class FaoResultSerializer(serializers.Serializer):
    URUN =serializers.CharField(label="Ürün Adı",required=False)
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    ULKE = serializers.CharField(label="Ülke Adı",required=False)
    DEGISKEN = serializers.CharField(label="Değişken Adı",required=False)
    YIL = serializers.IntegerField(label="Ürün Yılı",required=False)
    BIRIM = serializers.CharField(label="Ürün Birimi",required=False)
    DEGER = serializers.FloatField(label="Değer",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)

class UsdaResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    ULKE = serializers.CharField(label="Ülke",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    DEGISKEN = serializers.CharField(label="Değişken",required=False)
    BIRIM = serializers.CharField(label="Birim",required=False)
    DEGER = serializers.FloatField(label="Değer",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)
    
class MapUretimlerResultSerializer(serializers.Serializer):
    YIL = serializers.IntegerField(label="Yıl",required=False)
    IL_ADI = serializers.CharField(label="İl Adı",required=False)
    ILCE_ADI = serializers.CharField(label="İlçe Adı",required=False)
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    GRUP_ADI = serializers.CharField(label="Grup Adı",required=False)
    MADDE_ADI = serializers.CharField(label="Madde Adı",required=False)
    EKIM_ALANI = serializers.FloatField(label="Ekim Adı",required=False)
    BIRIM_EKIM_ALANI = serializers.CharField(label="Birim Ekim Alanı",required=False)
    HASAT_EDILEN_ALAN = serializers.FloatField(label="Hasat Edilen Alan",required=False)
    BIRIM_HASAT_ALANI = serializers.CharField(label="Birim Hasat Alanı",required=False)
    URETIM = serializers.FloatField(label="Üretim",required=False)
    BIRIM_URETIM = serializers.CharField(label="Birim Üretim",required=False)
    VERIM = serializers.FloatField(label="Verim",required=False)
    BIRIM_VERIM = serializers.CharField(label="Birim Verim",required=False)
    SAGILAN_HAYVAN_BAS = serializers.IntegerField(label="Sağılan Hayvan (Baş)",required=False)
    KIRKILAN_HAYVAN_SAYISI_BAS = serializers.IntegerField(label="Kırkılan Hayvan Sayısı (Baş)",required=False)
    MEYVE_VEREN_YASTA_AGAC_SAYISI = serializers.IntegerField(label="Meyve Veren Yaşta Ağaç Sayısı",required=False)
    MEYVE_VERMEYEN_YASTA_AGAC_SAYISI = serializers.IntegerField(label="Meyve Vermeyen Yaşta Ağaç Sayısı",required=False)
    KOY_SAYISI_ADET = serializers.IntegerField(label="Köy Sayısı (Adet)",required=False)
    HANE_SAYISI_ADET = serializers.IntegerField(label="Hane Sayısı (Adet)",required=False)
    ACILAN_KUTU_ADET = serializers.IntegerField(label="Açılan Kutu (Adet)",required=False)

class TufeResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM_ADI = serializers.CharField(label="Kalem",required=False)
    ACIKLAMA = serializers.CharField(label="Ülke",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Değişken",required=False)
    BIRIM = serializers.CharField(label="Birim",required=False)
    FIYAT_TUFE = serializers.FloatField(label="Değer",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)    

class UfeResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM_ADI = serializers.CharField(label="Kalem",required=False)
    ACIKLAMA = serializers.CharField(label="Ülke",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Değişken",required=False)
    BIRIM = serializers.CharField(label="Birim",required=False)
    FIYAT_UFE = serializers.FloatField(label="Değer",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False) 

class TuikResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    ALT_KALEM = serializers.CharField(label="Alt Kalem",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    MIKTAR = serializers.CharField(label="Birim",required=False)
    BIRIM = serializers.FloatField(label="Değer",required=False)

class TuikexternalResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Ay",required=False)
    ISTPOZ_ADI = serializers.CharField(label="Istpoz Adı",required=False)
    ULKE_ADI = serializers.CharField(label="Ülke Adı",required=False)
    OLCU_ADI = serializers.CharField(label="Ölçü Adı",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)
    ITHALAT_MIKTAR1 = serializers.FloatField(label="İthalat Miktarı 1",required=False)
    ITHALAT_MIKTAR2 = serializers.FloatField(label="İthalat Miktarı 2",required=False)
    ITHALAT_DOLAR = serializers.FloatField(label="İthalat Dolar",required=False)
    IHRACAT_MIKTAR1 = serializers.FloatField(label="İhracat Miktarı 1",required=False)
    IHRACAT_MIKTAR2 = serializers.FloatField(label="İhracat Miktarı 2",required=False)
    IHRACAT_DOLAR = serializers.FloatField(label="İhracat Dolar",required=False)

class TuikotsexternalResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Ay",required=False)
    ISTPOZ_ADI = serializers.CharField(label="Istpoz Adı",required=False)
    ULKE_ADI = serializers.CharField(label="Ülke Adı",required=False)
    OLCU_ADI = serializers.CharField(label="Ölçü Adı",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)
    ITHALAT_MIKTAR1 = serializers.FloatField(label="İthalat Miktarı 1",required=False)
    ITHALAT_MIKTAR2 = serializers.FloatField(label="İthalat Miktarı 2",required=False)
    ITHALAT_DOLAR = serializers.FloatField(label="İthalat Dolar",required=False)
    IHRACAT_MIKTAR1 = serializers.FloatField(label="İhracat Miktarı 1",required=False)
    IHRACAT_MIKTAR2 = serializers.FloatField(label="İhracat Miktarı 2",required=False)
    IHRACAT_DOLAR = serializers.FloatField(label="İhracat Dolar",required=False)

class TuikdirexternalResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Ay",required=False)
    ISTPOZ_ADI = serializers.CharField(label="Istpoz Adı",required=False)
    ULKE_ADI = serializers.CharField(label="Ülke Adı",required=False)
    OLCU_ADI = serializers.CharField(label="Ölçü Adı",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)
    ITHALAT_MIKTAR1 = serializers.FloatField(label="İthalat Miktarı 1",required=False)
    ITHALAT_MIKTAR2 = serializers.FloatField(label="İthalat Miktarı 2",required=False)
    ITHALAT_DOLAR = serializers.FloatField(label="İthalat Dolar",required=False)
    IHRACAT_MIKTAR1 = serializers.FloatField(label="İhracat Miktarı 1",required=False)
    IHRACAT_MIKTAR2 = serializers.FloatField(label="İhracat Miktarı 2",required=False)
    IHRACAT_DOLAR = serializers.FloatField(label="İhracat Dolar",required=False)

class TuikotsdirexternalResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    AY = serializers.IntegerField(label="Ay",required=False)
    ISTPOZ_ADI = serializers.CharField(label="Istpoz Adı",required=False)
    ULKE_ADI = serializers.CharField(label="Ülke Adı",required=False)
    OLCU_ADI = serializers.CharField(label="Ölçü Adı",required=False)
    KAYNAK = serializers.CharField(label="Kaynak",required=False)
    ITHALAT_MIKTAR1 = serializers.FloatField(label="İthalat Miktarı 1",required=False)
    ITHALAT_MIKTAR2 = serializers.FloatField(label="İthalat Miktarı 2",required=False)
    ITHALAT_DOLAR = serializers.FloatField(label="İthalat Dolar",required=False)
    IHRACAT_MIKTAR1 = serializers.FloatField(label="İhracat Miktarı 1",required=False)
    IHRACAT_MIKTAR2 = serializers.FloatField(label="İhracat Miktarı 2",required=False)
    IHRACAT_DOLAR = serializers.FloatField(label="İhracat Dolar",required=False)

class WorldagricultureResultSerializer(serializers.Serializer):
    URUN_ID = serializers.IntegerField(label="Ürün ID",required=False)
    KALEM = serializers.CharField(label="Kalem",required=False)
    ULKE = serializers.CharField(label="Ülke",required=False)
    HEDEF_ULKE = serializers.CharField(label="Ülke Adı",required=False)
    YIL = serializers.IntegerField(label="Yıl",required=False)
    TICARET_YONU = serializers.CharField(label="Ticaret Yönü",required=False)
    BIRIM = serializers.CharField(label="Birim",required=False)
    MIKTAR = serializers.FloatField(label="Miktar",required=False)
    DEGER_USD = serializers.FloatField(label="Değer USD",required=False)

class ProductpriceResultSerializer(serializers.Serializer):
    VARIETY = serializers.CharField(label="Çeşidi",required=False)
    MARKET = serializers.CharField(label="Market Adı",required=False)
    DAY = serializers.IntegerField(label="Gün",required=False)
    MONTH = serializers.IntegerField(label="Ay",required=False)
    YEAR = serializers.IntegerField(label="Yıl",required=False)      
    PRODUCT = serializers.CharField(label="Ürün",required=False)
    CATEGORY = serializers.CharField(label="Kategori",required=False)
    SELL_KIND = serializers.CharField(label="Satış Şekli",required=False)
    URL = serializers.CharField(label="Ürün Linki",required=False)          
    PRICE = serializers.FloatField(label="Fiyatı (TL)",required=False)
    HIGH_PRICE = serializers.FloatField(label="Üst Fiyatı (TL)",required=False)
    LOW_PRICE = serializers.FloatField(label="Alt Fiyatı (TL)",required=False)    
    QUANTITY = serializers.IntegerField(label="Miktarı",required=False)
    AMOUNT = serializers.FloatField(label="Tutar (TL)",required=False)      
    UNIT = serializers.CharField(label="Birim",required=False)
    CURRENCY_PRICE = serializers.FloatField(label="Döviz Fiyatı (TL)",required=False)