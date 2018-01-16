<template>
  <div class="container">
    <transition>
      <div class="row">
        <div class="col-xs-12 col-md-5">
          <h2 class="hoverable channel-title" @click="toggleShow()">{{ channel.name }} <i class="fa fa-arrow-down fa-2x"></i></h2>
        </div>
        <div class="col-xs-12 col-md-7">
          <span class="text-small">ostatni film: {{ moment(channel.videos[0].snippet.publishedAt, moment.HTML5_FMT.DATETIME_LOCAL_MS).fromNow() }}</span>
        </div>
      </div>
    </transition>
    <div v-if="show" class="container">
      <div v-for="(video, index) in channel.videos" :key="index" class="container">
        <app-movie :video="video"></app-movie>
      </div>
    </div>
  </div>
</template>

<script>
  import AppMovie from './AppMovie.vue'
  import moment from 'moment'
  moment.locale('pl')
  export default {
    name: 'AppChannel',
    components: {
      AppMovie
    },
    data () {
      return {
        show: false
      }
    },
    methods: {
      toggleShow () {
        this.show = !this.show
      }
    },
    beforeCreate () {
      this.moment = moment
    },
    props: ['channel']
  }
</script>

<style scoped>
  .text-small {
    font-size: 70%;
  }
  .channel-title {
    vertical-align: middle;
  }
</style>
