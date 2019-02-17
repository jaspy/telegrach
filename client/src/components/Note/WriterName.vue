<template>
    <div id="writerNameWrapper">
        <input type="text" name="writerName" class="writerName" v-model="writerName" placeholder="Your Name"> 
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: "WriterName",
    computed: { 
        writerName: {
            get(){
                return this.$store.getters.writerName
            },
            set(newWriterName){
                this.changeWriterName(newWriterName)
            }
        }
    },
    methods: {
        ...mapActions(['changeWriterName'])
    }
}
</script>

<style scoped>
.writerName, .writerName:focus, .writerName:active  {
  outline: none;
  border: none;
}
</style>
