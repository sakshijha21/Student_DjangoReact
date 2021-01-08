
from django.db import models
class Students(models.Model):
    Roll=models.CharField("Roll",max_length=50,default="",unique=True)
    Name=models.CharField("Name",max_length=50,default="")
    Maths=models.IntegerField("Maths",default=0)
    Physics=models.IntegerField("Physics",default=0)
    Chemistry=models.IntegerField("Chemistry",default=0)
    Total=models.IntegerField("Total",default=0)
    Percentage=models.DecimalField("Percentage",default=0.0,max_digits=20,decimal_places=15)