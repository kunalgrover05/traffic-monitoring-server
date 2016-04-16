from django.db import models

# Create your models here.
class BTData(models.Model):
	bt_id = models.CharField(max_length=12)
	timestamp = models.DateTimeField(auto_now_add=True)
	hardware_id = models.IntegerField()