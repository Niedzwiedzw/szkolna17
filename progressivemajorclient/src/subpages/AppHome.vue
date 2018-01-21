<template>
  <div>




    <!-- Main Content -->
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <app-channel v-for="(channel, index) in channels" :key="channel.videos[0].id.videoId" :channel="channel"></app-channel>
        </div>
      </div>
      <div class="row">
        <p v-if="channels && channels[0]" class="copyright text-muted t-center"><strong>{{ channels[0].hits }}</strong> odwiedzin strony ugółem!</p>
      </div>
    </div>


  </div>
</template>

<script>
  import axios from '../axiosInstance'
  import AppMovie from '../components/AppMovie.vue'
  import AppChannel from '../components/AppChannel.vue'
  export default {
    name: 'AppHome',
    components: {
      AppMovie,
      AppChannel
    },
    data () {
      return {
        channels: []
      }
    },
    created () {
      axios.get('').then((response) => {
        this.channels = response.data
      })
      this.channels.sort((channel1, channel2) => {
        let date1 = new Date(channel1.videos[0].snippet.publishedAt)
        let date2 = new Date(channel2.videos[0].snippet.publishedAt)
        if (date1 < date2) return -1
        if (date1 > date2) return 1
        return 0
      })
    }
  }
</script>

<style scoped>
  .t-center {
    margin-left: auto;
    margin-right: auto;
  }
</style>
