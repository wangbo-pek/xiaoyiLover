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
            },

            // 名人名言信息
            quotes:[],
            // 当前展示的名人名言
            quote:{},
        }
    }
})
export default useExtraInfoStore