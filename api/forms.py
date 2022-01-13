from django import forms
from .models import Learner

class CreateLearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = ['learner_image','reg_no','first_name','second_name','last_name','course_taken','date_enrolled','date_completed','grade_attained','certificates','institution']


class UpdateLearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = ['learner_image','reg_no','first_name','second_name','last_name','course_taken','date_enrolled','date_completed','grade_attained','certificates','institution']
