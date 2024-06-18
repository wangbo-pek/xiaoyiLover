import request from "@/utils/request.js";
import useDiaryStore from "@/store/diary.js";
import pinia from "@/store/index.js";

let diaryStore = useDiaryStore(pinia)


// 获取所有日记列表信息
function getDiaryList() {
    request.get('/get_diary_list/').then(response => {
        console.log('@@@@getDiaryList@@@@')
        console.log(response)

        response.diaryList_data.forEach(value => {
            let item = {
                diary_id: value.diary_id,
                title: value.title,
                weather: value.weather,
                temperature: value.temperature,
                mood: value.mood,
                cover: value.cover,
                diary_text: value.diary_text,
                diary_html: value.diary_html,
                created_date: value.created_date.slice(0, 10)
            }
           diaryStore.diaryList.push(item)
        })
    })
}

export {getDiaryList}