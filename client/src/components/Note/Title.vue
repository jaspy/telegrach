<template>
    <div class="titleWrapper">
        <input type="text" name="title" class="noteTitle" placeholder="Title" v-model="title" maxlength='20'>
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
        },
    },
    methods: {
        ...mapActions(['changeTitle'])
    }
}
</script>

<style scoped lang='scss'>

.noteTitle, .noteTitle:focus, .noteTitle:active  {
    outline: none;
    border: none;
}

.titleWrapper {
    text-align: center;
    width: 100%;
    padding: 20px;
}

.titleWrapper > input {
    width: 80%;
    font-size: 2em;
}

</style>