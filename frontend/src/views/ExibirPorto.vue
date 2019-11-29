<template>
  <div>
    <h2>Número LOCODE #{{ porto.un_locode }}</h2>
    <p><b>Nome:</b> {{ porto.nome }}</p>
    <p><b>Capacidade em TEUs anuais:</b> {{ porto.capacidade_teus_anuais }}</p>
    <p><b>Cidade:</b> {{ porto.endereco.cidade }}</p>
    <v-row>
      <v-col cols="3">
        <v-btn color="blue" class="mr-4" :to="'/portos/'+porto.un_locode+'/alterar'">Alterar porto</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ExibirPorto',
  data() {
    return {
      porto: [],
    }
  },
  mounted () {
    this.$emit('message', 'Portos');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }

    axios.get('http://localhost:8000/api/portos/'+ this.$route.params.id +'/')
      .then(response => {
        this.porto = response.data;
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