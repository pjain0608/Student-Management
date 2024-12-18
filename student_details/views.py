from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from django.db.models import Q

details = Student.objects.all()  

def index(request):
    query = request.GET.get('search', '')
    if query:
        students = Student.objects.filter(
            Q(Name__icontains=query) | 
            Q(Company__icontains=query) | 
            Q(Skills__icontains=query)
        )
        # students = Student.objects.filter(Name__icontains=query)
    else:
        students = Student.objects.all()

    context = {
        'students':students    
        }
    return render(request,'index.html',context)

def pyspiders(request):
    
    context = {
        'students' : details
    }
    return render(request,'pyspiders.html',context)

def qspiders(request):
    
    context = {
        'students' : details
    }
    return render(request,'qspiders.html',context)

def jspiders(request):
    
    context = {
        'students' : details
    }
    return render(request,'jspiders.html',context)

def prospiders(request):
    context = {
        'students' : details
    }
    return render(request,'prospiders.html',context)

def student(request,pk):
    try:
        details1 = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponse("Student data not present", status=404) 
    if request.method == 'POST':
        details1.delete()
        return redirect('main')
    context = {
        'details1' : details1
    }
    return render(request,'student.html',context)

def edit(request,ab):
    data2 = Student.objects.get(id = ab)
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Qualification = request.POST.get('Qualification')
        Gender = request.POST.get('Gender')
        YOP = request.POST.get('YOP')
        Age = request.POST.get('Age')
        Skills = request.POST.get('Skills')
        # DOB = request.POST.get('DOB')
        Address = request.POST.get('Address')
        Mock_Rating = request.POST.get('Mock_Rating')
        Company = request.POST.get('Company')
        print(Name,Qualification,Gender,YOP,Age,Skills,Address,Mock_Rating,Company)
        data2.Name = Name
        data2.Qualification = Qualification
        data2.Gender = Gender
        data2.YOP = YOP
        data2.Age = Age
        data2.Skills = Skills
        # data2.DOB = DOB
        data2.Address = Address
        data2.Mock_Rating = Mock_Rating
        data2.Company = Company
        data2.save()
        print(Name,Qualification,Gender,YOP,Age,Skills,Address,Mock_Rating,Company)

        return redirect('main')

    context = {
        'data2' : data2
    }
    return render(request, 'edit.html', context)

def create(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Qualification = request.POST.get('Qualification')
        Gender = request.POST.get('Gender')
        YOP = request.POST.get('YOP')
        Age = request.POST.get('Age')
        Skills = request.POST.get('Skills')
        DOB = request.POST.get('DOB')
        Address = request.POST.get('Address')
        Mock_Rating = request.POST.get('Mock_Rating')
        Company = request.POST.get('Company')
        a = Student.objects.create(Name = Name, Qualification=Qualification, Gender=Gender, YOP=YOP,Age=Age,Skills=Skills,DOB=DOB,Address=Address,Mock_Rating=Mock_Rating,Company=Company)
        return redirect('main')
    return render(request,'create.html')