<template>
  <div class="Home Note">
    <noteTitle></noteTitle>
    <br />
    <noteWriterName></noteWriterName>
    <br />
    <noteStory></noteStory>
    <controlButtons></controlButtons>
  </div>
</template>

<script>
import Title from "../components/Note/Title.vue";
import WriterName from "../components/Note/WriterName.vue";
import Story from "../components/Note/Story.vue";
import ControlButtons from "../components/Note/ControlButtons.vue";

export default {
  name: "Home",
  created() {
    console.log(this.$route.params);
    console.log(this.$store)
  this.$store.dispatch('initState')
},
  components: {
    noteTitle: Title,
    noteWriterName: WriterName,
    noteStory: Story,
    controlButtons: ControlButtons,
  },
};
</script>

<style lang="scss">
@import "@/assets/note.scss";
</style>
