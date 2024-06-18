import request from "@/utils/request.js";
import useArticlesStore from "@/store/articles.js";
import pinia from "@/store/index.js";

let articlesStore = useArticlesStore(pinia)

// 获取所有文章列表信息
async function getArticlesList() {
    await request.get('/get_articles_list/').then(response => {
        articlesStore.articlesList = []
        console.log('@@getArticlesList')
        console.log(response.articlesList_data)
        response.articlesList_data.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.articlesList.push(item)
        })
    })
}

// 获取文章分类
async function getAllCategory() {
    await request.get('/get_all_category/').then(response => {
        console.log('@@getAllCategory')
        console.log(response)
        articlesStore.categoryList = response.category_data
        articlesStore.subcategoryObject = response.subcategory_data
    })
}

// 获取文章标签
async function getAllTag() {
    await request.get('/get_all_tag/').then(response => {
        console.log('@@getAllTag')
        console.log(response)
        articlesStore.tagsList = response.tag_data
    })
}

// 创建文章
async function createArticle(newArticle) {
    await request.post('/create_article/', newArticle).then(response => {
        console.log(response)
        const newArticle = {
            article_id: response.newArticle_data.article_id,
            title: response.newArticle_data.title,
            subtitle: response.newArticle_data.subtitle,
            is_display: response.newArticle_data.is_display,
            updated_date: response.newArticle_data.updated_date.slice(0, 10),
            created_date: response.newArticle_data.created_date.slice(0, 10),
            subcategory: response.newArticle_data.subcategory,
            category: response.newArticle_data.category,
            tags: response.newArticle_data.tags
        }
        articlesStore.articlesList.push(newArticle)

        articlesStore.currentArticle.article_id = response.newArticle_data.article_id
        articlesStore.currentArticle.title = response.newArticle_data.title
        articlesStore.currentArticle.subtitle = response.newArticle_data.subtitle
        articlesStore.currentArticle.is_display = response.newArticle_data.is_display
        articlesStore.currentArticle.content_text = response.newArticle_data.content_text
        articlesStore.currentArticle.content_html = response.newArticle_data.content_html
        articlesStore.currentArticle.read_count = response.newArticle_data.read_count
        articlesStore.currentArticle.comment_count = response.newArticle_data.comment_count
        articlesStore.currentArticle.like_count = response.newArticle_data.like_count
        articlesStore.currentArticle.reprinted_count = response.newArticle_data.reprinted_count
        articlesStore.currentArticle.updated_date = response.newArticle_data.updated_date.slice(0, 10)
        articlesStore.currentArticle.created_date = response.newArticle_data.created_date.slice(0, 10)
        articlesStore.currentArticle.category = response.newArticle_data.category
        articlesStore.currentArticle.subcategory = response.newArticle_data.subcategory
        articlesStore.currentArticle.tags = response.newArticle_data.tags
    })
}

// 删除文章
async function deleteArticle(articleId, listIndex) {
    await request.get(`/delete_article/${articleId}`).then(response => {
        console.log(response)
        articlesStore.articlesList.splice(listIndex, 1)
    })
}

// 获取指定文章的信息
async function fetchArticle(articleId, index) {
    articlesStore.currentIndex = index
    console.log('index', index)
    console.log('articlesStore.currentIndex', articlesStore.currentIndex)
    await request.get(`/fetch_article/${articleId}/`).then(response => {
        console.log('@@viewArticle')
        console.log(response)
        articlesStore.currentArticle.article_id = articlesStore.articlesList[index].article_id
        articlesStore.currentArticle.title = articlesStore.articlesList[index].title
        articlesStore.currentArticle.subtitle = articlesStore.articlesList[index].subtitle
        articlesStore.currentArticle.is_display = articlesStore.articlesList[index].is_display
        articlesStore.currentArticle.content_text = response.article_info.content_text
        articlesStore.currentArticle.content_html = response.article_info.content_html
        articlesStore.currentArticle.read_count = response.article_info.read_count
        articlesStore.currentArticle.comment_count = response.article_info.comment_count
        articlesStore.currentArticle.like_count = response.article_info.like_count
        articlesStore.currentArticle.reprinted_count = response.article_info.reprinted_count
        articlesStore.currentArticle.updated_date = articlesStore.articlesList[index].updated_date
        articlesStore.currentArticle.created_date = articlesStore.articlesList[index].created_date
        articlesStore.currentArticle.category = articlesStore.articlesList[index].category
        articlesStore.currentArticle.subcategory = articlesStore.articlesList[index].subcategory
        articlesStore.currentArticle.tags = articlesStore.articlesList[index].tags
    })
}

