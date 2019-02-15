<template>
  <div class="Index">
    <button v-on:click="changeMode"> {{ currentMode }}</button>
    <div id="input" v-show="mode === 'edit'">
      <textarea-autosize
        placeholder="Type something here..."
        ref="text"
        class="text"
        v-model="text"
        :min-height="30"
        :max-height="350"
        @blur.native="onBlurTextarea"
      ></textarea-autosize>
    </div>
    <div id="result" v-show="mode === 'preview'" v-html="compiledMarked">
    </div>
  </div>
</template>

<script>


export default {
  name: 'Index',
  data(){
    return {
      text: "",
      mode: "edit"
    }
  },
  created(){
    this.$refs.text.$el.focus()
  },
  computed: {
    compiledMarked(){
      return this.$options.filters.marked(this.text)
    },
    currentMode(){
      return this.mode == "edit" ? "preview" : "edit" 
    }
  },
  methods: {
    changeMode(){
      this.mode = this.mode == "edit" ? "preview" : "edit"
    }
  }
}
</script>

<style>

.text, .text:focus, .text:active  {
  outline: none;
  border: none;
}



</style>
