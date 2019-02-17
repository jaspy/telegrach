<template>
    <div id="titleWrapper">
        <input type="text" name="title" class="noteTitle" placeholder="Title" v-model="title">
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: "noteTitle",
    computed: { 
        title: {
            get(){
                return this.$store.getters.title
            },
            set(newTitle){
                this.changeTitle(newTitle)
            }
        }
    },
    methods: {
        ...mapActions(['changeTitle'])
    }
}
</script>

<style scoped>

.noteTitle, .noteTitle:focus, .noteTitle:active  {
  outline: none;
  border: none;
}

</style>