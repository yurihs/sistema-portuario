import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'
import AlterarUsuario from '@/views/AlterarUsuario'
import AlterarEmpresa from '@/views/AlterarEmpresa'
import CadastrarUsuario from '@/views/CadastrarUsuario'
import CadastrarTiposCarga from '@/views/CadastrarTiposCarga'
import AlterarTiposCarga from '@/views/AlterarTiposCarga'
import AlterarPorto from '@/views/AlterarPorto'


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
      path: '/portos/:un_locode/alterar',
      name: 'AlterarPorto',
      component: AlterarPorto
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
