<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand" href="#">NowyMajor.pl</a>
        <!--<button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">-->
          <!--Menu-->
          <!--<i class="fa fa-bars"></i>-->
        <!--</button>-->
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <!--<li class="nav-item">-->
              <!--<a class="nav-link" href="#">Strona Główna</a>-->
            <!--</li>-->
            <!--<li class="nav-item">-->
            <!--<a class="nav-link" href="#">About</a>-->
            <!--</li>-->
            <!--<li class="nav-item">-->
            <!--<a class="nav-link" href="#">Sample Post</a>-->
            <!--</li>-->
            <!--<li class="nav-item">-->
            <!--<a class="nav-link" href="#">Contact</a>-->
            <!--</li>-->
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Header -->
    <header class="masthead" style="background-image: url('/static/img/home-bg.jpg')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="site-heading">
              <h1>Szkolna 17</h1>
              <span class="subheading">Najnowsze filmiki zawsze rychło w czas.</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <app-channel v-for="(channel, index) in channels" :key="channel.videos[0].id.videoId" :channel="channel"></app-channel>
        </div>
      </div>
    </div>

    <hr>

    <!-- Footer -->
    <footer>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <ul class="list-inline text-center">
              <li class="list-inline-item">
                <a href="https://www.facebook.com/groups/314687479014489/" target="_blank">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x"></i>
                    <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                  </span>
                </a>
              </li>
            </ul>
            <p class="copyright text-muted">Copyright &copy; nowymajor.pl 2018</p>
          </div>
        </div>
      </div>
    </footer>
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

</style>
