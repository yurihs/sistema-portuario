import Vue from 'vue'
import App from './views/App.vue'
import vuetify from './plugins/vuetify';
import router from './router';

import VeeValidate from 'vee-validate'; 
Vue.use(VeeValidate); 

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')