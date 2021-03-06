import Vue from 'vue'
import VueRouter from 'vue-router'
import predioa from '@/components/predioa'
import agregar from '@/components/agregar'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/predioas/lista',
    name: 'predioa',
    component: predioa
  },
  {
    path: '/predioas/agregar',
    name: 'agregar',
    component: agregar
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})

export default router
