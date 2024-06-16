import {defineStore} from "pinia";

let useTestStore = defineStore('useTestStore', {
    state() {
        return {
            testArticleContent:'# 测试测试测试4'
        }
    }
})

export default useTestStore