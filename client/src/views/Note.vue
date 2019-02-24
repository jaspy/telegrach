<template>
  <div class="Note">
    <noteTitle ></noteTitle>
    <br>
    <noteWriterName ></noteWriterName>
    <br>
    <noteStory></noteStory> 
    <controlButtons v-if="isUserCreator === true"></controlButtons>
  </div>
</template>

<script>
import Title from '../components/Note/Title'
import WriterName from '../components/Note/WriterName'
import Story from '../components/Note/Story'
import ControlButtons from '../components/Note/ControlButtons'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Note',
  created(){
    this.$store.dispatch('getNote', this.$route.params.noteSlug)
    console.log(this.$route.params);
    
    // fetch data from server
    // const data = await axios.get().then() .... . catch()
    // if error - alert
    // const data = {}
    // this.initState(data)
    // console.log()
    // this.changeMode();
    // this.$store.dispatch('changeMode')
    
    console.log(this.$store)

    console.log(localStorage)
    console.log(localStorage.username)
    console.log(this.$store.state.writerName)
    console.log(this.isUserCreator())
    console.log(localStorage.username === this.$store.state.writerName)
  },
  computed: {
    ...mapGetters(['writerName']),
  },
  methods:{
    ...mapActions(['initState', 'changeMode', 'getNote']),
    isUserCreator() {
      return (localStorage.username === this.writerName)
    }
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
