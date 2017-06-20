from django.contrib import admin
from .models import Resume, ContactInfo, Aboutme, OpenSourceProject, ContributedProject


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'entry_time', 'time_of_separation')

admin.site.register(Resume, ResumeAdmin)
admin.site.register(ContactInfo)
admin.site.register(Aboutme)
admin.site.register(OpenSourceProject)
admin.site.register(ContributedProject)
