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
        flex-grow: 1;
    }

    .middleDash {
        flex-grow: 1;
    }

    .rightDash {
        flex-grow: 2;
    }
</style>