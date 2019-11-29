<template>
  <form>
    <v-row>
     <v-col cols="12" sm="8">
        <v-text-field
          name="Tipocarga"
          v-model="tipocarga"
          v-validate="'required'"
          :error-messages="errors.first('Tipocarga')"
          label="Tipo carga"
          :disabled="bloquear_campos"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4">
        <v-text-field
          name="UnidadeTipo"
          v-model="unidadetipo"
          v-validate="'required'"
          :error-messages="errors.first('UnidadeTipo')"
          label="Simbolo de Unidade de Medida"
          :disabled="bloquear_campos"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="3">
        <v-btn class="mr-4" @click="submit" :disabled="carregando ? true : false">Enviar</v-btn>
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
        <v-btn color="red" class="mr-4" @click="remover" :disabled="carregando ? true : false">Excluir Tipo de Carga</v-btn>
      </v-col>
    </v-row>
  </form>
  
</template>

<script>
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'AlterarTiposCarga',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      tipoAntigo: {},
      bloquear_campos: false,
      carregando: true,
      falha: false,
      mensagem: '',
      
      // Campos formulario
      tipocarga: '',
      unidadetipo: '',

    }
  },
  
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.put('http://localhost:8000/api/tipos-carga/'+ this.$route.params.id +'/',{
              nome: this.tipocarga,
              unidade: this.unidadetipo,
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
      axios.delete('http://localhost:8000/api/tipos-carga/'+ this.$route.params.id +'/') 
      .then(() => {
        this.bloquear_campos = true;
        this.falha = false;
        this.mensagem = "Remoção realizada com sucesso.";
        setTimeout( () => this.$router.push('Inicio'), 2000);
      })
      .catch(() => {
        this.falha = true;
        this.mensagem = "Erro na Exclusão. Tipo de Carga inexistente ou relacionada a navios e/ou viagens.";
      });
    },
  },    
  
  mounted () {
    this.$emit('message', 'Tipos de Carga');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
    // Carrega informações do usuário
    axios
      .get('http://localhost:8000/api/tipos-carga/'+ this.$route.params.id +'/')
      .then(response => {
        this.tipoAntigo = response.data;
        this.tipocarga = this.tipoAntigo.nome;
        this.unidadetipo = this.tipoAntigo.unidade;
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