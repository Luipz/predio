import Vue from 'vue'
import VueRouter from 'vue-router'
import predioa from '@/components/predioas'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/predioas/lista',
    name: 'predioa',
    component: predioa
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})

export default router
