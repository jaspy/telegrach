<template>
    <div class="writerNameWrapper">
        <label for="writerName" class="writerLabel" v-show="writerName">Author</label>
        <input type="text" name="writerName" class="writerName" v-model="writerName" placeholder="Your Name"  maxlength='20' v-bind:disabled="mode === 'preview'"> 
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: "WriterName",
    computed: {
        ...mapGetters(['mode']),
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
    // text-align: center;
    width: 100%;
    padding: 20px;
}

.writerNameWrapper > input {
    width: 80%;
    // padding: 30px;
    font-size: 1.5em;
}

.writerNameWrapper input:disabled {
    background-color: #fff;
    color: black;
}

.writerLabel {
    font-size: 1.5em;
    color: #747474;
    margin-right: 20px;
    padding-right: 5px;
    // width: 80%;
    border-right: 2px solid #747474;
}
</style>
