from django.contrib import admin
from .models import post,category,AboutUS,chatbot
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display=("title","content")
    search_fields=("title","content")
    list_filter=("category","created_at")

admin.site.register(post,postAdmin)
admin.site.register(category)
admin.site.register(AboutUS)
admin.site.register(chatbot)











