import request from "@/utils/request.js";
import useArticlesStore from "@/store/articles.js";
import pinia from "@/store/index.js";

let articlesStore = useArticlesStore(pinia)

// 获取所有文章列表信息
function getArticlesList() {
    articlesStore.articlesList = []
    request.get('get_article_list').then(response => {
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
            console.log(articlesStore.articlesList)
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
        let newArticle = {
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
    })
}

// 删除文章
function deleteArticle(articleId, listIndex) {
    request.get(`/delete_article/${articleId}`).then(response=>{
        console.log(response)
        articlesStore.articlesList.splice(listIndex, 1)
    })
}

export {getArticlesList, getAllCategory, getAllTag, createArticle, deleteArticle}