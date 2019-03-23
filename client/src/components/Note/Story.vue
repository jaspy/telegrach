<template>
    <div class="story">
        <div class="input" v-show="mode === 'edit'">
            <textarea-autosize
                placeholder="Type something here..."
                ref="story"
                class="story"
                v-model="rawStory"
                :min-height="30"
                :min-width="300"
            ></textarea-autosize>
        </div>
        <div id="result" v-html="markdownedStory" v-show="mode === 'preview'"></div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
    name: "story",
    computed: {
        ...mapGetters(['mode', 'story','markdownedStory']),
        rawStory: {
            get(){
                return this.story
            },
            set(newValue){
                this.changeStory(newValue)
            },
        },
    },
    methods: {
        ...mapActions(['changeMode', 'changeStory']),
    },
}
</script>


<style scoped lang="scss">

.story, .story:focus, .story:active  {
  outline: none;
  border: none;
}


.story {
    width: 100%;
    .input { 
        width: 100%;
    }
}


.story  textarea {
    font-size: 2em;
}

.story div#result {
    word-break: break-all;
    font-size: 2em;
}

</style>
