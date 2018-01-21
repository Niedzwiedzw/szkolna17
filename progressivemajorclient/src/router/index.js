import Vue from 'vue'
import Router from 'vue-router'
import AppHome from '../subpages/AppHome.vue'
import AppLives from '../subpages/AppLives.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AppHome',
      component: AppHome
    },
    {
      path: '/live',
      name: 'AppLives',
      component: AppLives
    }
  ]
})
