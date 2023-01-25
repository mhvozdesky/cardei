<template>
    <div>
        <div class="row row-reviews">
            <div class="single-form-left">
                <!-- contact form grid -->
                <div class="contact-single">
                    <h3 class="editContent" >
                        <span class="sub-tittle editContent">{{ number_reviews }}</span>Оставить отзыв</h3>
                    <form action="#" method="get" class="mt-4" id="formReview">
                        <div class="form-group editContent">
                            <label for="contactcomment" class="editContent">Ваш комментарий*</label>
                            <textarea
                                class="form-control border"
                                rows="5" id="contactcomment"
                                required=""
                                v-model="text"
                            >
                            </textarea>
                        </div>
                        <div class="d-sm-flex">
                            <div class="col-sm-6 form-group p-0 editContent">
                                <label for="contactusername" class="editContent">Имя*</label>
                                <input
                                    type="text"
                                    class="form-control border"
                                    id="contactusername"
                                    required=""
                                    v-model="name"
                                >
                            </div>
                            <div class="col-sm-6 form-group ml-sm-3 editContent">
                                <label for="contactemail" class="editContent">Email*</label>
                                <input
                                    type="email"
                                    class="form-control border"
                                    id="contactemail"
                                    required=""
                                    v-model="email"
                                >
                            </div>
                        </div>
                        <button type="button"
                                class="mt-3 btn btn-success btn-block py-3"
                                @click="sendReview()"
                        >Отправить
                        </button>
                    </form>
                </div>
                <!--  //contact form grid ends here -->
            </div>
            <div
                class="media py-5"
                v-for="review in reviews"
                :key="review.id"
            >
                <img src="@/assets/images/te2.jpg" class="mr-3 img-fluid" alt="image">
                <div class="media-body mt-4">
                    <h5 class="mt-0 editContent">{{ review.name }}</h5>
                    <p class="mt-2 editContent" v-html="review.text"></p>
                    <a href="#formReview" @click="addParent(review.id)">Ответить</a>
                    <div
                        class="media mt-5 editContent"
                        v-for="child in review.children"
                        :key="child.id"
                    >
                        <a class="pr-3" href="#">
                            <img src="@/assets/images/te1.jpg" class="img-fluid " alt="image" >
                        </a>
                        <div class="media-body">
                            <h5 class="mt-0 editContent">{{ child.name }}</h5>
                            <p class="mt-2 editContent" v-html="child.text"></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Review",
        props: ['reviews', 'movie_id'],
        data() {
            return {
                name: '',
                email: '',
                text: '',
                parent: null
            }
        },
        methods: {
            async sendReview() {
                let data = {
                    name: this.name,
                    email: this.email,
                    text: this.text,
                    parent: this.parent,
                    movie: this.movie_id 
                }
                
                try {
                    const response = await axios.post(
                        this.$store.getters.getServerURL + '/review/',
                        data
                    );
                    this.$emit('reLoad')
                    this.clearForm()

                } catch (e) {
                    console.log(e);
                }
            },
            addParent(parent_id) {
                this.parent = parent_id;
            },
            clearForm() {
                this.name = '';
                this.email = '';
                this.text = '';
                this.parent = null;
            }
        },
        computed: {
            number_reviews() {
                if (this.reviews) {
                    return this.reviews.length
                }

                return 0
                
            }
        }
    }
</script>

<style scoped>
    .row-reviews {
        flex-direction: column;
    }
</style>