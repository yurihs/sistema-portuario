import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/views/Login'

import Inicio from '@/views/Inicio'

import CadastrarUsuario from '@/views/CadastrarUsuario'
import AlterarUsuario from '@/views/AlterarUsuario'
import ListagemUsuarios from '@/views/ListagemUsuarios'
import ExibirUsuario from '@/views/ExibirUsuario'

import CadastrarEmpresa from '@/views/CadastrarEmpresa'
import AlterarEmpresa from '@/views/AlterarEmpresa'
import ExibirEmpresa from '@/views/ExibirEmpresa'
import ListagemEmpresas from '@/views/ListagemEmpresas'

import CadastrarTiposCarga from '@/views/CadastrarTiposCarga'
import AlterarTiposCarga from '@/views/AlterarTiposCarga'
import ListagemTiposCarga from '@/views/ListagemTiposCarga'

import AlterarPorto from '@/views/AlterarPorto'
import CadastrarPorto from '@/views/CadastrarPorto'

import AlterarNavio from '@/views/AlterarNavio'
import ExibirNavio  from '@/views/ExibirNavio'

import AlterarNavio from '@/views/AlterarNavio'
import CadastrarNavio from '@/views/CadastrarNavio'
import ListagemNavio from '@/views/ListagemNavio'


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
      path: '/login',
      name: 'Login',
      component: Login
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
      path: '/navios/',
      name: 'ListagemNavio',
      component: ListagemNavio,
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

    {
      path: '/empresas/cadastrar',
      name: 'CadastrarEmpresa',
      component: CadastrarEmpresa
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
      path: '/empresas',
      name: 'ListagemEmpresas',
      component: ListagemEmpresas
    },
    
    {
      path: '/tipos-carga/cadastrar',
      name: 'CadastrarTiposCarga',
      component: CadastrarTiposCarga
    },

    {
      path: '/tipos-carga',
      name: 'ListagemTiposCarga',
      component: ListagemTiposCarga
    },
    
    {
      path: '/tipos-carga/:id/alterar',
      name: 'AlterarTiposCarga',
      component: AlterarTiposCarga
    },
    

    {
      path: '/navios/cadastrar',
      name: 'CadastrarNavio',
      component: CadastrarNavio
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
