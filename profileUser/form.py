from django import forms
from profileUser.models import ProfilePatient, ProfileDoctor, ProfileSettings
from django.contrib.auth.models import User


class CreateProfileSettings(forms.ModelForm):
    class Meta:
        model = ProfileSettings
        fields = [
            "profile",
        ]
        labels = {
            'profile': 'Perfil de usuário',
        }


class CreateProfileDoctor(forms.ModelForm):
    class Meta:
        model = ProfileDoctor
        fields = [
            "crm",
            "state_crm",
            "full_name",
        ]
        labels = {
            'crm': 'CRM',
            'state_crm': 'Estado do CRM',
            'full_name': 'Nome completo'
        }


class CreateProfilePatient(forms.ModelForm):
    class Meta:
        model = ProfilePatient
        fields = [
            "full_name",
        ]
        labels = {
            'full_name': 'Nome completo'
        }


class EditProfileDoctor(forms.ModelForm):
    class Meta:
        model = ProfileDoctor
        fields = [
            'crm',
            'state_crm',
            'full_name',
        ]


class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',

        ]
