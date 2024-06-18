import request from '@/utils/request.js'
import pinia from "@/store/index.js";
import useExtraInfoStore from "@/store/extraInfo.js";

let extraInfoStore = useExtraInfoStore()

// 获取天气信息
function fetchWeatherInfo() {
    request.get('/api/weather/').then(response => {
        extraInfoStore.weatherInfo.weather = response.result.realtime.info
        extraInfoStore.weatherInfo.air_speed = response.result.realtime.power
        extraInfoStore.weatherInfo.air_quality = response.result.realtime.aqi
        extraInfoStore.weatherInfo.air_humidity = response.result.realtime.humidity
        extraInfoStore.weatherInfo.temperature = response.result.realtime.temperature
        console.log('@@@ weather')
        console.log(extraInfoStore.weatherInfo)
    })
}

export {fetchWeatherInfo}