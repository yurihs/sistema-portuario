import Vue from 'vue'
import Router from 'vue-router'

import Inicio from '@/views/Inicio'

import CadastrarUsuario from '@/views/CadastrarUsuario'
import AlterarUsuario from '@/views/AlterarUsuario'
import ListagemUsuarios from '@/views/ListagemUsuarios'

import AlterarEmpresa from '@/views/AlterarEmpresa'
import ExibirEmpresa from '@/views/ExibirEmpresa'

import AlterarPorto from '@/views/AlterarPorto'

import AlterarNavio from '@/views/AlterarNavio'
import ExibirNavio  from '@/views/ExibirNavio'

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
      path: '/navios/:numero_imo/alterar',
      name: 'AlterarNavio',
      component: AlterarNavio,
    },
    {
      path: '/navios/:numero_imo',
      name: 'ExibirNavio',
      component: ExibirNavio
    },
    
    {
      path: '/empresas/:id/alterar',
      name: 'AlterarEmpresa',
      component: AlterarEmpresa
    },
    {
      path: '/empresas/:id',
      name: 'ExibirEmpresa',
      component: ExibirEmpresa
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