// 修改指定文章
async function reviseArticle(toBeRevisedArticle) {
    console.log('articlesStore.currentIndex', articlesStore.currentIndex)
    await request.post('/revise_article/', toBeRevisedArticle).then(response => {
        console.log('@@reviseArticle')
        console.log(response)
        articlesStore.articlesList[articlesStore.currentIndex].title = response.revisedArticle_data.title
        articlesStore.articlesList[articlesStore.currentIndex].subtitle = response.revisedArticle_data.subtitle
        articlesStore.articlesList[articlesStore.currentIndex].is_display = response.revisedArticle_data.is_display
        articlesStore.articlesList[articlesStore.currentIndex].updated_date = response.revisedArticle_data.updated_date.slice(0, 10)
        articlesStore.articlesList[articlesStore.currentIndex].created_date = response.revisedArticle_data.created_date.slice(0, 10)
        articlesStore.articlesList[articlesStore.currentIndex].subcategory = response.revisedArticle_data.subcategory
        articlesStore.articlesList[articlesStore.currentIndex].category = response.revisedArticle_data.category
        articlesStore.articlesList[articlesStore.currentIndex].tags = response.revisedArticle_data.tags

        articlesStore.currentArticle.article_id = articlesStore.articlesList[articlesStore.currentIndex].article_id
        articlesStore.currentArticle.title = response.revisedArticle_data.title
        articlesStore.currentArticle.subtitle = response.revisedArticle_data.subtitle
        articlesStore.currentArticle.is_display = response.revisedArticle_data.is_display
        articlesStore.currentArticle.content_text = response.revisedArticle_data.content_text
        articlesStore.currentArticle.content_html = response.revisedArticle_data.content_html
        articlesStore.currentArticle.read_count = articlesStore.articlesList[articlesStore.currentIndex].read_count
        articlesStore.currentArticle.comment_count = articlesStore.articlesList[articlesStore.currentIndex].comment_count
        articlesStore.currentArticle.like_count = articlesStore.articlesList[articlesStore.currentIndex].like_count
        articlesStore.currentArticle.reprinted_count = articlesStore.articlesList[articlesStore.currentIndex].reprinted_count
        articlesStore.currentArticle.updated_date = response.revisedArticle_data.updated_date.slice(0, 10)
        articlesStore.currentArticle.created_date = response.revisedArticle_data.created_date.slice(0, 10)
        articlesStore.currentArticle.category = response.revisedArticle_data.category
        articlesStore.currentArticle.subcategory = response.revisedArticle_data.subcategory
        articlesStore.currentArticle.tags = response.revisedArticle_data.tags
    })
}

// 筛选文章
async function filterArticles(filterCondition) {
    await request.get('/filter_article/', {params: filterCondition}).then(response => {
        articlesStore.articlesList = []
        console.log('@@filterArticle')
        console.log(response)
        response.articlesList_data.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.articlesList.push(item)
        })
    })
}

// 获取首页文章和留言
async function getHomeArticlesList() {
    await request.get('/get_home_articles_list/').then(response => {
        articlesStore.homePopularityArticlesList = []
        articlesStore.homeCodingLatestArticlesList = []
        articlesStore.homeProductLatestArticlesList = []
        articlesStore.homeEnglishLatestArticlesList = []
        articlesStore.homeLatestMessagesList = []
        console.log('@@getHomeArticlesList')
        console.log(response)
        response.popularityArticlesList.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.homePopularityArticlesList.push(item)
        })

        response.codingLatestArticlesList.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.homeCodingLatestArticlesList.push(item)
        })

        response.productLatestArticlesList.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.homeProductLatestArticlesList.push(item)
        })

        response.englishLatestArticlesList.forEach(value => {
            let item = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                subcategory: value.subcategory,
                category: value.category,
                tags: value.tags
            }
            articlesStore.homeEnglishLatestArticlesList.push(item)
        })

        response.homeLatestMessagesList.forEach(value => {
            let item = {
                message_id: value.message_id,
                message_content: value.message_content,
                created_date: value.created_date,
                guest_name: value.guest_name
            }
            articlesStore.homeLatestMessagesList.push(item)
        })
    })
}

export {
    getArticlesList,
    getAllCategory,
    getAllTag,
    createArticle,
    deleteArticle,
    fetchArticle,
    reviseArticle,
    filterArticles,
    getHomeArticlesList,
}