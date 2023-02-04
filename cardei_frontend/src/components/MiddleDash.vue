<template>
    <div class="content-MiddleDash">
        <div class="button-area">
            <div class="btn-set">
                <div class="add-set">
                    <div class="btn add-btn"></div>
                    <ul v-if="categorylist" class="ul-add">
                        <li v-for="category in categorylist" :key="category.id" @click="this.$emit('add_element', category.id)">
                            {{ category.title }}
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <ul v-if="element_list" class="list-MiddleDash">
            <li v-for="element in element_list" class="item-MiddleDash" @click="this.$emit('show_elem', element.id)">{{ element.title }}</li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "MiddleDash",
        props: ['categorylist', 'element_list']
    }
</script>

<style>
    .item-MiddleDash {
        margin: 0;
    }

    .list-MiddleDash {
        list-style: none;
        padding: 0;
        /* font-family: "Lucida Sans"; */
    }

    .list-MiddleDash li {
        padding: 10px;
    }

    .list-MiddleDash li:nth-child(odd) {
        background: #e1e1e1;
    }

    .list-MiddleDash li:nth-child(even) {
        background: #f4f4f7;
    }

    .list-MiddleDash li:nth-child(odd):hover,
    .list-MiddleDash li:nth-child(even):hover {
        background-color: #d0d1e5;
    }

    .content-MiddleDash .button-area {
        height: 35px;
    }

    .content-MiddleDash .btn {
        width: 20px;
        height: 20px;
        background-image: url("@/assets/images/add.svg") !important;
        background-color: transparent !important;
        background-position: center;
        background-repeat: no-repeat;
        padding: 0;
    }

    .content-MiddleDash .btn:hover {
        background-color: #60cd65 !important; 
        border-radius: 50%;
        cursor: pointer;
    }

    .content-MiddleDash .btn:active {
        background-color: #409344 !important; 
    } /* при нажатии */

    .ul-add {
        position: relative;
        background-color: #b7b9b7;
        padding: 5px;
        display: none;
    }

    .add-set:hover > .ul-add {
        display: block;
    }
</style>