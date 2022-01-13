from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_learner = models.BooleanField(default = False)


class Employer(models.Model):
    logo = CloudinaryField('logo')
    company_name = models.CharField(max_length=50)
    about = models.TextField(max_length=1000)
    tel_number = models.IntegerField(null=True)
    email = models.EmailField()
    reg_number = models.CharField(max_length=20)
    joined_on = models.DateTimeField(auto_now_add=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def save_employer(self):
        self.save()
    
    def update_employer(self):
        self.save()
    
    def __str__(self):
        return self.user.username


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
        
    @classmethod
    def filter_by_reg_no(cls, reg_no):
        found_institution = cls.objects.filter(reg_no = reg_no)
        return found_institution
    
    def __str__(self):
        return self.user.username
    
    @classmethod
    def get_institution_by_name(cls, search_term):
        institution = cls.objects.filter(name__icontains=search_term)
        return institution

    @classmethod
    def filter_by_reg_no(cls, reg_no):
        found_institution = cls.objects.filter(reg_no = reg_no)
        return found_institution

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
    
    @classmethod
    def filter_by_id(cls, id):
        found_learner = cls.objects.filter(id = id)
        return found_learner
        
    def search_by_learner_name(cls, search_term):
        learner = cls.objects.filter(first_name__icontains=search_term)
        return learner
