<template>
  <form>
    <v-row>
    <v-col cols="12" sm="6">
    <v-text-field
      name="CNPJ"
      v-model="cnpj"
      v-mask ="cnpjMask"
      v-validate="'required'"
      :error-messages="errors.first('CNPJ')"
      label="CNPJ"
    ></v-text-field>
    </v-col>
    </v-row>
    <v-row>
     <v-col>
        <v-text-field
          name="Razão Social"
          v-model="razao_social"
          v-validate="'required'"
          :error-messages="errors.first('Razão Social')"
          label="Razão Social"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          name="Nome Fantasia"
          v-model="nome_fantasia"
          v-validate="'required'"
          :error-messages="errors.first('Nome Fantasia')"
          label="Nome Fantasia"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field 
          name="Email" 
          v-model="email" 
          v-validate="'required|email'"
          :error-messages="errors.first('Email')"
          label="Email"
          :disabled="carregando"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-text-field 
          name="Telefone" 
          v-model="telefone"  
          v-mask="telefoneMask"
          v-validate="'required'"
          :error-messages="errors.first('Telefone')"
          label="Telefone"
          :disabled="carregando"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field
          name="Endereço"
          v-model="endereco"
          v-validate="'required'"
          :error-messages="errors.first('Endereço')"
          label="Endereço"
          :disabled="carregando"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="6">
        <v-text-field
          name="Cidade"
          v-model="cidade"
          v-validate="'required'"
          :error-messages="errors.first('Cidade')"
          label="Cidade"
          :disabled="carregando"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="4">
        <v-text-field
          name="Região"
          v-model="regiao"
          v-validate="'required'"
          :error-messages="errors.first('Região')"
          label="Região"
          :disabled="carregando"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="4">
        <v-text-field
          name="País"
          v-model="pais"
          v-validate="'required'"
          :error-messages="errors.first('País')"
          label="País"
          :disabled="carregando"
        ></v-text-field>
      </v-col>
    
      <v-col cols="12" sm="4">
        <v-text-field
          name="Codigo Postal"
          v-model="codigo_postal"
          v-mask="codigo_postalMask"
          v-validate="'required'"
          :error-messages="errors.first('Codigo Postal')"
          label="Codigo Postal"
          :disabled="carregando"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-btn class="mr-4" @click="submit" :disabled="carregando">Enviar</v-btn>
      </v-col>
      <v-col>
        <v-alert
          dense
          text
          :type="falha ? 'error' : 'success'"
          v-if="mensagem"
        >
          {{ mensagem }}
        </v-alert>  
      </v-col>
      
    </v-row>
  </form>
      
</template>

<script>
import { mask } from 'vue-the-mask';
import axios from 'axios';
// import Router from 'vue-router';
export default {
  name: 'CadastrarUsuario',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      carregando: true,
      falha: false,
      mensagem: '',
      
      // Campos formulario
      cnpj: '',
      razao_social: '',
      nome_fantasia: '',
      email: '',
      telefone: '',
      endereco: '',
      cidade: '',
      regiao: '',
      pais: '',
      codigo_postal: '',
      // Mascaras
      cnpjMask: '##.###.###/####-##',
      codigo_postalMask: '####-###',
      telefoneMask: '##(##) ####-####',
    }
  },
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.post('http://localhost:8000/api/empresas/', {
              cnpj: this.cnpj,
              razao_social: this.razao_social,
              nome_fantasia: this.nome_fantasia,
              email: this.email,
              telefone: this.telefone,
              endereco:{ 
              linha_1: this.endereco,
              cidade: this.cidade,
              regiao: this.regiao,
              pais: this.pais,
              codigo_postal: this.codigo_postal
              }
            })
            .then(() => {
              this.mensagem = "Cadastro realizado com sucesso.";
              this.falha = false;
              setTimeout( () => this.$router.push('Home'), 2000);
              
            })
            .catch(() => {
              this.falha = true;
              this.mensagem = "Houve um erro no processamento. Verifique os dados e tente novamente.";
            });
          }
      })
    }
  },
  mounted () {
    // Carrega grupos
    axios
      .get('http://localhost:8000/api/grupos/')
      .then(response => {
        this.grupos = response.data.map(function(grupo){
          return grupo.nome;
        });
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      })
      .finally(() => this.carregando = false)
  }
}
</script>

<style scoped>
</style>