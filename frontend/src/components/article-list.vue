<script setup>
defineOptions({
    name: 'ArticleList'
})

import useArticlesStore from "../store/articles.js";

let articlesStore = useArticlesStore()

</script>

<template>
    <div class="article-list-container">
        <template v-for="article in articlesStore.articlesList" :key="article.article_id">
            <q-card class="article-list-item" flat bordered>

                <q-card-section>
                    <div class="article-category">
                        <span class="article-l1-category">{{ article.levelFirstCategory }}</span>
                        /
                        <span class="article-l2-category">{{ article.levelSecondCategory }}</span>
                    </div>
                    <div class="article-title">{{ article.title }}</div>
                    <div class="article-short-content">{{ article.short_content }}</div>
                    <span class="article-updated-date">{{ article.updated_date }}</span>

                    <template v-for="(item, index) in article.tags" :key="index">
                        <span class="article-tags">{{ item }}</span>
                    </template>

                </q-card-section>
                <q-separator/>
                <q-card-actions>
                    <q-btn class="action-btn view" size="12px" label="view"></q-btn>
                    <q-btn class="action-btn edit" size="12px" label="edit"></q-btn>
                    <q-btn class="action-btn delete" size="12px" label="delete"></q-btn>
                    <q-btn class="action-btn like" round size="10px" icon="thumb_up"></q-btn>
                    <q-btn class="action-btn comment" round size="10px" icon="textsms"></q-btn>
                    <q-btn class="action-btn share" round size="10px" icon="share"></q-btn>
                </q-card-actions>
            </q-card>
        </template>
        <div class="ph"></div>
    </div>
</template>

<style scoped lang="scss">
.article-list-container {
    position: absolute;
    top: 10px;
    left: 10%;

    .article-list-item {
        width: 80%;
        margin: 20px 0 30px 0;

        .article-category {
            margin: 0 40px 10px 0;

            .article-l1-category {
                font-size: 17px;
                font-weight: 600;
            }

            .article-l2-category {
                font-size: 13px;
                font-weight: 400;
            }
        }

        .article-title {
            font-size: 26px;
            font-weight: 800;
        }

        .article-short-content {
            font-size: 18px;
            font-weight: 400;
            margin: 0 0 10px 0;
        }

        .article-updated-date {
            font-size: 14px;
            font-weight: 300;
            margin-right: 20px;
        }

        .article-tags {
            font-size: 14px;
            font-weight: 400;
            margin-right: 10px;
        }

        .action-btn {
            margin: 2px 15px 2px 5px;
        }

        .view {
            color: whitesmoke;
            background-color: teal;
        }

        .edit {
            color: whitesmoke;
            background-color: teal;
        }

        .delete {
            color: whitesmoke;
            background-color: #c43939;
        }

        .like {
            color: teal;
        }

        .comment {
            color: teal;
        }

        .share {
            color: teal;
        }
    }
}

.ph{
    width: 100px;
    height: 50px;
}
</style>