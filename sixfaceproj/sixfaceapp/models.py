from django.db import models
class Employee(models.Model):
	empname=  models.CharField(max_length=255)
	empId= models.CharField(max_length=255)
	empsal= models.CharField(max_length=255)
	empphoto=models.CharField(max_length=255)
	empdate=models.CharField(max_length=255)
	def __unicode__(self):
		return self.empname

class student(models.Model):
	student_name=models.CharField(max_length=255)
	student_sex=models.BooleanField(default=1)
	student_age=models.IntegerField()
	student_Date=models.DateField()
	student_photo=models.FileField(upload_to='upload_file')
	#  student email=email
	def __unicode__(self):
		return self.student_name    

# Create your models here.
