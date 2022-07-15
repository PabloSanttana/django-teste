from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileSettings(models.Model):
    PACIENTE = 'Paciente'
    MEDICO = 'Médico'
    DEFAULT = ""
    profile = [
        (DEFAULT, ''),
        (PACIENTE, 'Paciente'),
        (MEDICO, 'Médico'),


    ]
    profile = models.CharField(
        max_length=255,
        choices=profile,
        default=DEFAULT,

    )
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='profile')


class ProfileDoctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='profileDoctor')
    is_Homologated = models.BooleanField(default=False)
    crm = models.CharField(max_length=6, unique=True)
    state_crm = models.CharField(max_length=2)
    full_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class ProfilePatient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='profilePatient')
    is_Homologated = models.BooleanField(default=False)
    full_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
