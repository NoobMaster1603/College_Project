from django.db import models

# Create your models here.
class Djemployee(models.Model):
    
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length = 50)
    emp_desig = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.emp_name
