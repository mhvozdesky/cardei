<template>
    <div v-if="!global_error" class="home-content">
        <div class="choice-set">
            <div @click="comp_change(0)"><span>Фільтр</span></div>
            <div @click="comp_change(1)"><span>Елементи</span></div>
            <div @click="comp_change(2)"><span>Вікно</span></div>
        </div>
        <div class="home" v-if="width>=750">
            <LeftDash class="leftDash" />
            <MiddleDash class="middleDash" />
            <RightDash class="rightDash" />
        </div>
        <div class="mobile-home" v-else-if="comp == 0">
            <LeftDash class="leftDash" />
        </div>
        <div class="mobile-home" v-else-if="comp == 1">
            <MiddleDash class="middleDash" />
        </div>
        <div class="mobile-home" v-else-if="comp == 2">
            <RightDash class="rightDash" />
        </div>
    </div>
</template>

<script>
    import LeftDash from '@/components/LeftDash';
    import MiddleDash from '@/components/MiddleDash';
    import RightDash from '@/components/RightDash';
    import axios from 'axios';
    export default {
        name: 'App',
        components: {
            LeftDash,
            MiddleDash,
            RightDash
        },
        data() {
            return {
                width: 0,
                comp: 1,
                global_error: false
            }
        },
        methods: {
            updateWidth() {
                this.width = window.innerWidth;
            },
            comp_change(e) {
                this.comp = e;
            },
            get_profile() {
                const url = '/api/v1/profile/';
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
                        this.$store.commit('setUser', response.data)
                    })
                    .catch((error) => {
                        this.$router.push({name: 'Login'})
                    })
                } catch {
                    this.global_error = true
                }
            }
        },
        computed: {
            env() {
                return process.env
            },

            user() {
                return this.$store.state.user
            }
        },
        created() {
            this.width = window.innerWidth;
            window.addEventListener('resize', this.updateWidth);
        },
        mounted() {
            this.get_profile();
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
        background: #f4f4f7;
    }

    .rightDash {
        flex-grow: 3;
        max-width: 60%;
    }

    .choice-set {
        display: flex;
        background-color: #f4f4f7;
    }

    .home-content {
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .choice-set div {
        color: #fff; /* цвет текста */
        text-decoration: none; /* убирать подчёркивание у ссылок */
        user-select: none; /* убирать выделение текста */
        background: #4CAF50; /* фон кнопки */
        padding: 4px 2px; /* отступ от текста */
        outline: none; /* убирать контур в Mozilla */
        width: 80px;
        margin: 5px;
        display: none;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    @media (max-width: 750px) {
        .choice-set div {
            display: flex;
        }

        .leftDash, .middleDash, .rightDash {
            max-width: 100%;
            width: 100%;
            height: 100%;
        }
    }

    .choice-set div:hover {
        background: #60cd65; 
    } /* при наведении курсора мышки */

    .choice-set div:active {
        background: #409344; 
    } /* при нажатии */

    .mobile-home {
        height: 100%;
    }
</style>