<template>
    <Nav v-if="! ['/register', '/login'].includes($route.path)" />
    <router-view/>
</template>

<script>
    import axios from 'axios';
    import Nav from '@/components/Nav';
    export default {
        name: 'App',
        components: {
            Nav
        },
        methods: {

        },
        computed: {
            env() {
                return process.env.VUE_APP_URL_BACK
            }
        },
        mounted() {
        },
        created() {
        }
    }
</script>

<style>
    html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,menu,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,main,menu,nav,output,ruby,section,summary,time,mark,audio,video{
        margin:0;
        padding:0;
        border:0;
        font-size:100%;
        font:inherit;
        vertical-align:baseline;
        box-sizing: border-box;
    }

    body{
        line-height:1
    }

    menu,ol,ul{
        list-style:none
    }

    table{
        border-collapse:collapse;
        border-spacing:0
    }

    button{
        background:transparent;
        border:0;
        font-size:100%;
        font:inherit;
        margin:0;
        padding:0;
        vertical-align:baseline
    }

    html,body{
        height:100%;
        width:100%
    }
    html{
        font-size:15px;
        overflow:hidden
    }
    body{
        background-color:#fff;
        line-height:1.2em;
        position:absolute;
        overflow:auto;
        color:#333;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans","Helvetica Neue",Helvetica,Arial,sans-serif
    }

    #app {
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    li {
        cursor: pointer;
        margin: 5px;
        padding: 5px;
        overflow: hidden
    }

    li:hover {
        background-color: #d0d1e5;
    }
 
</style>