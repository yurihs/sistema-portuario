<template>
  <v-data-table
    :headers="headers"
    :items="tipos_carga"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando Tipos de Carga... Por favor aguarde"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" :to="'/tipos-carga/cadastrar'">Novo Tipo de Carga</v-btn>
      </v-toolbar>
  </template>

    <template v-slot:item="{ item }"> 
      <router-link tag="tr" :to="'/tipos-carga/'+item.id+'/alterar'">
        <td>{{item.id}}</td>
        <td>{{item.nome}}</td>
        <td>{{item.unidade}}</td>
      </router-link>
    </template>
  </v-data-table>

</template>

<script>
import axios from 'axios';

export default {
  name: 'ListagemTiposCarga',
  data(){
    return {
      tipos_carga: [],
      headers: [
        {text: 'ID', value: 'id'},
        {text: 'Tipo de Carga', value: 'tipo_carga'},
        {text: 'Unidade', value: 'nome'},
      ]
    }
  },
 mounted () {
    this.$emit('message', 'Tipos de Cargas');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }

    axios
      .get('http://localhost:8000/api/tipos-carga/')
      .then(response => {
        this.tipos_carga = response.data;
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