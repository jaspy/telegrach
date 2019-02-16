import Vue from 'vue'
import Vuex from 'vuex'
import store from './store'
import App from './App.vue'
import VueTextareaAutosize from 'vue-textarea-autosize'
import marked from 'marked';

Vue.filter('marked', marked)
Vue.filter('capitalize', function (value) {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
})


Vue.use(VueTextareaAutosize)
Vue.use(Vuex)

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
