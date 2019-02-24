/* eslint-disable no-param-reassign */
import Vue from 'vue';
import Vuex from 'vuex';
import router from './router';
import marked from 'marked';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(Vuex);
Vue.use(VueAxios, axios)

const store = new Vuex.Store({
  state: {
    mode: 'edit',
    title: '',
    writerName: '',
    story: '',
  },
  getters: {
    mode(state) {
      return state.mode;
    },
    title(state) {
      return state.title;
    },
    writerName(state) {
      return state.writerName;
    },
    story(state) {
      return state.story;
    },
    markdownedStory(state) {
      return marked(state.story);
    },
  },
  mutations: {
    initState(state, data) {
      state.mode = "edit";
      state.title = data && data.title ? data.title : "";
      state.writerName = data && data.writerName ? data.writerName : "";
      state.story = data && data.story ? data.story : "";
    },
    changeMode(state) {
      state.mode = state.mode == 'edit' ? 'preview' : 'edit';
    },
    changeTitle(state, data) {
      state.title = data.newTitle;
    },
    changeWriterName(state, data) {
      state.writerName = data.newWriterName;
    },
    changeStory(state, data) {
      state.story = data.story;

      // console.log(state);
    },
    clearState(state){
      state.mode = 'preview'
      state.title= ''
      // state.writerName= ''
      state.story = ''
    },
    getNote(state, data) {
      state.mode = 'preview'
      state.title = data.title
      state.writerName= data.username
      state.story = data.body

      // localStorage.user = data.username
    },
  },
  actions: {
    initState({commit}, data) {
      commit('initState', data);
    },
    changeMode({commit}) {
      commit('changeMode');
    },
    changeTitle({commit}, newTitle) {
      commit('changeTitle', {newTitle});
    },
    changeWriterName({commit}, newWriterName) {
      commit('changeWriterName', {newWriterName});
    },
    changeStory({commit}, story) {
      commit('changeStory', {story});
    },
    publishNote({commit, state}, where) {
      console.log(localStorage)
      if (where.noteSlug) {
        axios
        .put(`http://localhost:5000/api/posts/${where.noteSlug}`, {
          title: state.title,
          username: state.writerName,
          body: state.story,
        })
        .then(r => r.data)
        .then(data => {
          // this.$cookie.set('test', 'Hello world!', 1);
          // console.log(this.$cookie.get('test'));
          
          commit('getNote', data)
        }).catch(e => {e})
      } else {
        axios
        .post('http://localhost:5000/api/posts', {
          title: state.title,
          username: state.writerName,
          body: state.story,
        })
        .then(r => r.data)
        .then(data => {
          router.push(`/${data.slug}`)
          commit('clearState')
        }).catch(e => {e});
      }
    },
    getNote({commit}, slug) {
      axios
        .get(`http://localhost:5000/api/posts/${slug}`)
        .then(r => r.data)
        .then(data => {
          commit('getNote', data)
        });
    },
    deleteNote({commit}, slug) {
      axios
        .delete(`http://localhost:5000/api/posts/${slug}`)
        .then(r => r.data)
        .then(data => {
          console.log(data)
          router.push('/')          
        });
    },
  },
});

export default store;
