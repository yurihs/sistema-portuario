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
          :disabled="carregando || desabilitar_campose"
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
          :disabled="carregando || desabilitar_campose"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4">
        <v-text-field
          name="CapacidadeTEU"
          v-model="capacidadeteu"
          v-validate="'required|integer'"
          :error-messages="errors.first('CapacidadeTEU')"
          label="TEU capacidade anual"
          :disabled="carregando || desabilitar_campose"
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
          :disabled="carregando || desabilitar_campose"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="6">
        <v-text-field
          name="Cidade" 
          v-model="cidade" 
          v-validate="'required'"
          :error-messages="errors.first('Cidade')"
          label="Cidade"
          :disabled="carregando || desabilitar_campose"
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
          :disabled="carregando || desabilitar_campose"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Regiao" 
          v-model="regiao" 
          v-validate="'required'"
          :error-messages="errors.first('Regiao')"
          label="Região"
          :disabled="carregando || desabilitar_campose"
        ></v-text-field>
    </v-col>    
    <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Codigopostal" 
          v-model="codigo_postal" 
          v-validate="'required'"
          :error-messages="errors.first('Codigopostal')"
          label="Código Postal"
          :disabled="carregando || desabilitar_campose"
        ></v-text-field>
    </v-col>   
    </v-row>   

    <v-row>
      <v-col cols="3">
        <v-btn class="mr-4" @click="submit" :disabled="carregando || desabilitar_campos">Enviar</v-btn>
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
    <v-row>
      <v-col cols="3">
        <v-btn color="red" class="mr-4" @click="remover" :disabled="carregando || desabilitar_campos">Excluir Porto</v-btn>
      </v-col>
    </v-row>
  </form>
  
</template>

<script>
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'AlterarPorto',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      portoAntigo: {},
      carregando: true,
      desabilitar_campos: false,
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
            axios.put('http://localhost:8000/api/portos/'+ this.$route.params.un_locode +'/',{
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
              this.mensagem = "Alteração realizada com sucesso.";
              this.falha = false;
            })
            .catch(() => {
              this.falha = true;
              this.mensagem = "Houve um erro no processamento. Verifique os dados e tente novamente.";
            });
          }
      })
    },
  
    remover() {
      axios.delete('http://localhost:8000/api/portos/'+ this.$route.params.un_locode +'/') 
      .then(() => {              
        this.desabilitar_campos = true;
        this.falha = false;
        this.mensagem = "Porto removido com sucesso.";
        setTimeout( () => this.$router.push('Inicio'), 2000);
      })
      .catch(() => {
        this.falha = true;
        this.mensagem = "Erro na Exclusão. Porto relacionado a viagens.";
      });
    },
  },    
  
  mounted () {
    // Carrega informações do usuário
    axios
      .get('http://localhost:8000/api/portos/'+ this.$route.params.un_locode +'/')
      .then(response => {
        this.portoAntigo = response.data;
        this.un_locode = this.portoAntigo.un_locode;
        this.nomeporto = this.portoAntigo.nome;
        this.capacidadeteu = this.portoAntigo.capacidade_teus_anuais
        
       if (this.portoAntigo.endereco != null){
          this.endereco = this.portoAntigo.endereco.linha_1;
          this.cidade = this.portoAntigo.endereco.cidade;
          this.pais = this.portoAntigo.endereco.pais;
          this.regiao = this.portoAntigo.endereco.regiao;
          this.codigo_postal = this.portoAntigo.endereco.codigo_postal;
        }       
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