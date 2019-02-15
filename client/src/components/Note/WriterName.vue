<template>
    <div id="writerNameWrapper">
        <input type="text" name="writerName" class="writerName" placeholder="Your Name"> 
    </div>
</template>

<script>
export default {
    name: "WriterName"
}
</script>

<style scoped>

.writerName, .writerName:focus, .writerName:active  {
  outline: none;
  border: none;
}

</style>
