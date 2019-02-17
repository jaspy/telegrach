<template>
  <div class="Home Note">
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

export default {
  name: 'Home',
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
