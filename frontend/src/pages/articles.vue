<script setup>
import ArticleActionBar from "@/components/article-actionbar.vue";
import ArticleList from "@/components/article-list.vue";
import {getArticlesList} from "@/api/articlesAPI.js";
import {onMounted} from "vue";

defineOptions({
    name: 'Articles'
})

</script>

<template>
    <div class="article-container desktop-only">
        <div class="column action-bar">
            <ArticleActionBar></ArticleActionBar>
        </div>
        <div class="column article-list">
            <ArticleList></ArticleList>
        </div>
    </div>
    <div class="placeholderr"></div>
</template>

<style scoped lang="scss">

.article-container {
    .action-bar {
        position: absolute;
        top: $header-high;
        left: 0;
        width: 75%;
        height: $actionbar-high;
    }

    .article-list {
        position: absolute;
        top: calc($header-high + $actionbar-high);
        left: 0;
        width: 75%;
        height: 100vh;
    }
}



</style>