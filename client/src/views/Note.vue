<template>
  <div class="Note">
    <noteTitle ></noteTitle>
    <br>
    <noteWriterName ></noteWriterName>
    <br>
    <noteStory></noteStory> 
    <controlButtons ></controlButtons>
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
    console.log(this.$route.params);
    
    // fetch data from server
    // const data = await axios.get().then() .... . catch()
    // if error - alert
    // const data = {}
    // this.initState(data)
    // console.log()
    // this.changeMode();
    // this.$store.dispatch('changeMode')
    this.$store.dispatch('getNote', this.$route.params.noteSlug)
    console.log(this.$store)
  },
  methods:{
    ...mapActions(['initState', 'changeMode', 'getNote'])
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
