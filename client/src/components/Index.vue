<template>
  <div class="Index">
    <noteTitle></noteTitle>
    <br>
    <noteWriterName></noteWriterName>
    <br>
    <noteStory></noteStory>
    <controlButtons></controlButtons>
  </div>
</template>

<script>
import Title from './Note/Title'
import WriterName from './Note/WriterName'
import Story from './Note/Story'
import ControlButtons from './ControlButtons'

export default {
  name: 'Index',
  data(){
    return {
      title: '',
      name: '',
      story: "",
      mode: "edit"
    }
  },
  components: {
    noteTitle: Title,
    noteWriterName: WriterName,
    noteStory: Story,
    controlButtons: ControlButtons,
  },
  computed: {
    currentMode(){
      return this.mode == "edit" ? "preview" : "edit" 
    }
  },
  methods: {
    changeMode(){
      this.mode = this.mode == "edit" ? "preview" : "edit"
    },
    publsh(){
      // TODO: Publish 
    }
  }
}
</script>

<style>

</style>
