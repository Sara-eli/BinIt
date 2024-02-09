from django.urls import path,include
from Guest import views
app_name="webguest"
urlpatterns = [
    
    path('userregistration/',views.userregistration,name='userregistration'),
    path('ajax_ward/',views.ajax_ward,name='Ajaxward'),
    path('ajax_place/',views.ajax_place,name='Ajaxplace'), 
    path('login/',views.login,name='login'),


   
]
