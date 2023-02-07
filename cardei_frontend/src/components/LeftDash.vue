<template>
    <div class="content-LeftDash">
        <div class="categories item-LeftDash">
            <div class="title-item-LeftDash">
                <div class="text-title-item-LeftDash" v-bind:class="this.bolt_class">Категорії</div>
                <div class="btn-title-item-LeftDash" @click="this.$emit('cancel_cat')"></div>
            </div>
            <ul v-if="categorylist" class="list-item-LeftDash">
                <li v-for="category in categorylist" :key="category.id" @click="this.$emit('filter_by_category', category.id)">
                    {{category.title}}
                </li>
            </ul>
        </div>
        <div class="tags item-LeftDash">
            <div class="title-item-LeftDash">
                <div class="text-title-item-LeftDash" v-bind:class="this.bolt_tag_class">Теги</div>
                <div class="btn-title-item-LeftDash" @click="this.$emit('cancel_tag')"></div>
            </div>
            <ul v-if="taglist" class="list-item-LeftDash">
                <li v-for="tag in taglist" :key="tag.id" @click="this.$emit('filter_by_tag', tag.title)">
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
        props: ['categorylist', 'taglist', 'category_selected', 'tag_selected'],
        computed: {
            bolt_class() {
                if (this.category_selected) {
                    return 'bold-text'
                }

                return ''
            },
            bolt_tag_class() {
                if (this.tag_selected) {
                    return 'bold-text'
                }

                return ''
            }
        }
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

    .bold-text {
        font-weight: 600;
    }
</style>