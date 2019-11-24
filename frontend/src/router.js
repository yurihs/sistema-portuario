import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'

import CadastrarUsuario from '@/views/CadastrarUsuario'
import AlterarUsuario from '@/views/AlterarUsuario'
import ListagemUsuarios from '@/views/ListagemUsuarios'

import AlterarEmpresa from '@/views/AlterarEmpresa'

import CadastrarTiposCarga from '@/views/CadastrarTiposCarga'
import AlterarTiposCarga from '@/views/AlterarTiposCarga'

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
      path: '/tipos-carga/cadastrar',
      name: 'CadastrarTiposCargas',
      component: CadastrarTiposCarga
    },
    {
      path: '/tipos-carga/:id/alterar',
      name: 'AlterarTiposCarga',
      component: AlterarTiposCarga
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
