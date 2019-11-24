<template>
  <v-data-table
    :headers="headers"
    :items="usuarios"
    :items-per-page="5"
    class="elevation-1"
    loading-text="Carregando usuários... Por favor aguarde"
  >
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
      usuarios: [],
      headers: [
        {text: 'ID', value: 'id'},
        {text: 'Email', value: 'email'},
        {text: 'CPF', value: 'cpf'}
      ]
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000/api/usuarios/')
      .then(response => {
        this.usuarios = response.data;
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
</style>