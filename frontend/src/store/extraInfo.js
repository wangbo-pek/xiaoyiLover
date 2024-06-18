import {defineStore} from "pinia";

let useExtraInfoStore = defineStore('useExtraInfoStore', {
    state(){
        return {
            // 天气相关的信息
            weatherInfo:{
                weather:'',
                air_speed:'',
                air_quality:'',
                air_humidity:'',
                temperature:''
            }
        }
    }
})
export default useExtraInfoStore