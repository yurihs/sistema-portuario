<template>
  <v-data-table
    :headers="headers"
    :items="navios"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando navios... Por favor aguarde"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" :to="'/navios/cadastrar'">Novo navio</v-btn>
      </v-toolbar>
  </template>

    <template v-slot:item="{ item }"> 
      <router-link tag="tr" :to="'navios/'+item.id+'/alterar'">
        <td>{{item.numero_imo}}</td>
        <td>{{item.nome}}</td>
        <td>{{item.comprimento_metros}}</td>
        <td>{{item.largura_metros}}</td>
        <td>{{item.numero_de_tripulantes}}</td>
        <td>{{item.porte_bruto_toneladas}}</td>
        <td>{{item.empresa.nome_fantasia}}</td>
        <td>{{item.estado_bandeira}}</td>
      </router-link>
    </template>
  </v-data-table>

</template>

<script>
import axios from 'axios';

export default {
  name: 'ListagemNavios',
  data(){
    return {
      navios: [],
      headers: [
        {text: 'Número IMO', value: 'numero_imo'},
        {text: 'Nome', value: 'nome'},
        {text: 'Comprimento', value: 'comprimento_metros'},
        {text: 'Largura', value: 'largura_metros'},
        {text: 'Número de Tripulantes', value: 'numero_de_tripulantes'},
        {text: 'Porte Bruto', value: 'porte_bruto_toneladas'},
        {text: 'Empresa', value: 'empresa'},
        {text: 'CPF', value: 'estado_bandeira'}
      ]
    }
  },
  mounted () {
    this.$emit('message', 'Navios');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
    axios
      .get('http://localhost:8000/api/navios/')
      .then(response => {
        this.navios = response.data;
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      })
  }
}
</script>

<style scoped>
  tr {
    cursor: pointer;
  }
    v-btn, a{
    color: white !important;
  }
</style>