from django.contrib import admin

# Register your models here.
from .models import Problem, CompanyTag, CategoryTag

admin.site.register(Problem)
admin.site.register(CompanyTag)
admin.site.register(CategoryTag)
