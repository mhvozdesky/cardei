<template>
    <div class="content-MiddleDash">
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
</style>