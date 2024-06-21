from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()

    def __str__(self):
        return self.dept_name

class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return f'Dr.{self.doc_name} - {self.doc_spec}'
    
class Booking(models.Model):
    pat_name = models.CharField(max_length=100)
    pat_email = models.EmailField(max_length=100)
    pat_phone = models.CharField(max_length=10)
    doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.pat_name




