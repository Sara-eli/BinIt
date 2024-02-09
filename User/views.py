from django.shortcuts import render
from Guest.models import *
from User.models import *
from Admin.models import *
from datetime import date



# Create your views here.



def usermyprofile(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'user':user})
    
def userhomepg(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,'User/UserHomepage.html',{'user':user})

def editprofile(request):    
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method =="POST":
        user.user_name=request.POST.get("txt_name")
        user.user_contact=request.POST.get("txt_contact")
        user.user_email=request.POST.get("txt_email")
        user.user_address=request.POST.get("txt_add")
        user.save()
        return render(request,'User/Editprofile.html',{'user':user})
    else:
        return render(request,'User/Editprofile.html',{'user':user})


def changepassword(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        curpass=user.user_password
        if request.POST.get("txt_pass")==curpass:
            newpass=request.POST.get("txt_newpass")
            conpass=request.POST.get("txt_conpass")
            if newpass == conpass:
                user.user_password=newpass
                user.save()
                return render(request,'User/Homepage.html',{"msg":"Passwod Updated Sucessfully..."})
            else:
                return render(request,'User/Changepassword.html',{'msg':"cannot change password"})
        else:

            return render(request,'User/Changepassword.html',{'msg':"mismatch"})
    else:
        return render(request,'User/Changepassword.html')
    


def complaint(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_complaint.objects.create(complaint_title=request.POST.get("txt_title"),
         complaint_description=request.POST.get("txt_description"),user=user,complaint_date=date.today())
        return render(request,'User/Complaint.html')
    else:
        return render(request,'User/Complaint.html')
        

def viewreply(request):
    cmpdata=tbl_complaint.objects.filter(user=request.session['uid'])
    return render(request,'User/ViewCmpReply.html',{'cmpdata':cmpdata})

def feedback(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get("txt_feedback"),user=user)
        return render(request,'User/Feedback.html')
    else:
        return render(request,'User/Feedback.html')



# def complaint(request):
#     return render(request,'User/Complaint.html')
