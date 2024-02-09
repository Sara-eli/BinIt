from django.urls import path,include
from Panchayath import views
app_name="webpanchayath"

urlpatterns = [


    path('worker/',views.workerregistration,name='workerregistration'),
    path('delete_worker/<int:did>',views.del_worker,name='delete_worker'),
    path('workerlist/',views.workerlist,name='workerlist'),
    path('salary/<int:did>',views.salary,name='salary_worker'),


    path('panchayathhomepage/',views.panchayathhomepg,name='panchayathhomepg'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('myprofile/',views.panchayathmyprofile,name='panchayathmyprofile'),

    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('complaintreply/<int:did>',views.complaintreply,name='replycomplaint'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),


    path('viewward/',views.viewward,name='viewward'),
    path('assign_worker/<int:id>',views.assign_worker,name="assign_worker"),

   
]