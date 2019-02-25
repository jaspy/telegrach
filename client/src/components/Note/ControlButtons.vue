<template>
  <div class="controlButtons">
    <div class="changeMode">
        <button v-on:click="changeMode"> {{ mode === 'edit' ? 'preview' : 'edit' | capitalize   }} </button>
    </div>
    <div class="publish">
        <button v-on:click="pubOrEdit"> Publish </button>
    </div>
    <div class="delete" v-if="noteExists">
        <button v-on:click="deleting"> Delete </button>
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
    ...mapActions(['changeMode', 'publishNote', 'deleteNote', 'generateHash']),
    pubOrEdit() {
      localStorage.username = this.$store.getters.writerName;
      if (!this.$route.params.noteSlug && !localStorage.hash) {
        this.generateHash()
      };
      this.publishNote(this.$route.params);
    },
    deleting() {
      this.deleteNote(this.$route.params.noteSlug)
    },    
  }
}
</script>

<style scoped lang='scss'>
  .controlButtons {
    display: flex;
    justify-content: space-around;
    width: 80%;
  }

  .controlButtons > div > button {
    background-color: rgb(235, 135, 21); /* Green */
    border: 1px solid rgb(235, 135, 21);
    color: white;
    padding: 12px 26px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    border-radius: 4px;
  }

  .controlButtons > div:hover > button {
    background-color: rgb(204, 93, 19);
  }

  .controlButtons > div > button:focus {
    outline: none;
    box-shadow: 0 0 0 2pt rgba(204, 93, 19, 0.8); 
  }

  .controlButtons > div {
    margin-top: 40px;
  }

</style>
