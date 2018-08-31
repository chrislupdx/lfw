from django.contrib import admin
from .models import Jobapp, Company, Resume, CoverLetter

admin.site.register(Jobapp)
admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(CoverLetter)

# Register your models here.