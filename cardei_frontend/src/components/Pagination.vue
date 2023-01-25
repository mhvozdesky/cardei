<template>
    <div>
        <ul class="pagination">
            <li
                v-for="p in total_our_pages"
                :key="p"
            >
                <button
                    class="pagination-button"
                    :class="{active: current_page===p}"
                    @click="change_page(p)"
                >
                    {{ p }}
                </button>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Pagination",
        props: ['total_page', 'item'],
        data() {
            return {
                current_page: 1
            }
        },
        methods: {
            change_page(page_number) {
                this.current_page = page_number;
                this.$emit('page-changed', page_number)
            }
        },
        computed: {
            total_our_pages() {
                if (this.item > 0){
                    return Math.ceil(this.total_page / this.item)
                }

                return 0
            }
        }
    }
</script>

<style>
    .pagination {
        background-color: white;
        color: #1c1d21;
        border: 1px solid #3b5998;
    }

    .active {
        background-color: #1da1f2;
    }
</style>