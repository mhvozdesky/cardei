<template>
    <Nav />
    <router-view/>
    <Footer />
</template>

<script>
    import Nav from '@/components/Nav';
    import Footer from '@/components/Footer';
    export default {
        name: 'App',
        components: {
            Nav,
            Footer
        }
    }
</script>

<style>
    @import "assets/css/bootstrap.css";
    @import "assets/css/font-awesome.css";
    @import "assets/css/style.css";
 
</style>