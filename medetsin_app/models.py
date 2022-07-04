from wsgiref.validate import validator
from django.db import models
from .utils import rasm_olchami
# Create your models here.
    
class Jamoa(models.Model):
    img=models.ImageField(upload_to='jamoa _rasmlari', validators=[rasm_olchami])
    ismi=models.CharField(max_length=100)
    lavozimi=models.CharField(max_length=100)
    soat=models.DateTimeField()
    malumoti=models.TextField()

    
    def __str__(self):
        return self.ismi

# Create your models here.
