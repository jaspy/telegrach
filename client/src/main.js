import Vue from 'vue'
import App from './App.vue'
import marked from 'marked';

Vue.filter('marked', marked)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
