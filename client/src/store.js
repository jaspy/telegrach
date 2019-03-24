/* eslint-disable no-param-reassign */
import Vue from 'vue';
import Vuex from 'vuex';
import marked from 'marked';
import axios from 'axios';
import VueAxios from 'vue-axios';
import router from './router';
import {hexString, digestMessage} from './gen-hashes';

Vue.use(Vuex);
Vue.use(VueAxios, axios);

const store = new Vuex.Store({
  state: {
    mode: 'edit',
    title: '',
    writerName: '',
    story: '',
    hash: '',
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
    hash(state) {
      return state.hash;
    },
  },
  mutations: {
    initState(state, data) {
      state.mode = 'edit';
      state.title = data && data.title ? data.title : '';
      state.writerName = data && data.writerName ? data.writerName : '';
      state.story = data && data.story ? data.story : '';
    },
    changeMode(state) {
      state.mode = state.mode === 'edit' ? 'preview' : 'edit';
    },
    changeTitle(state, data) {
      state.title = data.newTitle;
    },
    changeWriterName(state, data) {
      state.writerName = data.newWriterName;
    },
    changeStory(state, data) {
      state.story = data.story;
    },
    clearState(state) {
      state.mode = 'preview';
      state.title = '';
      state.story = '';
    },
    getNote(state, data) {
      state.mode = 'preview';
      state.title = data.title;
      state.writerName = data.username;
      state.story = data.body;
      state.hash = data.hash;
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
    publishNote({commit, state}, slug) {
      if (slug) {
        // update note
        axios
          .put(`/api/posts/${slug}`, {
            title: state.title,
            username: state.writerName,
            body: state.story,
          })
          .then(response => commit('getNote', response.data))
          .catch(console.log);
      } else {
        // create note
        axios
          .post('/api/posts', {
            title: state.title,
            username: state.writerName,
            body: state.story,
            hash: localStorage.hash,
          })
          .then(response => {
            router.push(`/${response.data.slug}`);
            commit('clearState');
          })
          .catch(console.log);
      }
    },
    async getNote({commit}, slug) {
      await axios
        .get(`/api/posts/${slug}`)
        .then(r => r.data)
        .then(data => {
          commit('getNote', data);
        });
    },
    deleteNote({commit}, slug) {
      axios.delete(`/api/posts/${slug}`).then(() => {
        // console.log(res);
        commit('clearState');
        router.push('/');
      });
    },
    generateHash() {
      const hashed = (Date.now() + Math.random()).toString();
      digestMessage(hashed).then(digestValue => {
        localStorage.hash = hexString(digestValue);
      });
    },
  },
});

export default store;
