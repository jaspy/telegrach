import Vue from 'vue'
import App from './App.vue'
import VueTextareaAutosize from 'vue-textarea-autosize'
import marked from 'marked';

Vue.filter('marked', marked)

Vue.use(VueTextareaAutosize)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
