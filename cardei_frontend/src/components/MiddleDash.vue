<template>
    <div class="content-MiddleDash">
        <div class="button-area">
            <div class="btn-set">
                <div class="btn add-btn"></div>
            </div>
        </div>
        <ul class="list-MiddleDash">
            <li class="item-MiddleDash">Реєстрація на filmix</li>
            <li class="item-MiddleDash">Нові замітки</li>
            <li class="item-MiddleDash">Реєстрація на filmix</li>
            <li class="item-MiddleDash">Реєстрація на filmix</li>
            <li class="item-MiddleDash">Нові замітки</li>
            <li class="item-MiddleDash">Реєстрація на filmix</li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "MiddleDash"
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
        background: white;
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
        background-color: #bbb6b6 !important; 
        border-radius: 50%;
        cursor: pointer;
    }

    .content-MiddleDash .btn:active {
        background-color: #7f848d !important; 
    } /* при нажатии */
</style>