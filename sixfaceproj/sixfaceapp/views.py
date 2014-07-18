from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from sixfaceapp.models import * 
from sixfaceapp.forms import Employeeform,Studentform


def home(request):
	a=1
	b=2
	c= a + b
	return render (request,'sixface1.html',locals())
def circle(request):

	if request.POST:
		r=request.POST.get('radious')
		pi=3.17
		A=pi*int(r)*int(r) 	
	return render (request,'sixface2.html',locals())
def employee_details(request):
	empform=Employeeform()
	if request.POST:
		empname=request.POST.get('Employee_Name')
		empId=request.POST.get('Employee_Id')
		empsal=request.POST.get('Employee_Salary')
		empdate=request.POST.get('Employee_Date')
		empphoto=request.POST.get('Employee_Photo')
		a=Employee(empname=empname,empId=empId,empsal=empsal,empdate=empdate,empphoto=empphoto)
		a.save()
		view1=Employee.objects.all()

		return render(request,'sixfaceview.html',locals())
	return render (request,'sixface3.html',locals())
def student_details(request):
	form = Studentform()
	if request.POST:
		# import ipdb
		# ipdb.set_trace()
		student_name=request.POST.get('student_name')
		#student_file=request.FILES[student_file]
		student_sex=request.POST.get('student_sex')
		student_age=request.POST.get('student_age')
		student_Date=request.POST.get('student_Date')
		student_photo=request.FILES['student_photo']
		#student_email=request.post.get('student_email')
		a=student(student_name=student_name,student_sex=student_sex,student_age=student_age,student_Date=student_Date,student_photo=student_photo)
		a.save()
	# import ipdb
	# ipdb.set_trace()	
	studview=student.objects.all()

	return render (request,'studentview.html',locals())
def sixfacefn (request):
	fn1=Employeeform()

	return render (request,'sixface5.html',locals())

def sixfaceview (request):
	# import ipdb
	# ipdb.set_trace()
	view1=Employee.objects.all()

	return render (request,'sixfaceview.html',locals())
def firstpage (request):

	return render (request,'sixface1.html',locals())


