from django.shortcuts import render


# Create your views here.

#function based,class based views
def homepage(request):
    return render(request,'index.html')

def addAdmission(request):
    values={"name":"mani","age":36,"add":"vzm"}
    return render(request,'admissions/add-admission.html',values)

def admissionsReport(request):
    return render(request,'admissions/admissions-report.html')
