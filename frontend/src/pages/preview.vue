<script setup>

defineOptions({
    name: 'PreviewArticle'
})

import {MdPreview} from "md-editor-v3";
import useArticlesStore from "@/store/articles.js";
import 'md-editor-v3/lib/style.css'
import {useRouter} from "vue-router";

let articlesStore = useArticlesStore()
let $router = useRouter()

// back-btn
function back() {
    $router.push({
        name: 'articles'
    })
}

// edit-btn
function edit() {
    $router.push({
        name: 'revise'
    })
}

</script>

<template>

    <div class="preview-container">

        <div class="back-save-like-comment-share">
            <div class="back-action">
                <q-btn
                    class="back-btn"
                    size="10px"
                    color="cyan-1"
                    text-color="teal-10"
                    icon="arrow_back"
                    round
                    @click="back"
                ></q-btn>
            </div>
            <div class="edit-action">
                <q-btn
                    class="edit-btn"
                    size="10px"
                    color="cyan-1"
                    text-color="teal-10"
                    icon="edit"
                    round
                    @click="edit"
                ></q-btn>
            </div>
            <div class="like-action">
                <q-btn
                    class="edit-btn"
                    size="10px"
                    color="deep-orange-10"
                    text-color="cyan-1"
                    icon="thumb_up"
                    round
                ></q-btn>
            </div>
            <div class="comment-action">
                <q-btn
                    class="edit-btn"
                    size="10px"
                    color="brown-6"
                    text-color="cyan-1"
                    icon="question_answer"
                    round
                ></q-btn>
            </div>
            <div class="share-action">
                <q-btn
                    class="edit-btn"
                    size="10px"
                    color="blue-grey-6"
                    text-color="cyan-1"
                    icon="share"
                    round
                ></q-btn>
            </div>
        </div>

        <div class="article-header">
            <div class="article-header-card">
                <template></template>
                <p class="title-content">{{ articlesStore.currentArticle.title }}</p>
                <p class="subtitle-content">—— {{ articlesStore.currentArticle.subtitle }}</p>
                <span class="l1category-content">{{ articlesStore.currentArticle.category }}/</span>
                <span class="l2category-content">{{ articlesStore.currentArticle.subcategory }}</span>
                <template v-for="(tag, index) in articlesStore.currentArticle.tags" :key="index">
                    <span class="tags-content">{{ tag }}</span>
                </template>
                <p class="update-date-content">{{ articlesStore.currentArticle.updated_date }}</p>
            </div>
        </div>

        <div class="article-content">
            <q-separator></q-separator>
            <q-card>
                <MdPreview
                    v-model="articlesStore.currentArticle.content_text"
                ></MdPreview>
            </q-card>

        </div>
    </div>
</template>

<style scoped lang="scss">
.preview-container {

    .back-save-like-comment-share {
        position: fixed;
        top: 15px;
        left: 105px;
        z-index: 99;

        .back-action {
            margin-bottom: 15px;
        }

        .edit-action {
            margin-bottom: 15px;
        }

        .like-action {
            margin-bottom: 15px;
        }

        .comment-action {
            margin-bottom: 15px;
        }

        .share-action {
            margin-bottom: 15px;
        }
    }

    .article-header {
        position: fixed;
        top: 10px;
        left: 150px;
        width: 80%;
        z-index: 99;

        .article-header-card {
            background-image: linear-gradient(to bottom, rgba(139, 220, 227, 0.91), rgba(138, 238, 230, 0.95), rgba(140, 238, 203, 0.99));
            border-radius: 5px;
            padding: 10px 5px 5px 15px;

            .title-content {
                font-size: 26px;
                font-weight: 700;
            }

            .subtitle-content {
                font-size: 18px;
                font-weight: 600;
                margin-left: 60px;
            }

            .l1category-content {
                font-size: 15px;
                font-weight: 500;
                color: #525252;
            }

            .l2category-content {
                font-size: 14px;
                font-weight: 400;
                margin-right: 20px;
                color: #525252;
            }

            .tags-content {
                font-size: 14px;
                font-weight: 400;
                margin-right: 15px;
                color: #6b6b6b;
            }

            .update-date-content {
                font-size: 14px;
                font-weight: 300;
                color: #8d8d8d;
            }
        }
    }

    .article-content {
        position: absolute;
        top: 200px;
        left: 150px;
        width: 80%;
    }

}
</style>