from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Employ_form
from .models import Employ_info

# def employee(request):
#     template = loader.get_template('home.html')
#     return HttpResponse(template.render())

def form_view (request):
    if request.method == 'Post':
        emp = Employ_form(request.POST)
        if emp.is_valid():
            #access data from hmtl
            e_id = emp.cleaned_data['emp_id']
            e_name = emp.cleaned_data['emp_name']
            e_desig = emp.cleaned_data['emp_desig']
            
            #adding data into database table
            employ_info = Employ_info(emp_id = e_id, emp_name = e_name, emp_desig = e_desig)
            employ_info.save()
            
            return redirect('success')
        else:
            print(emp.errors)
    else:
        emp = Employ_form()
        
    return render(request, 'home.html', {'emp':emp})

def success_view(request):
    return render(request, 'success.html')
