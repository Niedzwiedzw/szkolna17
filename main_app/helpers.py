from main_app.models import YoutubeApiKey
import requests




def get_id_from_channel_name(channel_name):
    api_key = YoutubeApiKey.objects.first().value

    r = requests.get()
