<template>
    <div class="content-RightDash">
        <div class="work-area">
            <div class="item-dash">
                <div v-if="element_object" v-for="element in Object.keys(element_object)" class="item-field name-field">
                    <label class="item-field__label" v-bind:for="element">{{ this.dictionary[element] }}</label>
                    <div class="item-field__group">
                        <textarea
                            v-if="['notes', 'text'].includes(element)"
                            v-model="element_object[element]['text']"
                            class="item-field__input"
                            type="search"
                            v-bind:id="element"
                            v-bind:name="element"
                            v-bind:readonly="['show_only'].includes(this.mode)"
                            rows="15"
                        ></textarea>
                        <input
                            v-else
                            v-model="element_object[element]['text']"
                            class="item-field__input"
                            type="search"
                            v-bind:id="element"
                            v-bind:name="element"
                            v-bind:readonly="['show_only'].includes(this.mode)"
                        >
                        <button
                            v-if="this.copy_fields.includes(element)"
                            class="item-field__btn"
                            type="button"
                            v-bind:for="element"
                            @click="click_copy"
                        >Copy
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="button-area">
            <div class="btn-set">
                <div v-if="['show_only'].includes(this.mode)" @click="edit_elem" class="btn edit-btn">Редагувати</div>
                <div v-if="['edit', 'create'].includes(this.mode)" class="btn save-btn" @click="save_element">Зберегти</div>
                <div v-if="['edit'].includes(this.mode)" class="btn save-btn danger-button" @click="cancel_changes">Відмінити</div>
                <div v-if="['show_only'].includes(this.mode)" class="btn delete-btn danger-button" @click="delete_element">Видалити</div>
            </div>
        </div>

        <!-- <div>{{ this.element }}</div>
        <div>{{ this.right_elem }}</div> -->
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "RightDash",
        data() {
            return {
                unnecessary_fields: ['id', 'user', 'category'],
                element_category: null,
                readonly: true,
                mode: null,
                copy_fields: [
                    'login',
                    'password',
                    'site',
                    'owner_name',
                    'card_number',
                    'year',
                    'month',
                    'cvv',
                    'pin_code'
                ],
                read_only_fields: [
                    'date_creation',
                    'date_update'
                ],
                dictionary: {
                    "title": "Назва",
                    "login": "Логін",
                    "password": "Пароль",
                    "site": "Сайт",
                    "notes": "Замітка",
                    "tag": "Теги",
                    "date_creation": "Дата створення",
                    "date_update": "Дата модифікації",
                    "category": "Категорія",
                    "text": "Текст",
                    "owner_name": "Власник",
                    "card_number": "Номер карти",
                    "year": "Рік",
                    "month": "Місяць",
                    "cvv": "cvv",
                    "pin_code": "Пін код"
                },
                element: {},
                element_object: null,
                field_set: [],
                new_id: null
            }
        },
        props: ['right_elem', 'categorylist', 'category_id', 'new_elem', 'update_right'],
        methods: {
            fetch_elem() {
                if (this.right_elem) {
                    const url = '/api/v1/items/' + this.right_elem + '/';
                    try {
                        axios.get(
                            url,
                            {
                                withCredentials: true,
                                headers: {
                                    "Content-Type": "application/json",
                                    "Masterpass": 'qwerty'
                                }
                            }
                        )
                        .then((response) => {
                            this.element = response.data;
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                    } catch {
                        console.log('error fetch_elem')
                    }
                }
            },
            fill_field_set() {
                const field_set = this.categorylist.filter((obj) => obj['id'] == this.category_id)[0]['field_set'];
                this.field_set = field_set.filter((obj) => ! this.unnecessary_fields.includes(obj));
            },
            create_element_object() {
                this.element_object = {}
                for (let i in this.field_set) {
                    this.element_object[this.field_set[i]] = {text: '', widget: 'null'};
                }

                console.log()
            },
            fill_element_object() {
                if (this.element) {
                    for (let i in this.element) {
                        if (typeof this.element_object[i] != 'undefined') {
                            if (i == 'tag') {
                                this.element_object[i]['text'] = this.tags_to_string(this.element[i])
                            } else {
                                this.element_object[i]['text'] = this.element[i]
                            }
                        }
                    }

                    //this.element_object = JSON.parse(JSON.stringify(this.element_object))
                }

                console.log()
            },
            save_element() {
                const data = {};
                for (let i in this.element_object) {
                    if (this.read_only_fields.includes(i)) {
                        continue
                    }

                    if (i == 'tag') {
                        data[i] = this.tags_to_list(this.element_object[i].text);
                    } else {
                        data[i] = this.element_object[i].text;
                    }
                }

                data['category'] = this.category_id;

                if (this.mode == 'create') {
                    this.create_element(data);
                } else if (this.mode == 'edit') {
                    this.update_element(data);
                }

            },
            create_element(data) {
                const url = 'api/v1/items/';

                const headers = {
                        "Content-Type": "application/json",
                        "masterpass": "qwerty"
                    }

                if (document.cookie) {
                    headers['x-csrftoken'] = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1] 
                }

                try {                    
                    axios.post(
                        url,
                        data,
                        {
                            withCredentials: true,
                            headers: headers
                        }
                    )
                    .then((response) => {
                        this.new_id = response.data.id
                        //this.$emit('item_update', response.data.id)
                    })
                    .catch((error) => {
                        console.log(error)
                    })  
                } catch(e) {
                    console.log(e)
                }
            },
            update_element(data) {
                const url = 'api/v1/items/' + this.element.id + '/';

                const headers = {
                        "Content-Type": "application/json",
                        "masterpass": "qwerty"
                    }

                if (document.cookie) {
                    headers['x-csrftoken'] = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1] 
                }

                try {                    
                    axios.patch(
                        url,
                        data,
                        {
                            withCredentials: true,
                            headers: headers
                        }
                    )
                    .then((response) => {
                        this.new_id = response.data.id
                        //this.$emit('item_update', response.data.id)
                    })
                    .catch((error) => {
                        console.log(error)
                    })  
                } catch(e) {
                    console.log(e)
                }
            },
            delete_element() {
                const url = 'api/v1/items/' + this.element.id + '/';

                const headers = {
                        "Content-Type": "application/json",
                        "masterpass": "qwerty"
                    }

                if (document.cookie) {
                    headers['x-csrftoken'] = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1] 
                }

                try {                    
                    axios.delete(
                        url,
                        {
                            withCredentials: true,
                            headers: headers
                        }
                    )
                    .then((response) => {
                        this.$emit('delete_element')
                        this.element = null;
                        this.element_object = null;
                    })
                    .catch((error) => {
                        console.log(error)
                    })  
                } catch(e) {
                    console.log(e)
                } 
            },
            edit_elem() {
                this.readonly = false;
                this.mode = 'edit';
            },
            show_only_mode() {
                this.mode = 'show_only'
            },
            apply_creation_mode() {
                this.mode = 'create'
            },
            cancel_changes() {
                this.mode = 'show_only';
                this.fill_element_object();
            },
            tags_to_string(tag_list) {
                return tag_list.join(', ')
            },
            tags_to_list(tag_string) {
                const res =  tag_string.split(',').map((val) => {return val.trim()})
                if (res.length == 1 && res[0] == '') {
                    return []
                }

                return res
            },
            click_copy(e) {
                const value = this.element_object[e.target.attributes.for.nodeValue].text
                navigator.clipboard.writeText(value)
                .then(() => {
                    console.log('Done')
                })
                .catch(err => {
                    console.log('Something went wrong', err);
                });
            }
        },
        mounted() {
            if (this.new_elem) {
                this.fill_field_set();
                this.create_element_object();
                this.apply_creation_mode();
                this.$emit('cansel_new_elem');
            } else if (this.right_elem) {
                this.fetch_elem();
                this.fill_field_set();
                this.create_element_object();
                this.mode = 'show_only'
            }
        },
        watch: {
            right_elem() {
                if (this.right_elem) {
                    this.fetch_elem();
                    this.fill_field_set();
                    this.create_element_object();
                    this.mode = 'show_only'
                }
            },
            new_elem() {
                if (this.new_elem) {
                    this.fill_field_set();
                    this.create_element_object();
                    this.apply_creation_mode();
                    this.$emit('cansel_new_elem');
                }
            },
            element() {
                this.fill_element_object();
                this.show_only_mode();
            },
            new_id() {
                if (this.new_id) {
                    this.$emit('item_update', this.new_id);
                    this.new_id = null;
                }
            },
            update_right() {
                if (this.right_elem) {
                    this.fetch_elem();
                    this.fill_field_set();
                    this.create_element_object();
                    this.mode = 'show_only'
                }
            }
        },
        computed: {
            //
        }
    }
