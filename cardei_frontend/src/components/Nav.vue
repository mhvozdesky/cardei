<template>
    <div>
        <header>
            <div class="left-header">
                <div class="content-left-header">
                    <div class="content-left-header__text">Cardei</div> 
                </div>
            </div>
            <div class="right-header">
                <label>Maksym Hvozdetsky</label>
            </div>
        </header>
    </div>
</template>

<script>
    export default {
        name: "Nav"
    }
</script>

<style>
    header {
        width: 100%;
        height: 70px;
        display: flex;
    }

    .left-header, .right-header {
        border: 0.5px solid #dbdbdb;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .left-header {
        flex-grow: 1;
    }

    .right-header {
        width: 240px;
        position: relative;
    }

    @media (max-width: 900px) {
        .right-header {
            width: 145px;
        }
    }

    .right-header label {
        text-overflow: ellipsis;
        overflow: hidden;
        display: inline-block;
        max-width: 130px;
        text-align: center;
    }
</style>