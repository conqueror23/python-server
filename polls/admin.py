from django.contrib import admin

# Register your models here.
#after you may check in the admin page
from .models import Question
from .models import Choice

admin.site.register(Choice)
admin.site.register(Question)
