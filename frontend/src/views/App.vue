<template>
  <v-app id="app">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <router-link to='/'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>
                Início
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to='/usuarios'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-account-multiple</v-icon>
            </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Usuários
                </v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to='/navios'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-ferry</v-icon>
            </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Navios
                </v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to='/tipos-carga'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-package-variant-closed</v-icon>
            </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Tipos de Carga
                </v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </router-link>

        <router-link to='/empresas'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-home-city</v-icon>
            </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Empresas
                </v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </router-link>

        <router-link to='/portos'>
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-warehouse</v-icon>
            </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Portos
                </v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </router-link>

        <v-list-item link v-on:click="logout()">
          <v-list-item-action>
            <v-icon></v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>{{ this.appTitle }}</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-container>
            <router-view @message="setTitle" @authToken="setAuthToken">
            </router-view>
          </v-container>
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
      appTitle: 'Application',
      auth_token: ''
    }),
    methods: {
      setTitle(variable){
        this.appTitle = variable;
      },
      setAuthToken(token){
        this.auth_token = token;
      },
      logout(){
        localStorage.removeItem('auth_token');
        this.$router.push('/Inicio');
      }
    }
  }
</script>

<style>
  a { /* router-link */
    color: #757575 !important;
    text-decoration: none;
  }
</style>