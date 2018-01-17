from main_app.models import SiteEntries
from main_app.models import YoutubeChannel


from django.http import JsonResponse


def index(request):
    channels = []
    SiteEntries.hit()
    amount_of_hits = SiteEntries.get_amount()
    for channel in YoutubeChannel.objects.all():
        channels.append({'name': channel.name,
                         'videos': channel.latest_videos,
                         'hits': amount_of_hits})

    channels.sort(key=lambda x: x['videos'][0]['snippet']['publishedAt'], reverse=True)

    return JsonResponse(data=channels, safe=False)
