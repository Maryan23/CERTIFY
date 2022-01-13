from django.shortcuts import redirect, render

from api.models import Institution, Learner
from api.forms import CreateLearnerForm, UpdateLearnerForm
from django.contrib import messages

#Create your views
def index(request):
  return render(request,'index.html')

def institution(request):
  # institution = Institution.filter_by_reg_no(reg_no)
  return render(request,'institution.html',{"institution":institution})

def learner(request, learner_id):
    current_user = request.user
    learner = Learner.objects.get(id=learner_id)
    learner = Learner.objects.filter(learner=learner)
    return render(request, 'intitution.html', {'current_user':current_user, 'institution':institution,'learner':learner})

def create_learner(request):
    if request.method == 'POST':
        create_learner_form = CreateLearnerForm(request.POST, request.FILES)
        if create_learner_form.is_valid():
            learner = create_learner_form.save(commit=False)
            learner.admin = request.user.profile
            learner.save()
            return redirect('home')
    else:
        create_learner_form = CreateLearnerForm()
    return render(request, 'newlearner.html', {'create_learner_form': create_learner_form})


def update_learner(request, learner_id):
    learner = Learner.objects.get(pk=learner_id)
    if request.method == 'POST':
        update_learner_form = UpdateLearnerForm(request.POST,request.FILES, instance=learner)
        if update_learner_form.is_valid():
            update_learner_form.save()
            messages.success(request, f'Learner updated!')
            return redirect('home')
    else:
        update_learner_form = UpdateLearnerForm(instance=learner)

    return render(request, 'update_learner.html', {"update_learner_form":update_learner_form})


def delete_learner(request,learner_id):
    current_user = request.user
    learner = Learner.objects.get(pk=learner_id)
    if learner:
        learner.delete_learner()
    return redirect('home')