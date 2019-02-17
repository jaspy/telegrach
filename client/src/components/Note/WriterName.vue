<template>
    <div class="writerNameWrapper">
        <input type="text" name="writerName" class="writerName" v-model="writerName" placeholder="Your Name"  maxlength='20'> 
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

<style scoped lang="scss">
.writerName, .writerName:focus, .writerName:active  {
  outline: none;
  border: none;
}


.writerNameWrapper {
    text-align: center;
    width: 100%;
    padding: 20px;
}

.writerNameWrapper > input {
    width: 80%;
    // padding: 30px;
    font-size: 1.5em;
}
</style>
