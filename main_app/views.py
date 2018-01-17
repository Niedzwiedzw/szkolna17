from django.shortcuts import render
from main_app.models import YoutubeChannel


from django.http import JsonResponse


def index(request):
    channels = []
    for channel in YoutubeChannel.objects.all():
        channels.append({'name': channel.name,
                         'videos': channel.latest_videos})

    channels.sort(key=lambda x: x['videos'][0]['snippet']['publishedAt'], reverse=True)
    return JsonResponse(data=channels, safe=False)
