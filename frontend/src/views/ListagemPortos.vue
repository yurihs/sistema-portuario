<template>
  <v-data-table
    :headers="headers"
    :items="portos"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando portos... Por favor aguarde"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" :to="'/portos/cadastrar'">Novo porto</v-btn>
      </v-toolbar>
  </template>

    <template v-slot:item="{ item }"> 
      <router-link tag="tr" :to="'portos/'+item.un_locode+'/alterar'">
        <td>{{item.un_locode}}</td>
        <td>{{item.nome}}</td>
        <td>{{item.capacidade_teus_anuais}}</td>
        <td>{{item.endereco.cidade}}</td>
      </router-link>
    </template>
  </v-data-table>

</template>                  

<script>
import axios from 'axios';

export default {
  name: 'ListagemPortos',
  data(){
    return {
      portos: [],
      headers: [
        {text: 'Número LOCODE', value: 'un_locode'},
        {text: 'Nome', value: 'nome'},
        {text: 'Capacidade em TEUs anuais', value: 'capacidade_teus_anuais'},
        {text: 'Endereco', value: 'endereco'}
      ]
    }
  },
  mounted () {

    this.$emit('message', 'Portos');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }

    axios
      .get('http://localhost:8000/api/portos/')
      .then(response => {
        this.portos = response.data;
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