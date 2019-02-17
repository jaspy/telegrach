import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Note from './views/Note.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/:noteSlug',
      name: 'note',
      component: Note,
    },
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        title: 'Home',
      },
    },
  ],
});
