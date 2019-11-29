<template> 
    <div align=center>   
      <v-row>
        <router-link to='/usuarios/'>      
          <v-col >
            <v-icon size="50">mdi-account-multiple</v-icon>
            <h1>USUÁRIOS</h1>
          </v-col>
        </router-link>     
        <router-link to='/navios/'>      
          <v-col>
            <v-icon size="50">mdi-ferry</v-icon>
            <h1>NAVIOS</h1>
          </v-col>
        </router-link>  
        <router-link to='/empresas/'>      
          <v-col>
            <v-icon size="50">mdi-home-city</v-icon>
            <h1>EMPRESAS</h1>
          </v-col>
        </router-link>  
        <router-link to='/portos/'>      
          <v-col>
            <v-icon size="50">mdi-warehouse</v-icon>
            <h1>PORTOS</h1>
          </v-col>
        </router-link>  
        <router-link to='/tipos-carga/'>      
          <v-col>
            <v-icon size="50">mdi-package-variant-closed</v-icon>
            <h1>CARGAS</h1>
          </v-col>
        </router-link> 
      </v-row>
     
    </div>    
</template>

<script>
export default {
  name: 'Inicio',
  data () {
    return {
    }
  },
  mounted () {
    this.$emit('message', 'Início');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
  }
}
</script>

<style scoped>

</style>