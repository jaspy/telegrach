<template>
  <div class="Note">
    <noteTitle ></noteTitle>
    <br>
    <noteWriterName ></noteWriterName>
    <br>
    <noteStory></noteStory> 
    <controlButtons v-if="isUserCreator"></controlButtons>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Title from '../components/Note/Title'
import WriterName from '../components/Note/WriterName'
import Story from '../components/Note/Story'
import ControlButtons from '../components/Note/ControlButtons'

export default {
  name: 'Note',
  async created(){
    await this.$store.dispatch('getNote', this.$route.params.noteSlug)
  },
  computed: {
    ...mapGetters(['hash']),
    isUserCreator() {
      return (localStorage.hash === this.hash)
    },
  },
  methods:{
    ...mapActions(['initState', 'changeMode', 'getNote']),
    
  },
  components: {
    noteTitle: Title,
    noteWriterName: WriterName,
    noteStory: Story,
    controlButtons: ControlButtons,
  },
}
</script>

<style lang="scss">
@import '@/assets/note.scss'; 

</style>
