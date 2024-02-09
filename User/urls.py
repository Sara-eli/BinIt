from django.urls import path,include
from User import views
app_name="webuser"

urlpatterns = [

    path('complaint/',views.complaint,name='complaint'),
    path('viewreply/',views.viewreply,name='viewreply'),
    path('feedback/',views.feedback,name='feedback'),
    


    path('myprofile/',views.usermyprofile,name='myprofile'),
    path('homepage/',views.userhomepg,name='userhomepg'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    


    
   
]
