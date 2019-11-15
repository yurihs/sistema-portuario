import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import AlterarUsuario from '@/components/usuarios/AlterarUsuario'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/usuarios/:id/alterar',
      name: 'AlterarUsuario',
      component: AlterarUsuario
    },
  ]
})
