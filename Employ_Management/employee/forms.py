from django import forms

class Employ_form(forms.Form):
    
    emp_id = forms.IntegerField()
    emp_name = forms.CharField(max_length = 50)
    emp_desig = forms.CharField(max_length = 50)