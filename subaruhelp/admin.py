from django.contrib import admin
from .models import ObdCode, Comment


@admin.register(ObdCode)
class ObdCodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'obd_code', 'pub_date', 'car_model',)
