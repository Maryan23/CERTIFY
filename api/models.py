from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.deletion import CASCADE
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.

class User(AbstractUser):
    is_institution = models.BooleanField(default=False)
    

class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    institution_reg_no = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=40)
    location_name = models.CharField(max_length=20)
    location_address = models.CharField(max_length=20)
    institution_email = models.EmailField()
    
    def save_institution(self):
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
    institution = models.ForeignKey(Institution, on_delete=CASCADE)
    
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
    