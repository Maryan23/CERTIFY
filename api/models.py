from django.db import models
# from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models

# # Create your models here.
# class User(AbstractUser):
#     is_employer = models.BooleanField(default=False)

# class Employer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     company_name = models.CharField(max_length=50,null=True,blank = True)
#     prof_photo = CloudinaryField('image')
#     about = models.TextField(max_length=1000, blank=True, null=True)
#     contact = models.CharField(max_length=50, blank=True, null=True)

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

class Institution(models.Model):
    institution_reg_no = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=40)
    location_name = models.CharField(max_length=20)
    location_address = models.CharField(max_length=20)
    institution_email = models.EmailField()
    
    def save_institution(self):

class Employer(models.Model):
    company_logo = CloudinaryField('image')
    company_name = models.CharField(max_length=50)
    about = models.TextField(max_length=1000, blank=True)
    company_tel_number = models.IntegerField()
    company_email = models.EmailField()
    company_reg_number = models.CharField(max_length=20)
    joined_on = models.DateTimeField(auto_now_add=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)


class Institution(models.Model):
    institution_reg_no = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=40)
    location_name = models.CharField(max_length=20)
    location_address = models.CharField(max_length=20)
    institution_email = models.EmailField()

=======
    def save_employer(self):
        self.save()
    
    def delete_institution(self):
        self.delete()
    
    def __str__(self):
        return self.institution_name
    
class Learner(models.Model):
    learner_reg_no = models.CharField(max_length=30)
    learner_first_name = models.CharField(max_length=10)
    learner_second_name = models.CharField(max_length=10, blank=True)
    learner_last_name = models.CharField(max_length=10)
    course_taken = models.CharField(max_length=30)
    date_enrolled = models.DateTimeField()
    date_completed = models.DateTimeField()
    grade_attained = models.CharField(max_length=20)
    certificate_image = CloudinaryField('image')
    institution = models.ManyToManyField(Institution)
    def _str_(self):
        return self.learner_first_name 
    
    def save_learner(self):
        self.save()
    
    def delete_learner(self):
        self.delete()
    
    # @classmethod    
    # def view_learners_by_institution(cls, institution_search):
    #     learners_by_institution = cls.objects.filter(institution_search)
    #     return learners_by_institution
        
    def __str__(self):
        return self.learner_first_name
    
