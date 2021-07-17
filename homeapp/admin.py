from django.contrib import admin

from .models import Message, Userprofile, Activitylog
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message','senderdevice', 'senderos', 'senderosversion',
                    'senderbrowser', 'senderbrowserversion', 'created_at']
    list_display_links = ['id', 'user']

    readonly_fields = ['created_at']


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['user','userdevice', 'useros', 'userosversion',
                    'userbrowser', 'userbrowserversion', 'created_at']


class ActivitylogAdmin(admin.ModelAdmin):
    readonly_fields = ['activity']
    list_display = ['user', 'activity', 'message', 'reflink', 'created_at']
    search_fields = ['message', 'activity']


admin.site.register(Userprofile, UserprofileAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Activitylog, ActivitylogAdmin)
