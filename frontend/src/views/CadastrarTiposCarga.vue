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
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4">
        <v-text-field
          name="UnidadeTipo"
          v-model="unidadetipo"
          v-validate="'required'"
          :error-messages="errors.first('UnidadeTipo')"
          label="Simbolo de Unidade de Medida"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-btn class="mr-4" @click="submit">Enviar</v-btn>
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

export default {
  name: 'CadastrarTiposCarga',
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
      tipocarga: '',
      unidadetipo: '',

    }
  },
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.post('http://localhost:8000/api/tipos-carga/', {
              nome: this.tipocarga,
              unidade: this.unidadetipo,
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
    }
  },
  
  
}

</script>

<style scoped>

</style>
