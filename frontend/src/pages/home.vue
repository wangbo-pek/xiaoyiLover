<script setup>
defineOptions({
    name: 'Home'
})

import {reactive, onMounted} from 'vue'
import useArticlesStore from "@/store/articles.js";
import {getHomeArticlesList} from '@/api/articlesAPI.js'

let articlesStore = useArticlesStore()

onMounted(() => {
    getHomeArticlesList()
})

</script>

<template>

    <div class="home-container">
        <q-card class="notice-container" flat>
            这里是通知内容
        </q-card>

        <div class="popularity-comment">
            <q-card class="popularity-article-container">
                <q-card-section class="popularity-article-area">
                    <span class="popularity-article-area-title">热门文章</span>
                </q-card-section>
                <q-separator/>
                <q-card-section class="popularity-article-list-area">
                    <template v-for="(item, index) in articlesStore.homePopularityArticlesList" :key="index">
                        <div style="margin-bottom: 10px">
                            <span class="popularity-article-date">{{ item.updated_date }}</span>
                            <span class="popularity-article-title">{{ item.title }}</span>
                        </div>
                    </template>
                </q-card-section>
            </q-card>

            <q-card class="comment-container">
                <q-card-section class="comment-area">
                    <span class="comment-area-title">最新留言</span>
                </q-card-section>
                <q-separator/>
                <q-card-section class="comment-list-area">
                    <template v-for="(item, index) in articlesStore.homeLatestMessagesList" :key="index">
                        <div style="margin-bottom: 10px">
                            <span class="comment-content">{{ item.message_content }}</span>
                            <span class="comment-guest-name">{{ item.guest_name }}</span>
                        </div>
                    </template>
                </q-card-section>
            </q-card>

        </div>
        <div class="coding-product-english-area">

            <q-card class="coding-article-container">
                <q-card-section class="coding-article-area">
                    <span class="coding-article-area-title">编程相关</span>
                </q-card-section>
                <q-separator/>
                <q-card-section class="coding-article-list-area">
                    <template v-for="(item, index) in articlesStore.homeCodingLatestArticlesList" :key="index">
                        <div style="margin-bottom: 10px">
                            <span class="coding-article-date">{{ item.updated_date }}</span>
                            <span class="coding-article-title">{{ item.title }}</span>
                        </div>
                    </template>
                </q-card-section>
            </q-card>

            <q-card class="product-article-container">
                <q-card-section class="product-article-area">
                    <span class="product-article-area-title">产品相关</span>
                </q-card-section>
                <q-separator/>
                <q-card-section class="product-article-list-area">
                    <template v-for="(item, index) in articlesStore.homeProductLatestArticlesList" :key="index">
                        <div style="margin-bottom: 10px">
                            <span class="product-article-date">{{ item.updated_date }}</span>
                            <span class="product-article-title">{{ item.title }}</span>
                        </div>
                    </template>
                </q-card-section>
            </q-card>

            <q-card class="english-article-container">
                <q-card-section class="english-article-area">
                    <span class="english-article-area-title">英语相关</span>
                </q-card-section>
                <q-separator/>
                <q-card-section class="english-article-list-area">
                    <template v-for="(item, index) in articlesStore.homeEnglishLatestArticlesList" :key="index">
                        <div style="margin-bottom: 10px">
                            <span class="english-article-date">{{ item.updated_date }}</span>
                            <span class="english-article-title">{{ item.title }}</span>
                        </div>
                    </template>
                </q-card-section>
            </q-card>
            <div class="placeholder"></div>
        </div>


    </div>
</template>

<style scoped lang="scss">
.home-container {
    position: absolute;
    top: $header-high;
    left: 0;
    width: 75%;
    background-color: lightblue;

    .notice-container {
        position: absolute;
        top: 30px;
        left: 50px;
        width: 90%;
        font-size: 20px;
        font-weight: 600;
        background-color: teal;
        color: whitesmoke;
        padding: 10px;
    }

    .popularity-comment {
        position: absolute;
        top: 120px;
        left: 50px;
        width: 90%;

        .popularity-article-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 49%;
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));

            .popularity-article-area {
                .popularity-article-area-title {
                    font-size: 20px;
                }
            }

            .popularity-article-list-area {
                .popularity-article-date {
                    font-size: 14px;
                    margin-left: 30px;
                }

                .popularity-article-title {
                    font-size: 16px;
                    margin-left: 20px;
                    text-decoration: underline;
                }
            }
        }

        .comment-container {
            position: absolute;
            top: 0;
            right: 0;
            width: 49%;
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));

            .comment-area {
                .comment-area-title {
                    font-size: 20px;
                }
            }

            .comment-list-area {
                .comment-guest-name {
                    font-size: 14px;
                    margin-left: 30px;
                }

                .comment-content {
                    font-size: 16px;
                    margin-left: 20px;
                    text-decoration: underline;
                }
            }
        }
    }

    .coding-product-english-area {
        position: absolute;
        top: 410px;
        left: 50px;
        width: 90%;

        .coding-article-container {
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
            margin-bottom: 30px;

            .coding-article-area {
                .coding-article-area-title {
                    font-size: 20px;
                }
            }

            .coding-article-list-area {
                .coding-article-date {
                    font-size: 14px;
                    margin-left: 30px;
                }

                .coding-article-title {
                    font-size: 16px;
                    margin-left: 20px;
                    text-decoration: underline;
                }
            }
        }

        .product-article-container {
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
            margin-bottom: 30px;

            .product-article-area {
                .product-article-area-title {
                    font-size: 20px;
                }
            }

            .product-article-list-area {
                .product-article-date {
                    font-size: 14px;
                    margin-left: 30px;
                }

                .product-article-title {
                    font-size: 16px;
                    margin-left: 20px;
                    text-decoration: underline;
                }
            }
        }

        .english-article-container {
            margin-bottom: 30px;
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));

            .english-article-area {
                .english-article-area-title {
                    font-size: 20px;
                }
            }

            .english-article-list-area {
                .english-article-date {
                    font-size: 14px;
                    margin-left: 30px;
                }

                .english-article-title {
                    font-size: 16px;
                    margin-left: 20px;
                    text-decoration: underline;
                }
            }
        }

        .placeholder {
            height: 70px;
        }
    }

}
</style>