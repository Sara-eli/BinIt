from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Panchayath.models import *
# Create your views here.

def userregistration(request):
        dispanchayath=tbl_panchayath.objects.all()
        disward=tbl_ward.objects.all()
        diplace=tbl_place.objects.all()
        if request.method=="POST" and request.FILES:
            tbl_newuser.objects.create(user_name=request.POST.get("txt_name"),
            user_contact=request.POST.get("txt_contact"),
            user_email=request.POST.get("txt_email"),
            user_password=request.POST.get("txt_password"),
            user_address=request.POST.get("txt_address"),
            user_proof=request.FILES.get("txt_file"),
            place=tbl_place.objects.get(id=request.POST.get("txt_place"))
            )
            return render(request,'Guest/UserRegistration.html',{'disward':disward,'dispanchayath':dispanchayath,'diplace':diplace})
        else:
            return render(request,'Guest/UserRegistration.html',{'disward':disward,'dispanchayath':dispanchayath,'diplace':diplace})

             
    
def ajax_ward(request):
    disob=tbl_panchayath.objects.get(id=request.GET.get('WARD'))
    ward=tbl_ward.objects.filter(panchayath=disob)
    return render(request,'Guest/Ajaxward.html',{'disward':ward})

def ajax_place(request):
    disob=tbl_ward.objects.get(id=request.GET.get('PLACE'))
    place=tbl_place.objects.filter(ward=disob)
    return render(request,'Guest/Ajaxplace.html',{'displace':place})

def login(request):
    email=request.POST.get("txt_email")
    password=request.POST.get("txt_pass")
    if request.method=="POST":
        ucount=tbl_newuser.objects.filter(user_email=email,user_password=password).count()
        wcount=tbl_workerregistration.objects.filter(worker_email=email,worker_password=password,worker_status=1).count()
        pcount=tbl_panchayath.objects.filter(panchayath_email=email,panchayath_password=password).count()
        acount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        if ucount > 0:
            userdata=tbl_newuser.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('webuser:userhomepg')
        elif wcount>0:
            workerdata=tbl_workerregistration.objects.get(worker_email=email,worker_password=password)
            request.session['wid']=workerdata.id
            return redirect('webworker:workerhomepg')
        elif pcount>0:
            panchayathdata=tbl_panchayath.objects.get(panchayath_email=email,panchayath_password=password)
            request.session['pid']=panchayathdata.id
            return redirect('webpanchayath:panchayathhomepg')
        elif acount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('webadmin:adminhomepg')
        else:
            msg="invalid Credentials"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')

 







