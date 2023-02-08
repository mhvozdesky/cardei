<template>
    <div class="login-block">
        <div class="container">
            <h1>Login</h1>
            <p>Please fill in this form to login.</p>
            <hr>

            <label for="email"><b>Email</b></label>
            <ul v-if="email.errors.length > 0" class="error-list">
                <li v-for="error in email.errors">
                    {{error}}
                </li>
            </ul>
            <input v-model="email.text" type="text" placeholder="Enter Email" name="email" required>
            

            <label for="psw"><b>Password</b></label>
            <ul v-if="password.errors.length > 0" class="error-list">
                <li v-for="error in password.errors">
                    {{error}}
                </li>
            </ul>
            <input v-model="password.text" type="password" placeholder="Enter Password" name="psw" required>
            <hr>

            <ul v-if="common_error.length > 0" class="error-list">
                <li v-for="error in common_error">
                    {{error}}
                </li>
            </ul>

            <button @click="login" type="submit" class="registerbtn">Login</button>
        </div>
        
        <div class="container signin">
            <p>Don't have an account yet? <a href="javascript:void(0);" @click="$router.push({name: 'Register'})">Sign up</a>.</p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Login",
        data() {
            return {
                email: {
                    text: null,
                    errors: []
                },
                password: {
                    text: null,
                    errors: []
                },
                common_error: []
            }
        },
        methods: {
            login() {
                this.clear_errors()
                const url = 'api/v1/account/login/';

                const data = {
                    email: this.email.text,
                    password: this.password.text
                }
                
                try {
                    const headers = {
                        "Content-Type": "application/json",
                        "masterpass": "qwerty"
                    }

                    if (document.cookie) {
                        headers['x-csrftoken'] = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1] 
                    }


                    axios.post(
                        url,
                        data,
                        {
                            withCredentials: true,
                            headers: headers
                        }
                    )
                    .then((response) => {
                        this.$store.commit('setMasterpass', this.password.text)
                        this.$router.push({name: 'Home'})
                    })
                    .catch((error) => {
                        if (typeof error.response.data.email != 'undefined') {
                            this.email.errors = error.response.data.email
                        }
                        if (typeof error.response.data.password != 'undefined') {
                            this.password.errors = error.response.data.password
                        }
                        if (typeof error.response.data.non_field_errors != 'undefined') {
                            this.common_error = error.response.data.non_field_errors
                        }
                        if (typeof error.response.data.detail != 'undefined') {
                            console.log(error.response.data.detail)
                        }
                    })  
                } catch(e) {
                    console.log(e)
                }
            },
            clear_errors() {
                this.email.errors = []
                this.password.errors = []
                this.common_error = []

            }
        }
    }
</script>

<style scoped>
    /* Add padding to containers */
    .container {
        padding: 16px;
        background-color: white;
    }

    .login-block {
        width: 500px;
        margin: auto;
    }

    @media (max-width: 550px) {
        .login-block {
            width: 340px;
        }
    }

    /* Full-width input fields */
    input[type=text], input[type=password] {
        width: 100%;
        padding: 15px;
        margin: 5px 0 22px 0;
        display: inline-block;
        border: none;
        background: #f1f1f1;
        box-sizing: border-box;
    }

    input[type=text]:focus, input[type=password]:focus {
        background-color: #ddd;
        outline: none;
    }

    /* Overwrite default styles of hr */
    hr {
        border: 1px solid #f1f1f1;
        margin-bottom: 25px;
    }

    /* Set a style for the submit button */
    .registerbtn {
        background-color: #4CAF50;
        color: white;
        padding: 16px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
        opacity: 0.9;
    }

    .registerbtn:hover {
        opacity: 1;
    }

    /* Add a blue text color to links */
    a {
        color: dodgerblue;
    }

    /* Set a grey background color and center the text of the "sign in" section */
    .signin {
        background-color: #f1f1f1;
        text-align: center;
    }
</style>