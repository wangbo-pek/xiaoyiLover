import request from "@/utils/request.js";
import useArticlesStore from "@/store/articles.js";
import pinia from "@/store/index.js";
import {getAllCategory, getAllTag} from '@/api/get_articles.js'

let articlesStore = useArticlesStore(pinia)

async function createArticle(newArticle) {
    await request.post('/create_article/', newArticle).then(response=>{
        console.log(response)
    })
}

export {createArticle}