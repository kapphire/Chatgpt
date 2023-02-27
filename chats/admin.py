from django.contrib import admin

from chats.models import Session, Chat


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
