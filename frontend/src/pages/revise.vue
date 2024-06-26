<script setup>
defineOptions({
    name: 'ReviseArticle'
})

import {reactive, watch} from 'vue'
import {MdEditor} from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import useArticlesStore from "@/store/articles.js";
import {useRouter} from "vue-router";
import {fetchArticle, reviseArticle} from '@/api/articlesAPI.js'
import showdown from 'showdown'

const $router = useRouter()
let articleStore = useArticlesStore()

let toBeRevisedArticle = reactive({
    article_id:articleStore.currentArticle.article_id,
    title:articleStore.currentArticle.title,
    subtitle: articleStore.currentArticle.subtitle,
    is_display: articleStore.currentArticle.is_display,
    content_text: articleStore.currentArticle.content_text,
    content_html: articleStore.currentArticle.content_html,
    category: articleStore.currentArticle.category,
    subcategory: articleStore.currentArticle.subcategory,
    selectedTag: articleStore.currentArticle.tags,
    newAddedTag: []
})

// category、subcategory的处理
function resetSelectedSecondCategory() {
    toBeRevisedArticle.subcategory = ''
}

// tag的处理
// watch监听已选择标签列表的值是否发生了变化
watch(() => toBeRevisedArticle.selectedTag, (newValue, oldValue) => {
    // 判断已选择标签列表中，到底是新增了标签，还是删除了标签
    if (newValue.length > oldValue.length) {  // 新增标签
        let newAddedTag = newValue.filter(function (v) {
            return oldValue.indexOf(v) === -1
        })[0]
        // 判断新增的标签changedTag是否已经存在
        if (!articleStore.tagsList.includes(newAddedTag)) {
            console.log('!!!')
            articleStore.tagsList.push(newAddedTag)
            toBeRevisedArticle.newAddedTag.push(newAddedTag)
            // newArticle.selectedTag.push(changedTag)
        }
    } else if (newValue.length < oldValue.length) {  // 删除标签
        let newEliminatedTag = oldValue.filter(function (v) {
            return newValue.indexOf(v) === -1
        })[0]
        // 判断删除的标签changedTag是否是在此次创建文章时所新创建的标签
        if (toBeRevisedArticle.newAddedTag.includes(newEliminatedTag)) {
            console.log('????')
            articleStore.tagsList = articleStore.tagsList.filter(item => item !== newEliminatedTag)
            toBeRevisedArticle.newAddedTag = toBeRevisedArticle.newAddedTag.filter(item => item !== newEliminatedTag)
        }
    }
})

function createTag(val, done) {
    val = '#' + val
    done(val)
}


// 保存编辑的文章
function revise() {
    const converter = new showdown.Converter()
    toBeRevisedArticle.content_html = converter.makeHtml(toBeRevisedArticle.content_text)
    reviseArticle(toBeRevisedArticle)
    $router.push({
        name:'preview'
    })
}

</script>

<template>
    <div class="create-container">

        <div class="back-save-title-l1category">
            <div class="back-btn">
                <q-btn
                    class="back-btn"
                    size="13px"
                    label="Back"
                    color="teal-5"
                    text-color="black"
                    @click="$router.back()"
                ></q-btn>
            </div>

            <div class="save-btn">
                <q-btn
                    class="save-btn"
                    size="13px"
                    label="Save"
                    color="teal-5"
                    text-color="black"
                    @click="revise"
                ></q-btn>
            </div>

            <div class="title-input">
                <q-input
                    v-model="toBeRevisedArticle.title"
                    color="teal-5"
                    label="title"
                    outlined
                    dense
                ></q-input>
            </div>

            <div class="category-select">
                <q-select
                    v-model="toBeRevisedArticle.category"
                    :options="articleStore.categoryList"
                    label="category"
                    color="teal-5"
                    outlined
                    @update:model-value="resetSelectedSecondCategory"
                    dense
                ></q-select>
            </div>
        </div>

        <div class="subtitle-subcategory">
            <div class="subtitle-input">
                <q-input
                    v-model="toBeRevisedArticle.subtitle"
                    color="teal-5"
                    label="subtitle"
                    outlined
                    dense
                ></q-input>
            </div>

            <div class="subcategory-select">
                <template v-if="!toBeRevisedArticle.category">
                    <q-select
                        v-model="toBeRevisedArticle.subcategory"
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
                <template v-else-if="toBeRevisedArticle.category==='Coding'">
                    <q-select
                        v-model="toBeRevisedArticle.subcategory"
                        :options="articleStore.subcategoryObject['Coding']"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        clearable
                    ></q-select>
                </template>
                <template v-else-if="toBeRevisedArticle.category==='English'">
                    <q-select
                        v-model="toBeRevisedArticle.subcategory"
                        :options="articleStore.subcategoryObject['English']"
                        label="subcategory"
                        color="teal-5"
                        use-input
                        outlined
                        dense
                        clearable
                    ></q-select>
                </template>
                <template v-else-if="toBeRevisedArticle.category==='Product'">
                    <q-select
                        v-model="toBeRevisedArticle.subcategory"
                        :options="articleStore.subcategoryObject['Product']"
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
                <q-radio v-model="toBeRevisedArticle.is_display" val="1" label="display" color="teal-5"></q-radio>
                <q-radio v-model="toBeRevisedArticle.is_display" val="0" label="hidden" color="teal-5"></q-radio>
            </div>

            <div class="tag-select">
                <q-select
                    v-model="toBeRevisedArticle.selectedTag"
                    :options="articleStore.tagsList"
                    label="tag"
                    color="teal-5"
                    outlined
                    multiple
                    clearable
                    use-chips
                    use-input
                    @new-value="createTag"
                    dense
                ></q-select>

            </div>
        </div>

        <div class="editor">
            <MdEditor
                v-model="toBeRevisedArticle.content_text"
                preview-theme="github"
            ></MdEditor>
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
            margin-right: 50px;
        }

        .save-btn {
            position: fixed;
            top: 30px;
            left: 150px;
        }

        .title-input {
            position: fixed;
            top: 27px;
            left: 17%;
            width: 38%;
        }

        .category-select {
            position: fixed;
            top: 27px;
            left: 58%;
            width: 38%;
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

    .editor {
        width: 92.7%;
        position: fixed;
        top: 230px;
        left: 50px;
    }
}

</style>