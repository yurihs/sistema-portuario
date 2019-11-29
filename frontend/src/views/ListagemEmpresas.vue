<template>
  <v-data-table
    :headers="headers"
    :items="empresas"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando empresas... Por favor aguarde"
  >
  <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" :to="'/empresas/cadastrar'">Nova Empresa</v-btn>
      </v-toolbar>
  </template>
    <template v-slot:item="{ item }"> 
      <router-link tag="tr" :to="'/empresas/'+item.id">
        <td>{{item.id}}</td>
        <td>{{item.nome_fantasia}}</td>  
        <td>{{item.cnpj}}</td>      
        <td>{{item.email}}</td>
        <td>{{item.telefone}}</td>
      </router-link>
    </template>
  </v-data-table>

</template>

<script>
import axios from 'axios';

export default {
  name: 'ListagemEmpresas',
  data(){
    return {
      empresas: [],
      headers: [
        {text: 'ID', value: 'id'},
        {text: 'Nome Fantasia', value: 'nome_fantasia'},
        {text: 'CNPJ', value: 'cnpj'},
        {text: 'Email', value: 'email'},
        {text: 'Telefone', value: 'telefone'},        
      ]
    }
  },
  mounted () {
    this.$emit('message', 'Empresas');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }

    axios
      .get('http://localhost:8000/api/empresas/')
      .then(response => {
        this.empresas = response.data;
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      });
  },
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