<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="card" style="width: 100%; margin-top: 1rem; margin-bottom: 1rem;">
            <!--<iframe width="100%" height="auto"-->
            <!--:src="'https://www.youtube.com/watch?v=0o_bHOcIkLg'">-->
            <!--</iframe>-->
            <a href="https://www.youtube.com/watch?v=0o_bHOcIkLg">
              <img
                src="https://i.ytimg.com/vi/s89XI8tn2Ds/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCkEjcaBPvCh_ED4qlv1zwb7oWpHg"
                class="hoverable"
                style="width: 100%; margin-top: 1rem; margin-bottom: 1rem"
                alt="MEXICANO LIVE">
            </a>
            <div class="card-body">
              <a class="hoverable" :href="'https://www.youtube.com/watch?v=0o_bHOcIkLg'">
                <h4>LAJT MEXICANO</h4>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import AppMovie from '../components/AppMovie.vue'
  export default {
    name: 'AppLives',
    components: {
      AppMovie
    },
    data() {
      return {}
    }
  }
</script>

<style scoped>

</style>
