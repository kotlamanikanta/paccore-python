from django.urls import path
from admissions.views import addAdmission
from admissions.views import admissionsReport
urlpatterns = [
    

    path('newadm/', addAdmission),
    path('admreport/', admissionsReport),
]
