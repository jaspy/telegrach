<template>
  <div class="controlButtons">
    <button v-on:click="changeMode"> {{ currentMode }} </button>
    <button v-on:click="publish"> Publish </button>
  </div>
</template>

<script>
export default {
  name: 'ControlButtons',
  data(){
    return {
      mode: "edit"
    }
  },
  props: {
      publish: Function
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
  }
}
</script>

<style>

</style>
