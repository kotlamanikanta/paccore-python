from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm



# Create your views here.

#function based,class based views
def homepage(request):
    return render(request,'index.html')

def addAdmission(request):
    form = StudentModelForm
    studentform={'form':form,"errors":None}
    errors=None
    print("hello")
    print(request.GET)
    if request.method=='POST':
        print(request.POST)
        form = StudentModelForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
        else:
            errors=form.errors
            # return admissionsReport(request)
            return render(request,'admissions/add-admission.html',{"errors":errors,"form":form})
        return homepage(request)
        
    return render(request,'admissions/add-admission.html',studentform)
       

def admissionsReport(request):
    result = Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/admissions-report.html',students)

def deleteStudent(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return admissionsReport(request)

def updateStudent(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}
    errors=None
    if request.method=='POST':
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return admissionsReport(request)
        else:
            errors=form.errors
            # return admissionsReport(request)
            return render(request,'admissions/add-admission.html',{"errors":errors})

    return render(request,'admissions/update-admission.html',dict)


def addVendor(request):
    form = VendorForm
    vform={'form':form}

    if request.method=='POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return homepage(request)    
    return render(request,'admissions/add-vendor.html',vform)