<template>
  <v-data-table
    :headers="headers"
    :items="usuarios"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando usuários... Por favor aguarde"
  >
  <template v-slot:top>
      <v-toolbar flat color="white">
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" :to="'/usuarios/cadastrar'">Novo usuário</v-btn>
      </v-toolbar>
  </template>
    <template v-slot:item="{ item }"> 
      <router-link tag="tr" :to="'/usuarios/'+item.id">
        <td>{{item.id}}</td>
        <td>{{item.email}}</td>
        <td>{{item.cpf}}</td>
      </router-link>
    </template>
  </v-data-table>

</template>

<script>
import axios from 'axios';

export default {
  name: 'ListagemUsuarios',
  data(){
    return {
      auth_token_access: localStorage.auth_token,

      usuarios: [],
      headers: [
        {text: 'ID', value: 'id'},
        {text: 'Email', value: 'email'},
        {text: 'CPF', value: 'cpf'}
      ]
    }
  },
  mounted () {
    this.$emit('message', 'Usuários');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }

    axios
      .get('http://localhost:8000/api/usuarios/', {
        headers: {
          Authorization: 'Bearer ' + this.auth_token_access
        }
      })
      .then(response => {
        this.usuarios = response.data;
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