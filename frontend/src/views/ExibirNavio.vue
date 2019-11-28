<template>
  <div>
    <h2>Navio {{ navio.nome }}</h2>
    <p><b>Número IMO:</b> {{ navio.numero_imo }}</p>
    <v-row>
        <v-col cols="4">
            <p><b>Bandeira:</b> {{ navio.estado_bandeira }}</p>
        </v-col>
        <v-col cols="4">
            <p><b>Comprimento (m):</b> {{ navio.comprimento_metros }}</p>
        </v-col>
        <v-col cols="4">
            <p><b>Largura (m):</b> {{ navio.largura_metros }}</p>
        </v-col>
    </v-row>
    <v-row>
        <v-col>
            <p><b>Número de Tripulantes:</b> {{ navio.numero_tripulantes }}</p>
        </v-col>
        <v-col>
            <p><b>Porte Bruto em Toneladas:</b> {{navio.porte_bruto_toneladas}}</p>
        </v-col>
    </v-row>
    <hr>
    <h3>Empresa:</h3>
        <v-row>
            <v-col offset-md="1">
                <v-row>
                    <v-col cols="4">
                        <p><b>ID:</b> {{ navio.empresa.id}}</p>
                     </v-col>
                    <v-col cols="4">
                        <p><b>CNPJ:</b> {{ navio.empresa.cnpj }}</p>
                    </v-col>
                    <v-col cols="4">
                        <p><b>Nome Fantasia:</b> {{ navio.empresa.nome_fantasia }}</p>
                    </v-col>                    
                </v-row>
            </v-col>
        </v-row>
        <v-row>
            <v-col offset-md="1">
                <v-row>
                    <v-col cols="6">
                        <p><b>Razão Social:</b> {{ navio.empresa.razao_social}}</p>
                     </v-col>
                    <v-col cols="3">
                        <p><b>E-mail:</b> {{ navio.empresa.email }}</p>
                    </v-col>
                    <v-col cols="3">
                        <p><b>Telefone:</b> {{ navio.empresa.telefone }}</p>
                    </v-col>                    
                </v-row>
            </v-col>
        </v-row>
        <v-row>
            <v-col offset-md="1">
                <v-row>
                    <v-col cols="6">
                        <p><b>Logradouro:</b> {{ navio.empresa.endereco.linha_1}}</p>
                     </v-col>
                    <v-col cols="3">
                        <p><b>Cidade:</b> {{ navio.empresa.endereco.cidade }}</p>
                    </v-col>
                    <v-col cols="3">
                        <p><b>Região:</b> {{ navio.empresa.endereco.regiao }}</p>
                    </v-col>                     
                </v-row>
            </v-col>
        </v-row>
        <v-row>
            <v-col offset-md="1">
                <v-row>
                    <v-col cols="6">
                        <p><b>País:</b> {{ navio.empresa.endereco.pais}}</p>
                     </v-col>
                    <v-col cols="6">
                        <p><b>Codigo Postal:</b> {{ navio.empresa.endereco.codigo_postal }}</p>
                    </v-col>                   
                </v-row>
            </v-col>
        </v-row> 
    <hr>
    <h3>Tipos de Cargas:</h3>
        <v-row>
            <v-col offset-md="1">
                <v-row>
                    <v-col cols="4">
                        <p><b>ID:</b> {{ navio.tipos_de_carga_suportados.id}}</p>
                     </v-col>
                    <v-col cols="4">
                        <p><b>Nome:</b> {{ navio.tipos_de_carga_suportados.nome }}</p>
                    </v-col>
                    <v-col cols="4">
                        <p><b>Unidade:</b> {{ navio.tipos_de_carga_suportados.unidade }}</p>
                    </v-col>                    
                </v-row>
            </v-col>
        </v-row>     
    
    
    

    
    <v-row>
      <v-col cols="3">
        <v-btn color="blue" class="mr-4" :to="'/navios/'+navio.numero_imo+'/alterar'">Alterar Navio</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ExibirNavio',
  data() {
    return {
      navio: [],
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/navios/'+ this.$route.params.numero_imo +'/')
      .then(response => {
        this.navio = response.data;
      })
  }    
}
</script>

<style scoped>
  h2{
    margin-bottom: 40px;
  }
  p{
    font-size: 18px;
    margin: 20px 0;
  }
  v-btn, a{
    color: white !important;
  }
</style>