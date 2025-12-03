from employees.models import Employee
from django.http import Http404,HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.
def employee_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    # return HttpResponse(employee)
    context = {"employee":employee}
    return render(request,"employee_detail.html",context)
    