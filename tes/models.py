from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExcelModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excelfile = models.FileField(upload_to='excel/', null=True, verbose_name="")

    def __str__(self):
        return self.pk
# Create your models here.
