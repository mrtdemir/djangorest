from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserApipermissions(models.Model):
    mapuretimler = models.IntegerField(db_column='mapUretimler')  # Field name made lowercase.
    usda = models.IntegerField()
    fao = models.IntegerField()
    tuik = models.IntegerField()
    ufe = models.IntegerField()
    tufe = models.IntegerField()
    tuikexternal = models.IntegerField()
    tuikdirexternal = models.IntegerField()
    tuikotsexternal = models.IntegerField()
    tuikotsdirexternal = models.IntegerField()
    worldagriculture = models.IntegerField()
    productprice = models.IntegerField()
    api = models.OneToOneField('UserUserattribute', models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'user_apipermissions'

class UserUserattribute(models.Model):
    phonenumber = models.CharField(db_column='phoneNumber', max_length=13)  # Field name made lowercase.
    user = models.OneToOneField(User, models.DO_NOTHING)
    crawl_login = models.IntegerField()
    download_login = models.IntegerField()
    api_login = models.IntegerField()
    full_api_login = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'user_userattribute'