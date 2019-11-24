<template>
  <div>
    <h2>Usuário #{{ usuario.id }}</h2>
    <p><b>Email:</b> {{ usuario.email }}</p>
    <p><b>CPF:</b> {{ usuario.cpf }}</p>
    <v-row>
      <v-col cols="3">
        <v-btn color="blue" class="mr-4" :to="'/usuarios/'+usuario.id+'/alterar'">Alterar usuário</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ExibirUsuario',
  data() {
    return {
      usuario: [],
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/usuarios/'+ this.$route.params.id +'/')
      .then(response => {
        this.usuario = response.data;
      })
  }    
}
</script>

<style scoped>
  h2{
    margin-bottom: 40px;
  }
  p{
    font-size: 18px;
    margin: 20px 0;
  }
  v-btn, a{
    color: white !important;
  }
</style>