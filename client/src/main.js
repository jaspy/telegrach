/* eslint-disable no-param-reassign */
/* eslint-disable func-names */
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import VueTextareaAutosize from 'vue-textarea-autosize';
import store from './store';
import router from './router';
import App from './App.vue';

Vue.filter('capitalize', function(value) {
  if (!value) return '';
  value = value.toString();
  return value.charAt(0).toUpperCase() + value.slice(1);
});

const {VUE_APP_SERVER_HOST, VUE_APP_SERVER_PORT} = process.env;
axios.defaults.baseURL = `http://${VUE_APP_SERVER_HOST}:${VUE_APP_SERVER_PORT}`;

Vue.use(VueTextareaAutosize);
Vue.use(Vuex);
Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app');
