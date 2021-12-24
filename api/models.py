from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_employer = models.BooleanField(default=False)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=50,null=True,blank = True)
    prof_photo = CloudinaryField('image')
    about = models.TextField(max_length=1000, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name

    def save_employer(self):
        self.save()

    def update_employer(self):
        self.save()

    @classmethod
    def search_by_company_name(cls,search_term):
        employer = cls.objects.filter(project_name__icontains=search_term)
        return employer
