from django.shortcuts import render

from django.apps import apps

from .forms import UserRegisterForm
from .models import Profile


def dashboard(request):
    """
    A login redirect view
    :param request:
    :return:
    """
    total_staff = Profile.objects.count()
    standard_model = apps.get_model('school', 'Standard')
    total_standard = standard_model.objects.count()
    student_model = apps.get_model('school.Student')
    total_student = student_model.objects.count()
    return render(request, 'account/dashboard.html', {
        'section': 'Dashboard',
        'total_staff': total_staff,
        'total_standard': total_standard,
        # 'total_student': total_student
    })


def staff_register(request):
    """
    Signs up to this site
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            # create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'registration/registraion_done.html', {'new_user': new_user})
        else:
            user_form = UserRegisterForm()
            return render(request, 'registration/register.html', {'user_form': user_form})

