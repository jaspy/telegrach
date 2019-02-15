<template>
  <div class="Index">
    <p>Hi</p>
    <textarea v-model="text"></textarea>
    <div id="result" v-html="compiledMarked">
      <!-- {{  }} -->
    </div>
  </div>
</template>

<script>


export default {
  name: 'Index',
  data(){
    return {
      text: ""
    }
  },
  computed: {
    compiledMarked(){
      return this.$options.filters.marked(this.text)
    }
  }
}
</script>

<style>
</style>
