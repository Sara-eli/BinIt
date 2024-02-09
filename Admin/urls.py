from django.urls import path,include
from Admin import views
app_name = "webadmin"

urlpatterns = [
    

    path('adminhomepg/',views.adminhomepg,name='adminhomepg'),


    path('place/',views.place,name='place'),
    path('del_place/<int:did>',views.del_place,name='del_place'),
    #  path('up_place/<int:did>',views.up_place,name='up_place'),
    
    path('panchayath/',views.panchayath,name='panchayath'),
    path('del_panchayath/<int:did>',views.del_panchayath,name='del_panchayath'),
    path('up_panchayath/<int:did>',views.up_panchayath,name='up_panchayath'),
    
    
    path('ward/',views.ward,name='ward'),
    path('ajax_ward/',views.ajax_ward,name='Ajaxward'), 
    path('delward/<int:did>',views.del_ward,name='delward'),  
    path('upward/<int:did>',views.up_ward,name='upward'),
    
    
    path('waste/',views.wastetype,name='wastetype'), 
    path('del_waste/<int:did>',views.delwaste,name='del_waste'),
    path('up_waste/<int:did>',views.upwaste,name='up_waste'),


    path('workerverification/',views.workerverification,name='Workerverification'),
    path('verifyworker/<int:did>',views.verifyworker,name='verify_worker'),
    path('verify/',views.verify,name='verify'),
    path('workerreject/<int:did>',views.workerreject,name='Reject_worker'),
    path('reject/',views.reject,name='reject'),
     ]
