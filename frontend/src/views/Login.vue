<template>
  <form>
    <v-text-field
      name="Email"
      v-model="email"
      v-validate="'required'"
      :error-messages="errors.first('Email')"
      label="Email"
    ></v-text-field>
    <v-text-field
      name="Senha"
      v-model="password"
      v-validate="'required'"
      :error-messages="errors.first('Senha')"
      label="Senha"
      type="password"
    ></v-text-field>
    
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
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      // Carregamento API
      falha: false,
      mensagem: '',
      
      // Campos formulario
      email: '',
      password: '',
    }
  },
  methods: {
    submit() {
      this.$validator.validateAll().then((result) => {
          if (result) {
            axios.post('http://localhost:8000/api/auth/token/', {
              email: this.email,
              password: this.password
            })
            .then((response) => {
              localStorage.auth_token = response.data.access;
              // this.$emit('authToken', response.data);
              this.mensagem = "Login realizado com sucesso.";
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