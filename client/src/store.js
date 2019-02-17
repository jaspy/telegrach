import Vue from 'vue';
import Vuex from 'vuex'
import marked from 'marked';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
      mode: 'edit',
      title: '',
      writerName: '123',
      story: "22",
    },
    getters: {
      mode(state){return state.mode},
      title(state){return state.title},
      writerName(state){return state.writerName},
      story(state){return state.story},
      markdownedStory(state){
        return marked(state.story)
      },
    },
    mutations: {
      changeMode(state){
        state.mode = state.mode == "edit" ? "preview" : "edit"
      },
      changeTitle(state, data){
          state.title = data.newTitle
      },
      changeWriterName(state, data){
          state.writerName = data.newWriterName
      },
      changeStory(state, data){
          state.story = data.story
      },
      publish(state){
        // TODO: publish note
      },
      deleteNote(state){
        // TODO: delete note
      }
    },
    actions: {
      changeMode ({commit}) {
        commit('changeMode')
      },
      changeTitle ({commit}, newTitle) {
        commit('changeTitle', {newTitle, })
      },
      changeWriterName({commit}, newWriterName){
        commit('changeWriterName', {newWriterName, })
      },
      changeStory({commit}, story){
        commit('changeStory', {story, })
      },
      publish({commit}){
        commit('publish')
      },
      deleteNote({commit}){
        commit('deleteNote')
      }
    }
  })

export default store;