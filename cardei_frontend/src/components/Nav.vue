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
                <div class="sub_menu">
                    <div class="logout">Logout</div>
                </div>
            </div>
        </header>
    </div>
</template>

<script>
    import {mapState, mapGetters, mapMutations, mapActions} from 'vuex'
    export default {
        name: "Nav",
        computed: {
            ...mapState({
                user: state => state.user
            }),
            ...mapActions({
                //fetch_user: 'fetch_user'
            }),
            fetch_user(){
                console.log(this.user)
                return this.user
            }
        }
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

    .sub_menu {
        position: absolute;
        top: 70px;
        width: 90%;
        background-color: #bfbfbf;
        min-height: 60px;
        z-index: 999;
        display: none;
    }

    .sub_menu div {
        text-align: center;
        cursor: pointer;
    }

    .right-header:hover > .sub_menu {
        display: block;
    }
</style>