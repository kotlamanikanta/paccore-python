from django.shortcuts import render

# Create your views here.

def feeCollection(request):
    return render(request,'finance/fee-Collection-report.html')
def feeDuesReport(request):
    return render(request,'finance/fee-collection.html')
 
def feeCollectionReport(request):
    return render(request,'finance/fee-due-report.html')
