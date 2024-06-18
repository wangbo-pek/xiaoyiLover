<script setup>
defineOptions({
    name: 'ArticleList'
})

import useArticlesStore from "../store/articles.js";
import {deleteArticle, fetchArticle, getArticlesList} from '@/api/articlesAPI.js'
import {onMounted, reactive} from "vue";
import {useRouter} from "vue-router";

let articlesStore = useArticlesStore()
let $router = useRouter()

// Quasar的dialog数据
let dialog = reactive({
    is_show:false,
    message:'',
    articleId:'',
    listIndex:'',
})


// 删除指定文章，需要进行dialog提示
function deleteSpecifiedArticle(articleId, listIndex, title) {
    dialog.message = `是否删除${title}，该操作无法撤销`
    dialog.articleId = articleId
    dialog.listIndex = listIndex
    dialog.is_show = true
}

// 查看指定文章
function previewSpecifiedArticle(articleId, index) {
    console.log(articleId, index)
    fetchArticle(articleId, index)
    $router.push({
        name:'preview'
    })
}

// 编辑指定文章
async function reviseSpecifiedArticle(articleId, index) {
    await fetchArticle(articleId, index)
    await $router.push({
        name:'revise'
    })
}

onMounted(()=>{
    getArticlesList()
})

</script>

<template>
    <div class="article-list-container">
        <template v-for="(item, index) in articlesStore.articlesList" :key="index">
            <q-card class="article-list-item" flat bordered>
                <q-card-section>
                    <div class="l1category-l2category-tags">
                        <span class="l1category">{{ item.category }}/</span>
                        <span class="l2category">{{ item.subcategory }}</span>
                        <template v-for="(tag, ind) in item.tags" :key="ind">
                            <span class="tags">{{ tag }}</span>
                        </template>
                    </div>
                    <div class="article-title">
                        <span class="title">{{ item.title }}</span>
                    </div>
                    <div class="update-date">
                        <span class="date">{{ item.updated_date }}</span>
                    </div>
                </q-card-section>
                <q-separator/>
                <q-card-actions>
                    <q-btn
                        class="action-btn view"
                        unelevated
                        size="12px"
                        label="View"
                        color="teal-5"
                        @click="previewSpecifiedArticle(item.article_id, index)"
                    ></q-btn>
                    <q-btn
                        class="action-btn edit"
                        unelevated
                        size="12px"
                        label="Revise"
                        color="teal-5"
                        @click="reviseSpecifiedArticle(item.article_id, index)"
                    ></q-btn>
                    <q-btn
                        class="action-btn delete"
                        unelevated
                        size="12px"
                        label="Delete"
                        color="deep-orange-6"
                        @click="deleteSpecifiedArticle(item.article_id, index, item.title)"
                    ></q-btn>
                </q-card-actions>
            </q-card>
        </template>
        <div class="ph"></div>
    </div>

    <!--dialog-->
    <q-dialog v-model="dialog.is_show" persistent>
        <q-card class="dialog-container">
            <q-card-section class="dialog-content">
                <q-avatar class="dialog-icon" icon="warning" size="75px" />
                <span class="dialog-text">{{ dialog.message }}</span>
            </q-card-section>
            <q-card-actions class="dialog-btn" align="right">
                <q-btn
                    class="dialog-confirm"
                    label="Confirm"
                    unelevated
                    color="teal-5"
                    size="13px"
                    @click="deleteArticle(dialog.articleId, dialog.listIndex)"
                    v-close-popup
                ></q-btn>
                <q-btn
                    class="dialog-cancel"
                    label="Cancel"
                    unelevated
                    color="deep-orange-6"
                    size="13px"
                    v-close-popup
                ></q-btn>
            </q-card-actions>
        </q-card>
    </q-dialog>

</template>

<style scoped lang="scss">
.article-list-container {
    position: absolute;
    top: 10px;
    left: 10%;
    width: 80%;

    .article-list-item {
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        border: 0.5px #015252 solid;
        border-radius: 10px;
        margin-bottom: 25px;
    }

    .l1category-l2category-tags {
        margin-bottom: 10px;

        .l1category {
            font-size: 17px;
            font-weight: 600;
            color: #006767;
        }

        .l2category {
            font-size: 16px;
            font-weight: 500;
            margin-right: 20px;
            color: #006767;
        }

        .tags {
            font-size: 15px;
            font-weight: 400;
            margin-right: 15px;
            color: #006767;
        }
    }

    .article-title {

        .title {
            font-size: 20px;
            font-weight: 600;
            color: #005252;
        }
    }

    .update-date {
        margin-top: 5px;

        .date {
            font-size: 13px;
            font-weight: 400;
            margin-right: 20px;
            color: #006767;
        }
    }


    .view {
        margin: 5px 25px 5px 20px;
        width: 60px;
        text-transform: none;
    }

    .edit {
        margin: 5px 25px 5px 0;
        width: 60px;
        text-transform: none;
    }

    .delete {
        margin: 5px 25px 5px 0;
        width: 60px;
        text-transform: none;
    }
}

.ph {
    width: 100px;
    height: 50px;
}

.dialog-container {
    min-width: 500px;

    .dialog-content {
        .dialog-icon {
            color: #ff5722;
            margin: 10px 0 10px 5px;
        }

        .dialog-text {
            font-size: 18px;
            font-weight: 500;
            margin: 10px 0 10px 10px;
        }
    }

    .dialog-btn {
        .dialog-confirm {
            margin: 5px 10px 20px 5px;
            text-transform: none;
        }

        .dialog-cancel {
            margin: 5px 20px 20px 5px;
            text-transform: none;
        }
    }

}

</style>