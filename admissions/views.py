from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm


# Create your views here.

#function based,class based views
def homepage(request):
    return render(request,'index.html')

def addAdmission(request):
    form = StudentModelForm
    studentform={'form':form}

    if request.method=='POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)    
    return render(request,'admissions/add-admission.html',studentform)
def admissionsReport(request):
    result = Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/admissions-report.html',students)
