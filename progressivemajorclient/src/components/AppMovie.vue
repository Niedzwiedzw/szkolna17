<template>
  <div class="card" style="width: 100%; margin-top: 1rem; margin-bottom: 1rem;">
    <iframe width="100%" height="auto"
            :src="'https://www.youtube.com/embed/' + video.id.videoId + '/'">
    </iframe>
    <div class="card-body">
      <a class="hoverable" :href="'https://www.youtube.com/watch?v=' + video.id.videoId">
        <h4>{{ video.snippet.title }}</h4>
      </a>
      <p class="card-text">wrzucony {{ moment(video.snippet.publishedAt, moment.HTML5_FMT.DATETIME_LOCAL_MS).fromNow() }}</p>
    </div>
  </div>
</template>

<script>
  import moment from 'moment'
  moment.locale('pl')
  export default {
    name: 'AppMovie',
    data () {
      return {}
    },
    beforeCreate () {
      this.moment = moment
    },
    props: ['video']
  }
</script>

<style scoped>

</style>
