<template>
  <form>
    <v-row>
      <v-col>
        <v-text-field
          name="Navio"
          v-model="nome"
          v-validate="'required'"
          :error-messages="errors.first('Navio')"
          label="Nome do Navio"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
     <v-col cols="12" sm="6">
        <v-text-field
          name="IMO" 
          v-model="numero_imo" 
          v-validate="'required'"
          v-mask="IMO" 
          :error-messages="errors.first('IMO')"
          label="Numero IMO"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="6">
        <v-text-field
          name="Bandeira"
          v-model="estado_bandeira"
          v-validate="'required'"
          :error-messages="errors.first('Bandeira')"
          label="Bandeira"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field 
          name="Comprimento" 
          v-model="comprimento_metros" 
          :error-messages="errors.first('Comprimento')"
          label="Comprimento (Metros)"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-text-field 
          name="Largura" 
          v-model="largura_metros" 
          :error-messages="errors.first('Largura')"
          label="Largura (Metros)"
        ></v-text-field>
      </v-col>
    </v-row>
        <v-row>
      <v-col cols="12" sm="6">
        <v-select
          item-text="nome_fantasia"
          item-value="id"
          :items="empresas"
          v-model="empresa"
          label="Empresa"
        ></v-select>
      </v-col>
      <v-col>
        <v-text-field 
          name="Porte" 
          v-model="porte_bruto_toneladas" 
          :error-messages="errors.first('Porte')"
          label="Porte Bruto (Toneladas)"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field
          name="Tripulantes" 
          v-model="numero_de_tripulantes" 
          :error-messages="errors.first('Tripulantes')"
          label="Número de Tripulantes"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          item-text="nome"
          item-value="id"
          name="Tipo de Carga"
          v-model="tipos_de_carga_suportados"
          :items="tipos_carga"
          multiple
          chips
          persistent-hint
          label="Tipo de Carga"


        ></v-select>
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
        <v-btn color="red" class="mr-4" @click="remover" :disabled="carregando || desabilitar_campos">Excluir Navio</v-btn>
      </v-col>
    </v-row>
  </form>
  
</template>

<script>
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'AlterarNavio',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      navioAntigo: {},
      carregando: true,
      falha: false,
      mensagem: '',
      
      
      // Campos formulario
      numero_imo: '',
      nome: '',
      estado_bandeira: '',
      comprimento_metros: '',
      largura_metros: '',
      numero_de_tripulantes: [],
      porte_bruto_toneladas: '',
      empresa: '',
      tipos_de_carga_suportados: [],
      empresas: [],
      tipos_carga: [],

      // Mascaras
      IMO: '#######',
    }
  },
  methods: {

    remover() {
      axios.delete('http://localhost:8000/api/navios/'+ this.$route.params.numero_imo +'/') 
      .then(() => {              
        this.desabilitar_campos = true;
        this.falha = false;
        this.mensagem = "Navio removido com sucesso.";
        setTimeout( () => this.$router.push('Inicio'), 2000);
      })
      .catch(() => {
        this.falha = true;
        this.mensagem = "Erro na Exclusão. Navio relacionado a viagens.";
      });
    },
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.put('http://localhost:8000/api/navios/'+ this.$route.params.numero_imo +'/', {
              numero_imo: this.numero_imo,
              nome: this.nome,
              estado_bandeira: this.estado_bandeira,
              comprimento_metros: this.comprimento_metros,
              largura_metros: this.largura_metros,
              numero_de_tripulantes: this.numero_de_tripulantes,
              porte_bruto_toneladas: this.porte_bruto_toneladas,
              empresa: this.empresa.id,
              tipos_de_carga_suportados: this.tipos_de_carga_suportados
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
    }
  },

  mounted () {
    // Carrega informações do navio
    axios
      .get('http://localhost:8000/api/navios/'+ this.$route.params.numero_imo +'/')
      .then(response => {
        this.navioAntigo = response.data;
        this.numero_imo = this.navioAntigo.numero_imo;
        this.nome = this.navioAntigo.nome;
        this.estado_bandeira = this.navioAntigo.estado_bandeira;
        this.comprimento_metros = this.navioAntigo.comprimento_metros;
        this.largura_metros = this.navioAntigo.largura_metros;
        this.numero_de_tripulantes = this.navioAntigo.numero_de_tripulantes;
        this.porte_bruto_toneladas = this.navioAntigo.porte_bruto_toneladas;
        this.empresa = this.navioAntigo.empresa;
        this.tipos_de_carga_suportados = this.navioAntigo.tipos_de_carga_suportados.map(x => x.id);
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      })
      .finally(() => this.carregando = false)

    // Carrega empresas
    axios
      .get('http://localhost:8000/api/empresas/')
      .then(response => {
        this.empresas = response.data.map(function(empresa){
          if(empresa)
          return {'id': empresa.id, 'nome_fantasia': empresa.nome_fantasia};
        });
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      })
      .finally(() => this.carregando = false)

    // Carrega tipos de carga
    axios
      .get('http://localhost:8000/api/tipos-carga/')
      .then(response => {
        this.tipos_carga = response.data.map(function(tipo_carga){
          if(tipo_carga)
          return {'id': tipo_carga.id, 'nome': tipo_carga.nome + " " + tipo_carga.unidade};
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