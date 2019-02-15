<template>
    <div id="titleWrapper">
        <input type="text" name="title" class="title" placeholder="Title">
    </div>
</template>

<script>
export default {
    name: "title"
}
</script>

<style scoped>

.title, .title:focus, .title:active  {
  outline: none;
  border: none;
}

</style>