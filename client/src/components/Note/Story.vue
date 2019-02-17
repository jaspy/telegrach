<template>
    <div id="story">
        <div id="input" v-show="currentMode === 'edit'">
            <textarea-autosize
                placeholder="Type something here..."
                ref="story"
                class="story"
                v-model="rawStory"
                :min-height="30"
                :min-width="300"
            ></textarea-autosize>
        </div>
        <div id="result" v-html="markdownedStory" v-show="currentMode === 'preview'"></div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
    name: "story",
    computed: {
        ...mapGetters(['mode', 'story','markdownedStory']),
        currentMode(){
            return this.mode
        },
        rawStory: {
            get(){
                return "this.story"
            },
            set(newValue){
                this.changeStory(newValue)
            }
        }
    },
    methods: {
        ...mapActions(['changeMode', 'changeStory']),
    }
}
</script>


<style scoped>

.story, .story:focus, .story:active  {
  outline: none;
  border: none;
}

</style>
