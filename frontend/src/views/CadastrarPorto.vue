<template>
  <form>
      <v-row>
     <v-col cols="12" sm="2">
        <v-text-field
          name="Unlocode"
          v-model="un_locode"
          v-validate="'required'"
          :error-messages="errors.first('Unlocode')"
          label="UN/LOCODE"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
     <v-col cols="12" sm="8">
        <v-text-field
          name="NomePorto"
          v-model="nomeporto"
          v-validate="'required'"
          :error-messages="errors.first('NomePorto')"
          label="Nome Porto"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4">
        <v-text-field
          name="CapacidadeTEU"
          v-model="capacidadeteu"
          v-validate="'required|integer'"
          :error-messages="errors.first('CapacidadeTEU')"
          label="TEU capacidade anual"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
    <v-col class="d-flex" cols="12" sm="6">
        <v-text-field
          name="Endereco" 
          v-model="endereco" 
          v-validate="'required'"
          :error-messages="errors.first('Endereco')"
          label="Endereço"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="6">
        <v-text-field
          name="Cidade" 
          v-model="cidade" 
          v-validate="'required'"
          :error-messages="errors.first('Cidade')"
          label="Cidade"
        ></v-text-field>
    </v-col>      
    </v-row>
    <v-row>
    <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Pais" 
          v-model="pais" 
          v-validate="'required'"
          :error-messages="errors.first('Pais')"
          label="País"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Regiao" 
          v-model="regiao" 
          v-validate="'required'"
          :error-messages="errors.first('Regiao')"
          label="Região"
        ></v-text-field>
    </v-col>    
    <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Codigopostal" 
          v-model="codigo_postal" 
          v-validate="'required'"
          :error-messages="errors.first('Codigopostal')"
          label="Código Postal"
        ></v-text-field>
    </v-col>   
    </v-row>   

    <v-row>
      <v-col cols="3">
        <v-btn class="mr-4" @click="submit" >Enviar</v-btn>
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
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'CadastrarPorto',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      portoAntigo: {},
      carregando: true,
      falha: false,
      mensagem: '',
      
      // Campos formulario
      un_locode: '',
      nomeporto: '',
      capacidadeteu: '',
      endereco: '',
      cidade: '',
      pais: '',
      codigo_postal: '',
      regiao: '',      

      // Mascaras
      //codigopostalMask: '#####-###',

    }
  },
  
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.post('http://localhost:8000/api/portos/',{
              un_locode: this.un_locode,
              nome: this.nomeporto,
              capacidade_teus_anuais: this.capacidadeteu,
              endereco: {
                cidade: this.cidade,
                pais: this.pais,
                codigo_postal: this.codigo_postal,
                regiao: this.regiao,
                linha_1: this.endereco
              }            
              
            })
            .then(() => {
              this.mensagem = "Cadastro realizado com sucesso.";
              this.falha = false;
              setTimeout( () => this.$router.push('Inicio'), 2000);
            })
            .catch(() => {
              this.falha = true;
              this.mensagem = "Houve um erro no processamento. Verifique os dados e tente novamente.";
            });
          }
      })
    },
  },    
  mounted () {
    this.$emit('message', 'Portos');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
  }
}

</script>

<style scoped>
</style>