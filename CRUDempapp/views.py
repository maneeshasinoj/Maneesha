from django.forms import EmailField
from django.forms import DateField
from django.shortcuts import redirect, render

from CRUDempapp.models import employee

# Create your views here.

# load employee page
def load_empinfo(request):
    return render(request,'empinfo.html')

# insert values..
def add_empdetails(request):
    if request.method=='POST':
        ename=request.POST['employee_name']
        addrs=request.POST['address']
        age=request.POST['age']
        email=request.POST['email']
        joindate=request.POST['joindate']
        qualification=request.POST['qualification']
        gender=request.POST['gender']

        emp=employee( employee_name=ename,
                        address=addrs,
                        age=age,
                        email_id=email,
                        joindate=joindate,
                        qualification=qualification,
                        gender=gender)
        emp.save()
        print("Hiiii")
        return redirect('showdetails')


  #show details...       
def showdetails(request):
    emps=employee.objects.all()  
    return render(request,'showempinfo.html',{'emp':emps})   


#load edit page....

def editpage(request,pk):
    emps=employee.objects.get(id=pk)  
    return render(request,'editinfo.html',{'emps':emps})


#edit employee details...

def edit_empdetails(request,pk):
    if request.method=='POST':
        emps=employee.objects.get(id=pk)
        emps.employee_name=request.POST.get('employee_name')
        emps.address=request.POST.get('address')
        emps.age=request.POST.get('age')
        emps.email_id=request.POST.get('email')
        emps.joindate=request.POST.get('joindate')
        emps.qualification=request.POST.get('qualification')
        emps.gender=request.POST.get('gender')
        emps.save()
        return redirect('showdetails')
    return render(request,'editpage.html')


#load deletepage..

def deletepage(request,pk):
    emps=employee.objects.get(id=pk)
    return render(request,'deletepage.html',{'emp':emps})

def delete_empdetails(request,pk):
    emp=employee.objects.get(id=pk)
    emp.delete()
    return redirect('showdetails')
