import {defineStore} from "pinia";

let useDiaryStore = defineStore('useDiaryStore', {
    state() {
        return {
            // 日记列表数据
            diaryList: [],
        }
    }
})

export default useDiaryStore