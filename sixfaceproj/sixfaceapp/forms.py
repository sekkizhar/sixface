from django import forms
from sixfaceapp.models import Employee,student
class Employeeform(forms.ModelForm):
	class Meta:
		model=Employee
		#title = forms.CharField(required=True)
class Studentform(forms.ModelForm):
 	class Meta:
 		model =student