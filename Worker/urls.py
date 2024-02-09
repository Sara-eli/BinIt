from django.urls import path,include
from Worker import views
app_name = "webworker"
urlpatterns=[

    path('workerhomepage/',views.workerhomepg,name='workerhomepg'),
    path('myprofile/',views.workermyprofile,name='myprofile'),
    path('editprofile/',views.workereditprofile,name='editprofile'),




]