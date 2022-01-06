from django.contrib import admin
from .models import Institution, Learner

# Register your models here.
admin.site.register(Institution)
admin.site.register(Learner)
from api.models import Employer

# Register your models here.
admin.site.register(Employer)