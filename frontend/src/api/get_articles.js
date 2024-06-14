import request from "@/utils/request.js";
import useArticlesStore from "@/store/articles.js";
import pinia from "@/store/index.js";

let articlesStore = useArticlesStore(pinia)

async function getAllArticles() {
    await request.get('/get_all_articles/').then(response => {
        console.log('@@getAllArticles')
        console.log(response.articles_data)
        response.articles_data.forEach(value => {
            let article = {
                article_id: value.article_id,
                title: value.title,
                subtitle: value.subtitle,
                is_display: value.is_display,
                content_text: value.content_text,
                content_html: value.content_html,
                short_content: function () {
                    if (value.content_html.length < 200) {
                        return value.content_html
                    } else {
                        return `${value.content_html.substring(0, 201)} ...`
                    }
                }(),
                read_count: value.read_count,
                comment_count: value.comment_count,
                like_count: value.like_count,
                reprinted_count: value.reprinted_count,
                updated_date: value.updated_date.slice(0, 10),
                created_date: value.created_date.slice(0, 10),
                levelFirstCategory: value.levelFirstCategory,
                levelSecondCategory: value.levelSecondCategory,
                tags: []
            }
            value.tags.forEach(tag => {
                article.tags.push(tag)
            })
            articlesStore.articlesList.push(article)
        })
        console.log('##gotAllArticles')
        console.log(articlesStore.articlesList)
    })
}

async function getAllCategory() {
    await request.get('/get_all_category/').then(response=>{
        console.log('@@getAllCategory')
        console.log(response)
        articlesStore.categoryList = response.category_data
        articlesStore.subcategoryObject = response.subcategory_data
    })
}

async function getAllTag() {
    await request.get('/get_all_tag/').then(response=>{
        console.log('@@getAllTag')
        console.log(response)
        articlesStore.tagsList = response.tag_data
    })
}
export {getAllArticles, getAllCategory, getAllTag}