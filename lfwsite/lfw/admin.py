from django.contrib import admin
from .models import Jobapp, Company, Resume, Coverletter, Skill

admin.site.register(Jobapp)
admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(Coverletter)
admin.site.register(Skill)

# Register your models here.
