<template>
    <div>
        <header>
            <div @click="$router.push({name: 'Home'})" class="left-header">
                <div class="content-left-header">
                    <div class="content-left-header__text">Cardei</div> 
                </div>
            </div>
            <div class="right-header">
                <label>{{ this.$store.state.user.email }}</label>
                <div class="sub_menu">
                    <div @click="logout" class="logout">Logout</div>
                    <div @click="export_json" class="export-json">Json</div>
                </div>
            </div>
        </header>
    </div>
</template>

<script>
    import {mapState, mapGetters, mapMutations, mapActions} from 'vuex'
    import axios from 'axios';
    export default {
        name: "Nav",
        methods: {
            logout() {
                const url = 'api/v1/account/logout/';
                try {
                    axios.get(
                        url,
                        {
                            withCredentials: true,
                            headers: {
                                "Content-Type": "application/json"
                            }
                        }
                    )
                    .then((response) => {
                        if (response.status < 300){
                            window.sessionStorage.clear();
                            this.$router.push({name: 'Login'});
                        }
                    })
                    .catch((error) => {
                        console.log(error.response.data)
                    })
                } catch {
                    console.log('error logout')
                }
            },
            export_json() {
                const url = '/api/v1/items/export/';
                try {
                    axios.get(
                        url,
                        {
                            withCredentials: true,
                            headers: {
                                "Content-Type": "application/json",
                                "Masterpass": this.$store.state.masterpass
                                //"Masterpass": 'qwerty'
                            }
                        }
                    )
                    .then((response) => {
                        var a = document.createElement("a");
                        const b = JSON.stringify(response.data, null, 4)
                        var file = new Blob([b], {type: 'application/json'});
                        a.href = URL.createObjectURL(file);
                        a.download = 'export.json';
                        a.click();
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                } catch {
                    console.log('error get_element_list')
                }
            }
        },
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