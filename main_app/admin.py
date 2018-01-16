from django.contrib import admin
from main_app import models

# Register your models here.


class YoutubeChannelAdmin(admin.ModelAdmin):
    pass


class YoutubeApiKeyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.YoutubeChannel, YoutubeChannelAdmin)
admin.site.register(models.YoutubeApiKey, YoutubeApiKeyAdmin)
