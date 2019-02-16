import Vue from 'vue';
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
      mode: 'edit',
      title: '1',
      name: '',
      story: "32",
    },
    mutations: {
    changeTitle(state, title){
        state.title = title
    },
      changeMode(state){
        state.mode = state.mode == "edit" ? "preview" : "edit"
      },
    }
  })

export default store;