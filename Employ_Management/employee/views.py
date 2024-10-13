from django.shortcuts import render,redirect
from .forms import Employ_form
from .models import Djemployee

def form_view (request):
    if request.method == "POST":
        emp = Employ_form(request.POST)
        if emp.is_valid():
            #access data from hmtl
            e_id = emp.cleaned_data['emp_id']
            e_name = emp.cleaned_data['emp_name']
            e_desig = emp.cleaned_data['emp_desig']
            
            #adding data into database table
            djemployee = Djemployee(emp_id = e_id, emp_name = e_name, emp_desig = e_desig)
            djemployee.save()
            
            return redirect('success')
        else:
            print("Form errors: ",emp.errors)
    else:
        emp = Employ_form()
        
    return render(request, 'home.html', {'emp':emp})

def success_view(request):
    return render(request, 'success.html')
