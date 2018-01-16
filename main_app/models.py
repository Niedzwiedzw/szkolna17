from django.db import models

import requests


class YoutubeChannel(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    channel_id = models.CharField(max_length=256, null=True, blank=True)
    example_video = models.CharField(max_length=256)

    def get_channel_info(self):
        """
        example video is having it's id retrieved from the url,
        then data is fetched from API

        'https://www.youtube.com/watch?v=xfZZLSWbY3g' -> 'xfZZLSWbY3g'
        :return: <str> channel_id
        """

        video_id = self.example_video.split('?v=')[1]

        params = {
            'part': 'snippet',
            'id': video_id,
            'key': YoutubeApiKey.objects.first().value
        }
        r = requests.get('https://www.googleapis.com/youtube/v3/videos',
                         params=params).json()['items'][0]

        return r['snippet']

    def update(self):
        video_snippet = self.get_channel_info()
        self.channel_id = video_snippet['channelId']
        self.name = video_snippet['channelTitle']
        print(f'{self.name} added.')

        self.save()

    @property
    def latest_videos(self):
        if self.channel_id is None:
            self.update()

        params = {
            'part': 'snippet',
            'channelId': self.channel_id,
            'key': YoutubeApiKey.objects.first().value,
            'order': 'date',
            'maxResults': '10'
        }
        r = requests.get('https://www.googleapis.com/youtube/v3/search',
                         params=params)

        return r.json()['items']


class YoutubeApiKey(models.Model):
    value = models.CharField(max_length=512)
