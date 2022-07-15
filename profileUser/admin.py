from django.contrib import admin
from profileUser.models import ProfileDoctor, ProfileSettings, ProfilePatient

# Register your models here.


@admin.register(ProfileDoctor)
class ProfileDoctorAdmin(admin.ModelAdmin):
    ...


@admin.register(ProfileSettings)
class ProfileSettingsAdmin(admin.ModelAdmin):
    ...


@admin.register(ProfilePatient)
class ProfilePatientAdmin(admin.ModelAdmin):
    ...
