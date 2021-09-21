from django.db import models
from django.core.cache import cache
from django.core.validators import MinValueValidator, MaxValueValidator

class Fao(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (3 : Sığır, 395 : Ayçiçeği, 270 : Portakal)',validators=[MinValueValidator(1), MaxValueValidator(2000)])    

class Usda(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (281 : Armut, 284 : Vişne, 585 : Şeker)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class MapUretimler(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (3 : Sığır, 11 : Ördek, 227 : Nohut)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tufe(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (36 : Kuzu Eti, 120 : Yoğurt, 339 : Pirinç)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Ufe(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (331 : Buğday, 339 : Pirinç, 467 : Şeker Pancarı)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tuik(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (3 : Sığır, 60 : Levrek, 270 :  Portakal)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tuikexternal(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (280 : Elma, 339 : Pirinç, 14 :  Tavuk)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tuikdirexternal(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (280 : Elma, 339 : Pirinç, 14 :  Tavuk)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tuikotsexternal(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (280 : Elma, 339 : Pirinç, 14 :  Tavuk)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Tuikotsdirexternal(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (280 : Elma, 339 : Pirinç, 14 :  Tavuk)',validators=[MinValueValidator(1), MaxValueValidator(2000)])   

class Worldagriculture(models.Model):
    urun_id = models.IntegerField(verbose_name='Ürün ID (155 : Bal, 516 : Bitkisel yağlar, zeytin, 833 :  Tavuk)',validators=[MinValueValidator(1), MaxValueValidator(2000)])

class Productprice(models.Model):
    variety = models.CharField(verbose_name="Arpa, Fasulye, Mısır",max_length=256)   
    year = models.IntegerField(verbose_name="2017",validators=[MinValueValidator(2017), MaxValueValidator(2021)])