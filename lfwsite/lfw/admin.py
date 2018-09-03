from django.contrib import admin
from .models import Jobapp, Company, Resume, Coverletter

admin.site.register(Jobapp)
admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(Coverletter)

# Register your models here.