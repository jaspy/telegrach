<template>
    <div id="story">
        <div id="input" v-show="mode === 'edit'">
        <textarea-autosize
            placeholder="Type something here..."
            ref="story"
            class="story"
            v-model="story"
            :min-height="30"
            :min-width="300"
        ></textarea-autosize>
        </div>
        <div id="result" v-show="mode === 'preview'" v-html="markdownedStory"></div>
    </div>
</template>

<script>
export default {
    name: "story",
    data() {
        return {
            story: '',
            mode: 'edit'
        }
    },
    mounted(){
        this.$refs.story.$el.focus()
    },
    computed: {
        markdownedStory(){
            return this.$options.filters.marked(this.story)
        },
    }
}
</script>


<style scoped>

.story, .story:focus, .story:active  {
  outline: none;
  border: none;
}

</style>
