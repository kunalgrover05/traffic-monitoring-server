from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import TrafficDataForm
from .models import TrafficData, DeviceData
from django.core.urlresolvers import reverse
import pdb

def upload(request):
  if request.method =='POST':
    form =TrafficDataForm(request.POST, request.FILES)
    if form.is_valid():
      f = request.FILES['file']

      dev, c = DeviceData.objects.get_or_create(dev_id=int(f.readline()))

      for line in f.readlines():
        t = TrafficData.objects.create(macadd=line[8:25], device=dev)
        t.save()
  else:
    form = TrafficDataForm()
  return render(
    request,
    'uploader/index.html',
    {'form':form}
  )