</script>

<style>
    .item-field__group {
        display: flex;
    }

    .item-field__btn {
        display: inline-block;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        vertical-align: middle;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
        background-color: #4CAF50;
        border: 1px solid #4CAF50;
        padding: 1px .75rem;
        font-size: 1rem;
        border-radius: .25rem;
        transition: background-color .15s ease-in-out;
    }
    .item-field__btn:hover {
        background-color: #60cd65;
    }
    .item-field__group .text-field__input {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        position: relative;
        z-index: 2;
    }
    .item-field__group .item-field__btn {
        position: relative;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
        border-left-width: 0;
        color: white;
    }

    .item-field {
        display: flex;
        padding-top: 25px;
        flex-direction: column;
        align-items: start;
    }

    .content-RightDash {
        display: flex;
        flex-direction: column;
    }

    .button-area {
        height: 50px;
        border: 0.5px solid #dbdbdb;
        box-shadow: 1px -2px 6px 0px #99959529;
    }

    .work-area {
        flex-grow: 1;
        background-color: #f4f4f7;
        overflow: scroll;
    }

    .item-dash {
        padding: 10px;
    }

    .item-field__group {
        padding-left: 0;
    }

    .item-field__input {
        text-overflow: ellipsis;
        width: 500px;
        border: 0.5px solid #4caf50;
        padding-left: 5px;
        min-height: 26.5px;
    }

    @media (max-width: 900px) {
        .item-field__input {
            width: 416px;
        }
    }

    @media (max-width: 469px) {
        .item-field__input {
            width: 280px;
        }
    }

    .btn-set {
        display: flex;
        background-color: #f4f4f7;
    }

    /* .btn {
        cursor:pointer;
        border-width:1px;
        border-style:solid;
        background-color:gray;
        width:100px;
        text-align:center;
        color:#ffffff;
    } */

    .btn {
        color: #fff; /* цвет текста */
        text-decoration: none; /* убирать подчёркивание у ссылок */
        user-select: none; /* убирать выделение текста */
        background: #4CAF50; /* фон кнопки */
        padding: .7em 1.5em; /* отступ от текста */
        outline: none; /* убирать контур в Mozilla */
        width: 127px;
        margin: 5px;
    } 
    .btn:hover {
        background: #60cd65; 
    } /* при наведении курсора мышки */
    .btn:active {
        background: #409344; 
    } /* при нажатии */

    .danger-button {
        background-color: #cb3730ed;
    }

    .danger-button:hover {
        background-color: #e14841ed;
    }

    .danger-button:active {
        background-color: #c1120aed;
    }
</style>