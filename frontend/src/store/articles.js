import {defineStore} from "pinia";

let useArticlesStore = defineStore('useArticlesStore', {
    state() {
        return {
            articleObject: {
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
                levelFirstCategory:'No Data',
                levelSecondCategory:'No Data',
                tags: [],
            },
            articlesList: [],
            categoryList:[],
            subcategoryObject:{},
            tagsList:[]
        }
    }
})

export default useArticlesStore