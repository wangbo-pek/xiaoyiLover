<script setup>
defineOptions({
    name: 'ArticleActionBar'
})

import useArticlesStore from "@/store/articles.js";

let articlesStore = useArticlesStore()

console.log(articlesStore.categoryList)
console.log(articlesStore.subcategoryObject)

</script>

<template>
    <div class="actionbar-container">

        <div class="create-btn">
            <q-btn
                class="c-btn"
                size="15px"
                label="Create"
                text-color="black"
                unelevated
                :to="{name:'create'}"

            ></q-btn>
        </div>

            <div class="category-selection">
                <q-select
                    class="c-selection"
                    v-model="e"
                    :options="op"
                    label="Filter Category"
                    outlined
                    label-color="black"
                    color="white"
                    dense
                    clearable
                ></q-select>
            </div>

        <div class="tag-selection">
            <q-select
                class="t-selection"
                v-model="e"
                :options="d"
                label="Filter Tag"
                standout
                label-color="black"
                color="white"
                dense
                clearable
            ></q-select>
        </div>

    </div>
</template>

<style scoped lang="scss">
.actionbar-container {
    position: fixed;
    top: $header-high;
    left: 0;
    width: 75%;
    height: 70px;
    z-index: 98;
    background-color: rgba(255, 255, 255, 0.75);

    .create-btn {
        position: fixed;
        top: 95px;
        left: 50px;
        text-transform: none;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));

    }

    .category-selection {
        position: fixed;
        top: 95px;
        left: 170px;
        width: 300px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
    }

    .tag-selection {
        position: fixed;
        top: 95px;
        left: 500px;
        width: 300px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
    }
}
</style>