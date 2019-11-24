import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'
import AlterarUsuario from '@/views/AlterarUsuario'
import AlterarEmpresa from '@/views/AlterarEmpresa'
import CadastrarUsuario from '@/views/CadastrarUsuario'
import ListagemUsuarios from '@/views/ListagemUsuarios'

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
      path: '/usuarios',
      name: 'ListagemUsuarios',
      component: ListagemUsuarios
    },
    {
      path: '/usuarios/:id/alterar',
      name: 'AlterarUsuario',
      component: AlterarUsuario
    },
    {
      path: '/empresas/:id/alterar',
      name: 'AlterarEmpresa',
      component: AlterarEmpresa
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
