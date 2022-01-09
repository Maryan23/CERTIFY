from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models


# class Employer(models.Model):
#     company_logo = CloudinaryField('image')
#     company_name = models.CharField(max_length=50)
#     about = models.TextField(max_length=1000, blank=True)
#     company_tel_number = models.IntegerField()
#     company_email = models.EmailField()
#     company_reg_number = models.CharField(max_length=20)
#     joined_on = models.DateTimeField(auto_now_add=True,null=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)


#     def __str__(self):
#         return self.company_name

#     def save_employer(self):
#         self.save()

#     def update_employer(self):
#         self.save()

#     @classmethod
#     def search_by_company_name(cls,search_term):
#         employer = cls.objects.filter(project_name__icontains=search_term)
#         return employer
