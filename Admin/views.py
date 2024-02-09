from django.shortcuts import render,redirect
from Admin.models import *
from Panchayath.models import *
# Create your views here.



def place(request):
    dispanchayath=tbl_panchayath.objects.all()
    disward=tbl_ward.objects.all()
    diplace=tbl_place.objects.all()
    if request.method=="POST":
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),
        ward=tbl_ward.objects.get(id=request.POST.get("txt_ward")))
        return render(request,'Admin/Place.html',{'disward':disward,'dispanchayath':dispanchayath,'diplace':diplace})
    else:
        return render(request,'Admin/Place.html',{'disward':disward,'dispanchayath':dispanchayath,'diplace':diplace})

def ajax_ward(request):
    disob=tbl_panchayath.objects.get(id=request.GET.get('WARD'))
    ward=tbl_ward.objects.filter(panchayath=disob)
    return render(request,'Admin/Ajaxward.html',{'disward':ward})


def del_place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('webadmin:place')



# def up_place(request,did):
#     upplace=tbl_place.objects.get(id=did)
#     dispanchayath=tbl_panchayath.objects.all()
#     warddata=tbl_ward.objects.all()
#     diplace=tbl_place.objects.all()
#     if request.method=="POST":
#         wardid=tbl_ward.objects.get(id=request.POST.get("txt_ward"))
#         upplace.ward=wardid
#         panchayathid=tbl_panchayath.objects.get(id=request.POST.get("txt_panchayath"))
#         upplace.ward.panchayath=panchayathid
#         upplace.place_name=request.POST.get("txt_place")
#         upplace.save()
#         return render(request,'Admin/Place.html',{'disward':warddata,'diplace':diplace,'upplace':upplace,'dispanchayath':dispanchayath})
#     else:
#         # return redirect('webadmin:place')
#         return render(request,'Admin/Place.html',{'disward':warddata,'diplace':diplace,'upplace':upplace,'dispanchayath':dispanchayath})


def panchayath(request):
    dispanchayath=tbl_panchayath.objects.all()
    if request.method=="POST":
        tbl_panchayath.objects.create(panchayath_name=request.POST.get("txt_name"),
        panchayath_contact=request.POST.get("txt_contact"),
        panchayath_email=request.POST.get("txt_email"),
        panchayath_password=request.POST.get("txt_pass"))
        return render(request,'Admin/Panchayath.html',{'dispanchayath':dispanchayath})
    else:
        return render(request,'Admin/Panchayath.html',{'dispanchayath':dispanchayath})


def del_panchayath(request,did):
    tbl_panchayath.objects.get(id=did).delete()
    return redirect('webadmin:panchayath')


def up_panchayath(request,did):
    updata=tbl_panchayath.objects.get(id=did)
    dispanchayath=tbl_panchayath.objects.all()
    if request.method=="POST":
        updata.panchayath_name=request.POST.get("txt_name")
        updata.panchayath_contact=request.POST.get("txt_contact")
        updata.panchayath_password=request.POST.get("txt_pass")
        updata.save()
        return render(request,'Admin/Panchayath.html',{'dispanchayath':dispanchayath})
    else:
        return render(request,'Admin/Panchayath.html',{'dispanchayath':dispanchayath,'updata':updata})





def ward(request):
    disward=tbl_ward.objects.all()
    dispanchayath=tbl_panchayath.objects.all()
    if request.method=="POST":
        panchayathid=tbl_panchayath.objects.get(id=request.POST.get("txt_panchayath"))
        tbl_ward.objects.create(ward_number=request.POST.get("txt_ward"),panchayath=panchayathid)
        return render(request,'Admin/Ward.html',{'dispanchayath':dispanchayath,'disward':disward})
    else:
        return render(request,'Admin/Ward.html',{'disward':disward,'dispanchayath':dispanchayath})



def del_ward(request,did):
    tbl_ward.objects.get(id=did).delete()
    return redirect('webadmin:ward')


def up_ward(request,did):
    upward=tbl_ward.objects.get(id=did)
    warddata=tbl_ward.objects.all()
    panchayathdata=tbl_panchayath.objects.all()
    if request.method=="POST":
        panchayathid=tbl_panchayath.objects.get(id=request.POST.get("txt_panchayath"))
        upward.panchayath=panchayathid
        upward.ward_number=request.POST.get("txt_ward")
        upward.save()
        return render(request,'Admin/Ward.html',{'dispanchayath':panchayathdata,'upward':upward,'disward':warddata})
    else:
        return render(request,'Admin/Ward.html',{'dispanchayath':panchayathdata,'upward':upward,'disward':warddata})




def wastetype(request):
    diswaste=tbl_waste.objects.all()
    if request.method=="POST":
        tbl_waste.objects.create(waste_type=request.POST.get("txt_waste"))
        return render(request,'Admin/Wastetype.html',{'diswaste':diswaste})
    else:
        return render(request,'Admin/Wastetype.html',{'diswaste':diswaste})


def delwaste(request,did):
    tbl_waste.objects.get(id=did).delete()
    return redirect('webadmin:wastetype')

def upwaste(request,did):
    up_waste=tbl_waste.objects.get(id=did)
    diswaste=tbl_waste.objects.all()
    if request.method=="POST":
        up_waste.waste_type=request.POST.get("txt_waste")
        up_waste.save()
        return render(request,'Admin/Wastetype.html',{'diswaste':diswaste})
    else:
        return render(request,'Admin/Wastetype.html',{'diswaste':diswaste,'up_waste':up_waste})
    

def workerverification(request):
    worker=tbl_workerregistration.objects.filter(ward_id__panchayath=request.session["pid"])
    workerdetails=tbl_workerregistration.objects.all()
    return render(request,'Admin/Workerverification.html',{'workerdetails':workerdetails,'worker':worker})

def verifyworker(request,did):
    worker=tbl_workerregistration.objects.get(id=did)
    worker.worker_status=1
    worker.save()
    return redirect('webadmin:Workerverification')  

def verify(request):
    worker_data=tbl_workerregistration.objects.filter(worker_status=1)
    return render(request,'Admin/VerifiedWorker.html',{'workerdetails':worker_data})   

def workerreject(request,did):
    worker=tbl_workerregistration.objects.get(id=did)
    worker.worker_status=2
    worker.save()
    return redirect('webadmin:Workerverification')

def reject(request):
    worker_data=tbl_workerregistration.objects.filter(worker_status=2)
    return render(request,'Admin/RejectedList.html',{'workerdetails':worker_data})   


def adminhomepg(request):
    admin=tbl_admin.objects.get(id=request.session['aid'])
    return render(request,'Admin/Adminhomepage.html',{'admin':admin})