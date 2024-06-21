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
        return self.doc_name





