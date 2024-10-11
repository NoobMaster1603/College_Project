from django.db import models

# Create your models here.
class Employ_info(models.Model):
    
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length = 100)
    emp_desig = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.emp_name
