<template>
    <div>
        <section class="ab-info-main py-md-5 py-4 editContent single">
            <div class="container py-md-3">
                <!-- top Products -->
                <div class="row">
                    <div class="left-ads-display col-lg-10">
                        <div class="row">
                            <div class="desc1-left col-md-6">
                                <img :src="movie.poster" class="img-fluid" alt="">
                            </div>
                            <div class="desc1-right col-md-6 pl-lg-4">
                                <h3 class="editContent" >{{ movie.title }}</h3>
                                <h5 class="editContent">{{ movie.tagline }}</h5>
                                <ul>
                                    <li class="li-movie"><span><b>Год:</b> {{ movie.year }}</span></li>
                                    <li class="li-movie"><span><b>Страна:</b> {{ movie.country }}</span></li>
                                    <li class="li-movie"><span><b>Слоган:</b> «{{ movie.tagline }}»</span></li>
                                    <li class="li-movie">
                                        <span><b>Режиссеры: </b>
                                            <span
                                                v-for="director in movie.directors"
                                                :key="director.id"
                                            >
                                                {{ director.name }}
                                            </span>
                                        </span>
                                    </li>
                                    <li class="li-movie">
                                        <span><b>Актеры: </b>
                                            <span
                                                v-for="actor in movie.actors"
                                                :key="actor.id"
                                            >
                                                {{ actor.name }}
                                            </span>
                                        </span>
                                    </li>
                                    <li class="li-movie">
                                        <span><b>Жанр:</b>
                                            <span
                                                v-for="genre in movie.genres"
                                                :key="genre.id"
                                            >
                                                {{ genre }}
                                            </span>
                                        </span>
                                    </li>
                                    <li class="li-movie"><span><b>Премьера в мире:</b> {{ movie.world_premiere }}</span></li>
                                    <li class="li-movie"><span><b>Бюджет:</b> ${{ movie.budget }}</span></li>
                                    <li class="li-movie"><span><b>Сборы в США:</b> ${{ movie.fees_in_usa }}</span></li>
                                    <li class="li-movie"><span><b>Сборы в мире:</b> ${{ movie.fess_in_world }}</span></li>
                                    <li class="li-movie">
                                        <a href="#"><b>Рейтинг:</b>
                                        <span class="fa fa-star" aria-hidden="true"
                                            ></span>
                                            <span class="fa fa-star" aria-hidden="true"
                                                ></span>
                                            <span class="fa fa-star" aria-hidden="true"
                                                ></span>
                                            <span class="fa fa-star" aria-hidden="true"
                                                ></span>
                                            <span class="fa fa-star" aria-hidden="true"
                                                ></span>
                                            <span class="editContent"
                                                >5.0</span>
                                        </a>
                                    </li>
                                    <div class="share-desc">
                                        <div class="share">
                                            <h4 class="editContent"
                                                >
                                                Share:</h4>
                                            <ul class="w3layouts_social_list list-unstyled">
                                                <li>
                                                    <a href="#" class="w3pvt_facebook editContent"
                                                    >
                                                    <span class="fa fa-facebook-f"
                                                        ></span>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="#" class="w3pvt_twitter editContent"
                                                    >
                                                    <span class="fa fa-twitter"
                                                        ></span>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="#" class="w3pvt_dribble editContent"
                                                    >
                                                    <span class="fa fa-dribbble"
                                                        ></span>
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="clearfix"></div>
                                    </div>
                                </ul>
                            </div>
                        </div>
                        <div class="row sub-para-w3layouts mt-5">

                            <h3 class="shop-sing editContent" >
                                О фильме {{ movie.title }}</h3>
                            <p>
                                <img src="@/assets/images/about.jpg" class="img-fluid" alt="">
                                <img src="@/assets/images/admin.jpg" class="img-fluid" alt="">
                                <img src="@/assets/images/d1.jpg" class="img-fluid" alt="">
                            </p>
                            <p class="editContent" v-html="movie.description"></p>
                        </div>
                        <hr>
                        <Review
                            :reviews="movie.reviews"
                            :movie_id="movie.id"
                            @reLoad="loadMovie"
                        />
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import axios from 'axios'
    import Review from '@/components/Review.vue'
    export default {
        name: "Single",
        props: ['id'],
        components: {Review},
        data() {
            return {
                movie: {}
            }
        },
        created() {
            this.loadMovie();
        },
        mounted() {
            //this.loadMovie();
        },
        methods: {
            async loadMovie() {
                try {
                    const response = await axios.get(
                        this.$store.getters.getServerURL + '/movie/' + this.id + '/'
                    );

                    if (response.status < 400) {
                        this.movie = response.data;
                    }
                } catch (e) {
                    console.log(e);
                }
            }
        },
        computed: {
            some_films() {
                return this.movie;
            }
        }
    }
</script>

<style scoped>
    .single {
        outline: none;
        outline-offset: -2px;
        cursor: inherit;
        color: rgb(33, 37, 41);
        font-size: 16px;
        background-color: rgba(0, 0, 0, 0);
        font-family: Lato, sans-serif;
    }

    .li-movie {
        list-style: none;
    }
</style>