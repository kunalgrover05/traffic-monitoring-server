from django.db import models

# Create your models here.
class TrafficData(models.Model):
	bt_id = models.CharField(max_length=12)
	timestamp = models.DateTimeField(auto_now_add=True)
	dev_id = models.IntegerField()