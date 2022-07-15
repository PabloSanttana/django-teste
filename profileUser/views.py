from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import ProfileDoctor, ProfilePatient, ProfileSettings
from .form import CreateProfileSettings, CreateProfileDoctor, CreateProfilePatient, EditProfileDoctor, UserEdit
from django.views import View
from django.contrib.auth.models import User

# Create your views here.


@login_required()
def home(request):
    verify = ProfileSettings.objects.filter(
        user__email=request.user.email).first()
    if verify:
        if verify.profile == 'Paciente':
            return redirect('profile:patinet')
        else:
            return redirect('profile:doctor')

    register_form_data = request.session.get("profile_form_data", None)
    form = CreateProfileSettings(register_form_data)
    return render(request, 'profileUser/pages/home.html', context={
        'form': form,
    })


@login_required()
def profile_validation(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['profile_form_data'] = POST
    form = CreateProfileSettings(POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        request.session.pop('profile_form_data')
        profile = POST.get('profile')
        if profile == 'Paciente':
            return redirect('profile:patinet')
        else:
            return redirect('profile:doctor')
    return redirect('profile:home')


@login_required()
def profile_Doctor(request):
    verify = ProfileSettings.objects.filter(
        user__email=request.user.email).first()
    if verify.profile == 'Paciente':
        return redirect('profile:patinet')
    verify = ProfileDoctor.objects.filter(
        user__email=request.user.email).first()
    if verify:
        return redirect('monitoring:home')

    doctor_form_data = request.session.get("doctor_form_data", None)
    form = CreateProfileDoctor(doctor_form_data)
    return render(request, 'profileUser/pages/doctor.html', context={
        'form': form,
    })


@login_required()
def profile_Doctor_validation(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session["doctor_form_data"] = POST
    form = CreateProfileDoctor(POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        request.session.pop('doctor_form_data')
        return redirect('monitoring:home')
    return redirect('profile:doctor')


@login_required()
def profile_Patinet(request):
    verify = ProfileSettings.objects.filter(
        user__email=request.user.email).first()
    if verify.profile != 'Paciente':
        return redirect('profile:doctor')
    verify = ProfilePatient.objects.filter(
        user__email=request.user.email).first()
    if verify:
        return redirect('monitoring:home')

    patient_form_data = request.session.get("patient_form_data", None)
    form = CreateProfilePatient(patient_form_data)
    return render(request, 'profileUser/pages/patient.html', context={
        'form': form,
    })


@login_required()
def profile_Patinet_validation(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['patient_form_data'] = POST
    form = CreateProfilePatient(POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        request.session.pop('patient_form_data')
        return redirect('monitoring:home')
    return redirect('profile:patinet')


@login_required()
def Profile_User(request):
    user_profile = ProfileDoctor.objects.get(user=request.user)
    form = EditProfileDoctor(request.POST or None,
                             instance=user_profile)
    form1 = UserEdit(request.POST or None,
                     instance=request.user)

    return render(request, 'profileUser/pages/data.html', context={
        'form': form,
        'form1': form1
    })
