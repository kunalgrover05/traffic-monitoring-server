from django.db import models

class DeviceData(models.Model):
    dev_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12,null=True, blank=True)

class TrafficData(models.Model):
	macadd = models.CharField(max_length=12)
	timestamp = models.DateTimeField(auto_now_add=True)
	device = models.ForeignKey(DeviceData,on_delete=models.CASCADE)
