<script setup>

defineOptions({
    name: 'ArticleActionBar'
})

import useArticlesStore from "@/store/articles.js";
import {reactive, watch} from "vue";
import {filterArticles, getArticlesList} from '@/api/articlesAPI.js'

let articlesStore = useArticlesStore()
let articleFilter = reactive({
    categorySelected: null,
    subcategorySelected: null,
    tagSelected: null,
})

// reset
function resetSelectedFilter() {
    articleFilter.categorySelected = null
    articleFilter.subcategorySelected = null
    articleFilter.tagSelected = null
    getArticlesList()
}

// 通过watch监视articleFilter的值，来实现filter
watch(() => [articleFilter.categorySelected, articleFilter.subcategorySelected, articleFilter.tagSelected], (newValue, oldValue) => {
    console.log(newValue)
    console.log(oldValue)
    if (newValue[0] === null && newValue[1] === null && newValue[2] === null) {
        getArticlesList()
        return
    }

    if (newValue[0] === null) {
        articleFilter.subcategorySelected = null
    }

    let filterConditions = {
        categorySelected: articleFilter.categorySelected,
        subcategorySelected: articleFilter.subcategorySelected,
        tagSelected: articleFilter.tagSelected
    }
    filterArticles(filterConditions)
})

</script>

<template>
    <div class="actionbar-container">
        <div class="category-selection">
            <q-select
                class="category"
                v-model="articleFilter.categorySelected"
                :options="articlesStore.categoryList"
                label="Filter Category"
                outlined
                color="teal-5"
                text-color="black"
                dense
                clearable
                @update:model-value="articleFilter.subcategorySelected = null"
            ></q-select>
        </div>

        <div class="subcategory-selection">
            <template v-if="!articleFilter.categorySelected">
                <q-select
                    class="subcategory"
                    v-model="articleFilter.subcategorySelected"
                    :options="[]"
                    label="Filter Subcategory"
                    outlined
                    color="teal-5"
                    text-color="black"
                    dense
                    disable
                    clearable
                ></q-select>
            </template>
            <template v-else-if="articleFilter.categorySelected==='Coding'">
                <q-select
                    class="subcategory"
                    v-model="articleFilter.subcategorySelected"
                    :options="articlesStore.subcategoryObject['Coding']"
                    label="Filter Subcategory"
                    outlined
                    color="teal-5"
                    text-color="black"
                    dense
                    clearable
                ></q-select>
            </template>
            <template v-else-if="articleFilter.categorySelected==='Product'">
                <q-select
                    class="subcategory"
                    v-model="articleFilter.subcategorySelected"
                    :options="articlesStore.subcategoryObject['Product']"
                    label="Filter Subcategory"
                    outlined
                    color="teal-5"
                    text-color="black"
                    dense
                    clearable
                ></q-select>
            </template>
            <template v-else-if="articleFilter.categorySelected==='English'">
                <q-select
                    class="subcategory"
                    v-model="articleFilter.subcategorySelected"
                    :options="articlesStore.subcategoryObject['English']"
                    label="Filter Subcategory"
                    outlined
                    color="teal-5"
                    text-color="black"
                    dense
                    clearable
                ></q-select>
            </template>
        </div>

        <div class="tag-selection">
            <q-select
                class="tag"
                v-model="articleFilter.tagSelected"
                :options="articlesStore.tagsList"
                label="Filter Tag"
                outlined
                color="teal-5"
                text-color="black"
                dense
                clearable
            ></q-select>
        </div>

        <div class="reset-btn">
            <q-btn
                class="reset"
                size="10px"
                icon="restart_alt"
                @click="resetSelectedFilter"
            ></q-btn>
        </div>

        <div class="create-btn">
            <q-btn
                class="create"
                size="10px"
                icon="add_circle"
                :to="{name:'create'}">
            </q-btn>
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

    .category-selection {
        position: fixed;
        top: 95px;
        left: 50px;
        width: 250px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
    }

    .subcategory-selection {
        position: fixed;
        top: 95px;
        left: 320px;
        width: 250px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
    }

    .tag-selection {
        position: fixed;
        top: 95px;
        left: 590px;
        width: 250px;
        max-height: 300px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
    }

    .reset-btn {
        position: fixed;
        top: 100px;
        left: 870px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        color: #5c7370;
    }

    .create-btn {
        position: fixed;
        top: 100px;
        left: 940px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        color: #5c7370;
    }
}
</style>