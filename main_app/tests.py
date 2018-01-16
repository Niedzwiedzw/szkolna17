from django.test import TestCase
from main_app import models

# Create your tests here.


class TestVideosAreFetchedProperly(TestCase):
    def test_videos_are_fetched(self):
        models.YoutubeApiKey.objects.create(value='AIzaSyAXUc2KuPmjEQPCTy8wA_JMYTasfOnrLkI')
        channel = models.YoutubeChannel.objects.create(example_video='https://www.youtube.com/watch?v=gDRt1rhaSCg')

        movies = channel.latest_videos
        self.assertFalse(channel.channel_id == '')
        print('channel_id: ', channel.channel_id)

        for movie in movies:
            self.assertEqual(channel.channel_id, movie['snippet']['channelId'])
