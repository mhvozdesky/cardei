<template>
    <div>404 - NOT FOUND</div>
</template>

<script>
    export default {
        name: "PageNotFound",
        mounted() {
        // Set status code 404
        document.title = "404 - Page Not Found";
        if (window.history.state) {
            window.history.replaceState({ ...window.history.state, status: 404 }, '');
        }
    }
    }
</script>

<style>
 
</style>