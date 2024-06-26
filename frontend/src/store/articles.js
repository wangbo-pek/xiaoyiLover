import {defineStore} from "pinia";

let useArticlesStore = defineStore('useArticlesStore', {
    state() {
        return {
            // 文章列表数据
            articlesList: [],

            // 即将view、edit、delete的文章数据
            currentArticle: {
                article_id: -1,
                title: 'No Data',
                subtitle: 'No Data',
                is_display: '-1',
                content_text: 'No Data',
                content_html: 'No Data',
                read_count: '-1',
                comment_count: '-1',
                like_count:'-1',
                reprinted_count: '-1',
                updated_date: 'No Data',
                created_date: 'No Data',
                category:'No Data',
                subcategory:'No Data',
                tags: [],
            },

            // 即将view、edit、delete的文章在store列表中的index
            currentIndex:-1,

            // 所有的文章1级分类
            categoryList:[],
            // 所有的文章2级分类
            subcategoryObject:{},

            // 所有的文章标签
            tagsList:[],

            // 首页文章：最热5篇
            homePopularityArticlesList:[],

            // 首页文章：coding最新3篇
            homeCodingLatestArticlesList:[],

            // 首页文章：product最新3篇
            homeProductLatestArticlesList:[],

            // 首页文章：english最新3篇
            homeEnglishLatestArticlesList:[],

            // 首页留言：留言最新5条
            homeLatestMessagesList:[],
        }
    },
})

export default useArticlesStore