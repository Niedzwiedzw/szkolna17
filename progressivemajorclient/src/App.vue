<template>
  <div id="app">

    <!-- Bootstrap core CSS -->
    <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts for this template -->
    <link href="/static/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

    <!-- Custom styles for this template -->
    <link href="/static/css/clean-blog.min.css" rel="stylesheet">


    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <span class="navbar-brand hoverable" @click="$router.push('/')">NowyMajor.pl</span>
        <span class="pull-right hoverable menu-item" @click="$router.push('/')">Główna</span>
        <span class="pull-right hoverable menu-item" @click="$router.push('/live')">Lajty</span>
        <!--<button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">-->
        <!--Menu-->
        <!--<i class="fa fa-bars"></i>-->
        <!--</button>-->
        <!--<div class="collapse navbar-collapse" id="navbarResponsive">-->
        <!--<ul class="navbar-nav ml-auto">-->
        <!--<li class="nav-item">-->
        <!--<a class="nav-link" @click="$router.push('/')">Strona Główna</a>-->
        <!--</li>-->
        <!--<li class="nav-item">-->
        <!--<a class="nav-link" @click="$router.push('/')">Lajty boże</a>-->
        <!--</li>-->
        <!--<li class="nav-item">-->
        <!--<a class="nav-link" href="#">Sample Post</a>-->
        <!--</li>-->
        <!--<li class="nav-item">-->
        <!--<a class="nav-link" href="#">Contact</a>-->
        <!--</li>-->
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
    <router-view/>
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
  export default {
    name: 'App'
  }
</script>

<style>
  .hoverable {
    text-decoration: none;
    color: inherit;
    cursor: pointer;
  }

  .hoverable:hover {
    text-decoration: none;
    color: inherit;
    cursor: pointer;
    opacity: 0.6;
  }

  .menu-item {
    color: rgb(200, 200, 200);
  }

</style>
