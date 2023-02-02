<template>
    <div class="content-LeftDash">
        <div class="categories item-LeftDash">
            <div class="title-item-LeftDash">
                <div class="text-title-item-LeftDash">Категорії</div>
                <div class="btn-title-item-LeftDash"></div>
            </div>
            <ul v-if="categorylist" class="list-item-LeftDash">
                <li v-for="category in categorylist" :key="category.id">
                    {{category.title}}
                </li>
                <li>Пароль</li>
            </ul>
        </div>
        <div class="tags item-LeftDash">
            <div class="title-item-LeftDash">
                <div class="text-title-item-LeftDash">Теги</div>
                <div class="btn-title-item-LeftDash"></div>
            </div>
            <ul v-if="taglist" class="list-item-LeftDash">
                <li v-for="tag in taglist" :key="tag.id">
                    {{ tag.title }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LeftDash",
        data() {
            return {
                data: null
            }
        },
        props: ['categorylist', 'taglist']
    }
</script>

<style>
    .item-LeftDash {
        padding: 10px;
    }

    .list-item-LeftDash {
        padding: 10px;
    }

    .btn-title-item-LeftDash {
        width: 15px;
        height: 15px;
        background-image: url("@/assets/images/close.svg");
        background-size: contain;
        background-repeat: no-repeat;
        margin-left: 11px;
        align-self: center;
        cursor: pointer;
    }

    .title-item-LeftDash {
        display: flex;
    }
</style>