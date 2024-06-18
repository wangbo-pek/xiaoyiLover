import request from '@/utils/request.js'
import pinia from "@/store/index.js";
import useExtraInfoStore from "@/store/extraInfo.js";

let extraInfoStore = useExtraInfoStore(pinia)


// 获取天气信息
async function fetchWeatherInfo() {
    await request.get('/api/weather/').then(response => {
        extraInfoStore.weatherInfo.weather = response.result.realtime.info
        extraInfoStore.weatherInfo.air_speed = response.result.realtime.power
        extraInfoStore.weatherInfo.air_quality = response.result.realtime.aqi
        extraInfoStore.weatherInfo.air_humidity = response.result.realtime.humidity
        extraInfoStore.weatherInfo.temperature = response.result.realtime.temperature
        console.log('@@@ weather')
        console.log(extraInfoStore.weatherInfo)
    })
}

// 获取名人名言
async function fetchQuotes() {
    await request.get('/api/quotes/').then(response => {
        console.log('@@@@@@@fetchQuotes@@@@@@@')
        console.log(response)

        response.quotes.forEach(value => {
            value.result.list.forEach(v => {
                let newQuote = {
                    author: v.author,
                    content: v.content
                }
                extraInfoStore.quotes.push(newQuote)
            })
        })

        const randomElement = extraInfoStore.quotes[Math.floor(Math.random() * extraInfoStore.quotes.length)]
        extraInfoStore.quote = {
            author: randomElement.author,
            content: randomElement.content
        }
        console.log('@@@ quotes')
        console.log(extraInfoStore.quotes)
    })
}

export {fetchWeatherInfo, fetchQuotes}