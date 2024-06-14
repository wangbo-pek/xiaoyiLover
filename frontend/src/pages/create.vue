<script setup>
defineOptions({
    name: 'CreateArticle'
})

import {reactive} from 'vue'
import {MdEditor} from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import useArticlesStore from "@/store/articles.js";
import {useRouter} from "vue-router";

const $router = useRouter()

let newArticle = reactive({
    title: '',
    subtitle: '',
    is_display: '0',
    content_text: '',
    content_html: '',
    levelFirstCategory: '',
    levelSecondCategory: '',
    tags: [],
})

//
let articleStore = useArticlesStore()


function resetSecondCategory() {
    newArticle.levelSecondCategory = ''
}

</script>

<template>
    <div class="create-container">

        <div class="back-save-title-l1category">
            <div class="back-btn">
                <q-btn
                    class="back-btn"
                    size="13px"
                    label="back"
                    color="teal-5"
                    text-color="black"
                    @click="$router.back()"
                ></q-btn>
            </div>

            <div class="save-btn">
                <q-btn
                    class="save-btn"
                    size="13px"
                    label="save"
                    color="teal-5"
                    text-color="black"

                ></q-btn>
            </div>

            <div class="title-input">
                <q-input
                    v-model="newArticle.title"
                    color="teal-5"
                    label="title"
                    outlined
                    dense
                ></q-input>
            </div>

            <div class="category-select">
                <q-select
                    v-model="newArticle.levelFirstCategory"
                    :options="articleStore.categoryList"
                    label="category"
                    color="teal-5"
                    outlined
                    @update:model-value="resetSecondCategory"
                    dense
                ></q-select>
            </div>
        </div>

        <div class="subtitle-subcategory">
            <div class="subtitle-input">
                <q-input
                    v-model="newArticle.subtitle"
                    color="teal-5"
                    label="subtitle"
                    outlined
                    dense
                ></q-input>
            </div>

            <div class="subcategory-select">
                <template v-if="!newArticle.levelFirstCategory">
                    <q-select
                        v-model="newArticle.levelSecondCategory"
                        :options="[]"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        disable
                        clearable
                    ></q-select>
                </template>
                <template v-else-if="newArticle.levelFirstCategory==='coding'">
                    <q-select
                        v-model="newArticle.levelSecondCategory"
                        :options="articleStore.subcategoryObject['coding']"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        clearable
                    ></q-select>
                </template>
                <template v-else-if="newArticle.levelFirstCategory==='english'">
                    <q-select
                        v-model="newArticle.levelSecondCategory"
                        :options="articleStore.subcategoryObject['english']"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        clearable
                    ></q-select>
                </template>
                <template v-else-if="newArticle.levelFirstCategory==='product'">
                    <q-select
                        v-model="newArticle.levelSecondCategory"
                        :options="articleStore.subcategoryObject['product']"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        clearable
                    ></q-select>
                </template>
            </div>
        </div>

        <div class="display-tag">
            <div class="display-radio">
                <q-radio v-model="newArticle.is_display" val="0" label="display" color="teal-5"></q-radio>
                <q-radio v-model="newArticle.is_display" val="1" label="hidden" color="teal-5"></q-radio>

            </div>

            <div class="tag-select">
                <q-select
                    model-value=""
                    label="tag"
                    color="teal-5"
                    outlined
                    dense
                ></q-select>

            </div>
        </div>

        <div class="md-area">
            <MdEditor></MdEditor>
        </div>
    </div>
</template>

<style scoped lang="scss">
.create-container {

    .back-save-title-l1category {
        position: fixed;
        top: 30px;
        left: 30px;

        .back-btn {
            position: fixed;
            top: 30px;
            left: 50px;
            font-family: Courier,serif;
            margin-right: 50px;
        }

        .save-btn {
            position: fixed;
            top: 30px;
            left: 150px;
            font-family: Courier, serif;
        }

        .title-input {
            position: fixed;
            top: 27px;
            left: 17%;
            width: 38%;
            font-family: Courier, serif;
        }

        .category-select {
            position: fixed;
            top: 27px;
            left: 58%;
            width: 38%;
            font-family: Courier, serif;
        }
    }

    .subtitle-subcategory {
        position: fixed;
        top: 90px;
        left: 30px;

        .subtitle-input {
            position: fixed;
            top: 90px;
            left: 17%;
            width: 38%;
            font-family: Courier, serif;
        }

        .subcategory-select {
            position: fixed;
            top: 90px;
            left: 58%;
            width: 38%;
            font-family: Courier, serif;
        }
    }

    .display-tag {
        .display-radio {
            position: fixed;
            top: 155px;
            left: 45px;
            width: 38%;
            font-family: Courier, serif;
        }

        .tag-select {
            position: fixed;
            top: 155px;
            left: 17%;
            width: 79%;
            font-family: Courier, serif;
        }
    }

    .md-area {
        width: 92.7%;
        position: fixed;
        top: 230px;
        left: 50px;
    }
}

</style>