import Vue from 'vue'
import Router from 'vue-router'

// const AlterarUsuario = () => import('@/views/AlterarUsuario')

import AlterarUsuario from '@/views/AlterarUsuario'
import AlterarNavio from '@/views/AlterarNavio'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/usuarios/:id/alterar',
      name: 'AlterarUsuario',
      component: AlterarUsuario
    },
    {
      path: '/navios/:numero_imo/alterar',
      name: 'AlterarNavio',
      component: AlterarNavio
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
