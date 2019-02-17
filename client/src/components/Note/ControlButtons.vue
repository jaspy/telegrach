<template>
  <div class="controlButtons">
    <div class="changeMode">
        <button v-on:click="changeMode"> {{ mode === 'edit' ? 'preview' : 'edit' | capitalize   }} </button>
    </div>
    <div class="publish">
        <button v-on:click="publishNote"> Publish </button>
    </div>
    <div class="delete" v-if="noteExists">
        <button v-on:click="deleteNote"> Delete </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ControlButtons',
  computed: {
       mode: {
            get(){
                return this.$store.getters.mode
            },
            set(){
                this.changeMode()
            }
        },
        noteExists(){
          return this.$route && this.$route.params && this.$route.params.noteSlug ? true : false
        }
  },
  methods: {
    ...mapActions(['changeMode', 'publishNote', 'deleteNote']),
  }
}
</script>

<style>

</style>
