<template>
  <form>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field 
          name="CNPJ" 
          v-model="cnpj" 
          v-mask="cnpjMask" 
          v-validate="'required'"
          :error-messages="errors.first('CNPJ')"
          label="CNPJ"
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>      
    </v-row>
    <v-row>
        <v-col cols="12" sm="12">
         <v-text-field 
          name="Razaosocial" 
          v-model="razao_social" 
          v-validate="'required'"
          :error-messages="errors.first('Razaosocial')"
          label="Razão social"
          :disabled="carregando ? true : false"
        ></v-text-field>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="12" sm="12">
         <v-text-field 
          name="Nomefantasia" 
          v-model="nome_fantasia" 
          v-validate="'required'"
          :error-messages="errors.first('Nomefantasia')"
          label="Nome Fantasia"
          :disabled="carregando ? true : false"
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
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>
    <v-col class="d-flex" cols="12" sm="6">
        <v-text-field
          name="Telefone" 
          v-model="telefone" 
          v-mask="telefoneMask" 
          v-validate="'required'"
          :error-messages="errors.first('Telefone')"
          label="Telefone"
          :disabled="carregando ? true : false"
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
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="6">
        <v-text-field
          name="Cidade" 
          v-model="cidade" 
          v-validate="'required'"
          :error-messages="errors.first('Cidade')"
          label="Cidade"
          :disabled="carregando ? true : false"
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
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Regiao" 
          v-model="regiao" 
          v-validate="'required'"
          :error-messages="errors.first('Regiao')"
          label="Região"
          :disabled="carregando ? true : false"
        ></v-text-field>
    </v-col>    
    <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          name="Codigopostal" 
          v-model="codigo_postal" 
          v-mask="codigopostalMask"
          v-validate="'required'"
          :error-messages="errors.first('Codigopostal')"
          label="Código Postal"
          :disabled="carregando ? true : false"
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
        <v-btn color="red" class="mr-4" @click="remover" :disabled="carregando ? true : false">Excluir Empresa</v-btn>
      </v-col>
    </v-row>
  </form>
  
</template>

<script>
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'AlterarEmpresa',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      empresaAntigo: {},
      carregando: true,
      falha: false,
      mensagem: '',
      
      // Campos formulario
      razao_social: '',
      nome_fantasia: '',
      cnpj: '',
      email: '',
      telefone: '',
      endereco: '',
      cidade: '',
      pais: '',
      codigo_postal: '',
      regiao: '',

      // Mascaras
      cnpjMask: '##.###.###/####-##',
      telefoneMask: '##(##) ####-####',
      codigopostalMask: '#####-###',
    }
  },
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.put('http://localhost:8000/api/empresas/'+ this.$route.params.id +'/', {
              email: this.email,
              cnpj: this.cnpj,
              razao_social: this.razao_social,
              nome_fantasia: this.nome_fantasia,
              telefone: this.telefone,
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
      axios.delete('http://localhost:8000/api/empresas/'+ this.$route.params.id +'/') 
      .then(() => {              
        this.falha = false;
        this.$router.push('Inicio')
      })
      .catch(() => {
        this.falha = true;
        this.mensagem = "Erro na Exclusão. Empresa relacionada com navios.";
      });
    },
  },    
  
  mounted () {
    this.$emit('message', 'Empresas');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
    // Carrega informações do usuário
    axios
      .get('http://localhost:8000/api/empresas/'+ this.$route.params.id +'/')
      .then(response => {
        this.empresaAntigo = response.data;
        this.cnpj = this.empresaAntigo.cnpj;
        this.razao_social = this.empresaAntigo.razao_social;
        this.nome_fantasia = this.empresaAntigo.nome_fantasia;
        this.email = this.empresaAntigo.email;
        this.telefone = this.empresaAntigo.telefone;
        if (this.empresaAntigo.endereco != null){
          this.endereco = this.empresaAntigo.endereco.linha_1;
          this.cidade = this.empresaAntigo.endereco.cidade;
          this.pais = this.empresaAntigo.endereco.pais;
          this.regiao = this.empresaAntigo.endereco.regiao;
          this.codigo_postal = this.empresaAntigo.endereco.codigo_postal;
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