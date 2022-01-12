from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.lookups import In

# Create your models here.
class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default = False)


class Employer(models.Model):
    logo = CloudinaryField('logo')
    company_name = models.CharField(max_length=50)
    about = models.TextField(max_length=1000, blank=True)
    tel_number = models.IntegerField()
    email = models.EmailField()
    reg_number = models.CharField(max_length=20)
    joined_on = models.DateTimeField(auto_now_add=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def save_employer(self):
        self.save()
    
    def update_employer(self):
        self.save()
    
    def __str__(self):
        return self.company_name


class Institution(models.Model):
    reg_no = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=40)
    location = models.CharField(max_length=20)
    location_address = models.CharField(max_length=20)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    
    def save_institution(self):
        self.save()
    
    def delete_institution(self):
        self.delete()
    
    def __str__(self):
        return self.institution_name
    
    @classmethod
    def get_institution_by_name(cls, search_term):
        institution = cls.objects.filter(name__icontains=search_term)
        return institution

class Certificate(models.Model):
    cert_name = models.CharField(max_length=30,null=True)
    cert_image = CloudinaryField('cert_image')
    institution = models.ForeignKey(Institution, on_delete=CASCADE , null=True)

    def save_certificate(self):
        self.save()
    
    def delete_certificate(self):
        self.delete()
    
    def __str__(self):
        return self.cert_name

    
class Learner(models.Model):
    learner_image = CloudinaryField('learner_image')
    reg_no = models.CharField(max_length=30)
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10)
    course_taken = models.CharField(max_length=30)
    date_enrolled = models.DateTimeField()
    date_completed = models.DateTimeField()
    grade_attained = models.CharField(max_length=20)
    certificates = models.ForeignKey(Certificate , on_delete=CASCADE , null=True)
    institution = models.ForeignKey(Institution, on_delete=CASCADE , null=True)
    def _str_(self):
        return self.first_name 
    
    def save_learner(self):
        self.save()
    
    def delete_learner(self):
        self.delete()   
    
