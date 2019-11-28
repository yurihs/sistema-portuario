import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'

import CadastrarUsuario from '@/views/CadastrarUsuario'
import AlterarUsuario from '@/views/AlterarUsuario'
import ListagemUsuarios from '@/views/ListagemUsuarios'
import ExibirUsuario from '@/views/ExibirUsuario'

import AlterarEmpresa from '@/views/AlterarEmpresa'

import CadastrarTiposCarga from '@/views/CadastrarTiposCarga'
import AlterarTiposCarga from '@/views/AlterarTiposCarga'

import AlterarPorto from '@/views/AlterarPorto'
import CadastrarPorto from '@/views/CadastrarPorto'


import AlterarNavio from '@/views/AlterarNavio'



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
      path: '/usuarios/cadastrar',
      name: 'CadastrarUsuario',
      component: CadastrarUsuario
    },
    
    {
      path: '/usuarios/:id',
      name: 'ExibirUsuario',
      component: ExibirUsuario
    },

    {
      path: '/usuarios/:id/alterar',
      name: 'AlterarUsuario',
      component: AlterarUsuario
    },
    
    {
      path: '/navios/:numero_imo/alterar',
      name: 'AlterarNavio',
      component: AlterarNavio,
    },
    
    {
      path: '/empresas/:id/alterar',
      name: 'AlterarEmpresa',
      component: AlterarEmpresa
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
      path: '/portos/cadastrar',
      name: 'CadastrarPorto',
      component: CadastrarPorto
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
