from django.shortcuts import render
from Admin.models import *
from Panchayath.models import *
# Create your views here.
def workerhomepg(request):
    worker=tbl_workerregistration.objects.get(id=request.session['wid'])
    return render(request,'Worker/Workerhomepage.html',{'worker':worker})

def workermyprofile(request):
    worker=tbl_workerregistration.objects.get(id=request.session['wid'])
    return render(request,'Worker/Myprofile.html',{'worker':worker})

def workereditprofile(request):    
    worker=tbl_workerregistration.objects.get(id=request.session['wid'])
    if request.method =="POST":
        worker.worker_name=request.POST.get("txt_name")
        worker.worker_contact=request.POST.get("txt_contact")
        worker.save()
        return render(request,'Worker/Editprofile.html',{'worker':worker})
    else:
        return render(request,'Worker/Editprofile.html',{'worker':worker})


