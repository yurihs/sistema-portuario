<template>
  <div>


    <h2>Empresa #{{ empresa.id }}</h2>
    <p><b>CNPJ:</b> {{ empresa.cnpj }}</p>
    <v-row>
        <v-col cols="6">
            <p><b>Nome Fantasia:</b> {{ empresa.nome_fantasia }}</p>
        </v-col>
        <v-col cols="6">
            <p><b>Razão Social:</b> {{ empresa.razao_social }}</p>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="6">
            <p><b>E-mail:</b> {{ empresa.email }}</p>
        </v-col>
        <v-col cols="6">
            <p><b>Telefone:</b> {{ empresa.telefone }}</p>
        </v-col>
    </v-row>
    <div v-if="empresa.endereco">
      <v-row>
          <v-col cols="6">
              <p><b>Logradouro:</b> {{ empresa.endereco.linha_1 }}</p>
          </v-col>
          <v-col cols="6">
              <p><b>Codigo Postal:</b> {{ empresa.endereco.codigo_postal }}</p>
          </v-col>
      </v-row>
      <v-row>
          <v-col cols="4">
              <p><b>Cidade:</b> {{ empresa.endereco.cidade }}</p>
          </v-col>
          <v-col cols="4">
              <p><b>Região:</b> {{ empresa.endereco.regiao }}</p>
          </v-col>
          <v-col cols="4">
              <p><b>País:</b> {{ empresa.endereco.pais }}</p>
          </v-col>
      </v-row>
    </div>

    
    
    
    

    
    <v-row>
      <v-col cols="3">
        <v-btn color="blue" class="mr-4" :to="'/empresas/'+empresa.id+'/alterar'">Alterar empresa</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ExibirEmpresa',
  data() {
    return {
      empresa: [],
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/empresas/'+ this.$route.params.id +'/')
      .then(response => {
        this.empresa = response.data;
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