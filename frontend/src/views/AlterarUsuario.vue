<template>
  <form>
    <v-text-field
      name="Usuario"
      v-model="usuario"
      v-validate="'required'"
      :error-messages="errors.first('Usuario')"
      label="Nome de acesso"
    >{{ usuarioAntigo }}</v-text-field>
    <v-row>
     <v-col cols="12" sm="6">
        <v-text-field
          name="Nome"
          v-model="primeiroNome"
          v-validate="'required'"
          :error-messages="errors.first('Nome')"
          label="Nome"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="6">
        <v-text-field
          name="Sobrenome"
          v-model="sobrenome"
          v-validate="'required'"
          :error-messages="errors.first('Sobrenome')"
          label="Sobrenome"
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
      <v-col>
        <v-text-field 
          name="CPF" 
          v-model="cpfValue" 
          v-mask="cpfMask" 
          v-validate="'required'"
          :error-messages="errors.first('CPF')"
          label="CPF"
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field
          name="senha"
          v-model="senha"
          v-validate="'required|min:6'"
          :error-messages="errors.first('senha')"
          type="password"
          label="Senha"
          counter
          :disabled="carregando ? true : false"
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          name="Grupo"
          v-model="grupo"
          v-validate="'required'"
          :items="grupos"
          label="Grupo"
          :disabled="carregando ? true : false"
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
        <v-btn color="red" class="mr-4" @click="remover" :disabled="carregando || desabilitar_campos">Excluir Usuário</v-btn>
      </v-col>
    </v-row>
  </form>
  
</template>

<script>
import { mask } from 'vue-the-mask'
import axios from 'axios';

export default {
  name: 'AlterarUsuario',
  directives: {
    mask,
  },
  data() {
    return {
      // Carregamento API
      usuarioAntigo: {},
      carregando: true,
      falha: false,
      mensagem: '',
      
      // Campos formulario
      usuario: '',
      primeiroNome: '',
      sobrenome: '',
      cpfValue: '',
      email: '',
      grupos: [],
      grupo: '',
      senha: '',

      // Mascaras
      cpfMask: '###.###.###-##',
    }
  },
  methods: {
    remover() {
      axios.delete('http://localhost:8000/api/usuarios/'+ this.$route.params.id +'/') 
      .then(() => {              
        this.desabilitar_campos = true;
        this.falha = false;
        this.mensagem = "Usuário removido com sucesso.";
        setTimeout( () => this.$router.push('Inicio'), 2000);
      })
      .catch(() => {
        this.falha = true;
        this.mensagem = "Erro na Exclusão.";
      });
    },
  
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.put('http://localhost:8000/api/usuarios/'+ this.$route.params.id +'/', {
              email: this.email,
              cpf: this.cpfValue,
              grupo: this.grupo,
              password: this.senha
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
    this.$emit('message', 'Usuários');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
    // Carrega informações do usuário
    axios
      .get('http://localhost:8000/api/usuarios/'+ this.$route.params.id +'/')
      .then(response => {
        this.usuarioAntigo = response.data;
        this.email = this.usuarioAntigo.email;
        this.cpfValue = this.usuarioAntigo.cpf;
        this.grupo = this.usuarioAntigo.grupo;
      })
      .catch(error => {
        this.falha = true;
        this.mensagem = error;
      })
      .finally(() => this.carregando = false)

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