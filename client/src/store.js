/* eslint-disable no-param-reassign */
import Vue from 'vue';
import Vuex from 'vuex';
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
      state.title = data.title;
      state.writerName = data.writerName;
      state.story = data.story;
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

      // console.log(JSON.stringify(data.story));
    },
    publishNote(state) {
      // console.log(String.raw`${state.story}`)
      // console.log(state.story.split('\n'))
      // TODO: publish note
    },
    deleteNote(state) {
      // TODO: delete note
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
    publishNote({commit}) {
      commit('publishNote');
    },
    deleteNote({commit}) {
      commit('deleteNote');
    },
  },
});

export default store;
