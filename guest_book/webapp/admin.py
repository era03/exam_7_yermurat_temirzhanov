from django.contrib import admin
from webapp.models import GuestBook



class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'text', 'created_at', 'updated_at', 'status')
    list_filter = ('id', 'author', 'text', 'created_at', 'updated_at', 'status')
    search_fields = ('author', 'text', 'created_at', 'updated_at', 'status')
    fields = ('author', 'email', 'text', 'status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')



admin.site.register(GuestBook, GuestBookAdmin)