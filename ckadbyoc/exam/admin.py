from django.contrib import admin

from .models import Questions



@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['name_short', 'category', 'question', 'submission_date', 'nscontext', 'context', 'workdir']