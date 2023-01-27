<template>
    <div class="home">
        <LeftDash class="leftDash" />
        <MiddleDash class="middleDash" />
        <RightDash class="rightDash" />
    </div>
</template>

<script>
    import LeftDash from '@/components/LeftDash';
    import MiddleDash from '@/components/MiddleDash';
    import RightDash from '@/components/RightDash';
    export default {
        name: 'App',
        components: {
            LeftDash,
            MiddleDash,
            RightDash
        }
    }
</script>

<style>
    .home {
        display: flex;
        height: 100%;
    }

    .leftDash, .middleDash, .rightDash {
        border: 0.5px solid #dbdbdb;
    }

    .leftDash {
        flex-grow: 0.3;
        background-color: #f4f4f7;
        padding: 10px;
        max-width: 15%;
    }

    .middleDash {
        flex-grow: 1;
        max-width: 25%;
    }

    .rightDash {
        flex-grow: 3;
        max-width: 60%;
    }
</style>