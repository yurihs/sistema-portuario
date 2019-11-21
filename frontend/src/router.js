import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'
import AlterarUsuario from '@/views/AlterarUsuario'
import CadastrarUsuario from '@/views/CadastrarUsuario'
Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: Inicio
    },
    {
      path: '/usuarios/:id/alterar',
      name: 'AlterarUsuario',
      component: AlterarUsuario
    },
    {
      path: '/usuarios/cadastrar',
      name: 'CadastrarUsuario',
      component: CadastrarUsuario
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
