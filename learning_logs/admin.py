from webbrowser import register

from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.site_header = "LEARNING_LOG ADMIN"
admin.site.site_title = "Learning_Log Admin area"
admin.site.index_title = "Welcome to the Learning_Log admin area"

admin.site.register(Topic)
admin.site.register(Entry)

