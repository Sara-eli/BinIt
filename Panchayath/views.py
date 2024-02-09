from django.shortcuts import render,redirect
from Panchayath.models import *
from User.models import*
from Admin.models import*
from datetime import date
from django.db.models import Q

# Create your views here.

def panchayathhomepg(request):
    panchayath=tbl_panchayath.objects.get(id=request.session['pid'])
    return render(request,'Panchayath/PanchayathHomepage.html',{'panchayath':panchayath})



def changepassword(request):
    panchayath=tbl_panchayath.objects.get(id=request.session['pid'])
    if request.method=="POST":
        curpass=panchayath.user_password
        if request.POST.get("txt_pass")==curpass:
            newpass=request.POST.get("txt_newpass")
            conpass=request.POST.get("txt_conpass")
            if newpass == conpass:
                panchayath.panchayath_password=newpass
                panchayath.save()
                return render(request,'Panchayath/PanchayathHomepage.html',{"msg":"Passwod Updated Sucessfully..."})
            else:
                return render(request,'Panchayath/Changepassword.html',{'msg':"cannot change password"})
        else:

            return render(request,'Panchayath/Changepassword.html',{'msg':"mismatch"})
    else:
        return render(request,'Panchayath/Changepassword.html')
    


def editprofile(request):    
    panchayath=tbl_panchayath.objects.get(id=request.session['pid'])
    if request.method =="POST":
        panchayath.panchayath_name=request.POST.get("txt_name")
        panchayath.panchayath_contact=request.POST.get("txt_contact")
        panchayath.panchayath_email=request.POST.get("txt_email")
        panchayath.save()
        return render(request,'Panchayath/Editprofile.html',{'panchayath':panchayath})
    else:
        return render(request,'Panchayath/Editprofile.html',{'panchayath':panchayath})
    
def panchayathmyprofile(request):
    panchayath=tbl_panchayath.objects.get(id=request.session['pid'])
    return render(request,'Panchayath/Myprofile.html',{'panchayath':panchayath})



def workerregistration(request):
    workerdata=tbl_workerregistration.objects.all()
    panchayathdata=tbl_panchayath.objects.get(id=request.session["pid"])
    ward=tbl_ward.objects.filter(panchayath=panchayathdata)
    if request.method=="POST":
        tbl_workerregistration.objects.create(worker_name=request.POST.get("txt_name"),
        worker_contact=request.POST.get("txt_contact"),
        worker_email=request.POST.get("txt_email"),
        worker_password=request.POST.get("txt_password"),
        worker_gender=request.POST.get("txt_gender"),
        worker_photo=request.FILES.get("txt_photo"),
        worker_proof=request.FILES.get("txt_proof"),
        ward_id=tbl_ward.objects.get(id=request.POST.get("sel_ward")))
        return render(request,'Panchayath/WorkerRegistration.html',{'ward':ward,'workerdetails':workerdata})
    else:
        return render(request,'Panchayath/WorkerRegistration.html',{'ward':ward,'workerdetails':workerdata})

def del_worker(request,did):
    tbl_workerregistration.objects.get(id=did).delete()
    return redirect('webpanchayath:workerregistration')

def workerlist(request):
    panchayathdata=tbl_panchayath.objects.get(id=request.session["pid"])
    ward=tbl_ward.objects.filter(panchayath=panchayathdata)
    workerdata=tbl_workerregistration.objects.all()
    return render(request,'Panchayath/WorkerList.html',{'workerdetails':workerdata,'ward':ward})

def salary(request,did):
    workerdata=tbl_workerregistration.objects.get(id=did)
    if request.method == "POST":
        tbl_salary.objects.create(salary_date=date.today(),
        salary_amount=request.POST.get("txt_salary") ,
        worker=workerdata)
        return render(request,'Panchayath/Salary.html')
    else:
        return render(request,'Panchayath/Salary.html')
    
def viewcomplaint(request):
    complaint=tbl_complaint.objects.filter(user__place__ward=request.session['pid'],complaint_status=0)
    return render(request,'Panchayath/ViewComplaint.html',{'complaint':complaint})

def complaintreply(request,did):
    if request.method=="POST":
        updata=tbl_complaint.objects.get(id=did)
        updata.complaint_reply=request.POST.get("txt_reply")
        updata.complaint_status=1
        updata.save()
        return render(request,'Panchayath/ComplaintReply.html')
    else:
        return render(request,'Panchayath/ComplaintReply.html')
        

def viewfeedback(request):
    feedback=tbl_feedback.objects.filter(user__place__ward=request.session['pid'])
    return render(request,'Panchayath/ViewFeedback.html',{'feedback':feedback})


def viewward(request):
    ward=tbl_ward.objects.filter(panchayath=request.session['pid'])
    assign = tbl_assing.objects.all()
    workerids = []
    for a in assign:
        workerids.append(a.worker_id)
    worker=tbl_workerregistration.objects.filter(ward_id__panchayath=request.session['pid']).exclude(Q(id__in=workerids))
    print(request.session["pid"])
    if request.method == "POST":
        wr = tbl_workerregistration.objects.get(id=request.POST.get("sel_worker"))
        wa = tbl_ward.objects.get(id=request.POST.get("sel_ward"))
        tbl_assing.objects.create(worker=wr,ward=wa)
        return redirect("webpanchayath:viewward")
    else:
        return render(request,'Panchayath/Viewward.html',{'ward':ward,'worker':worker})

def assign_worker(request):
    return render(request,'Panchayath/Viewward.html')