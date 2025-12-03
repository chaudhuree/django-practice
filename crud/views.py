from django.shortcuts import render
from employees.models import Employee
# def home(request):
#     return HttpResponse("<h2>Home</h2>")

def home(request):
    employees = Employee.objects.all()
    context={"employees":employees}
    return render(request,"home.html",context)
