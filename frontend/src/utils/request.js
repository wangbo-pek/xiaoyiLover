import axios from "axios";
import {Notify} from 'quasar'

let request = axios.create({
    baseURL: '',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': sessionStorage.getItem('csrf_token')
    },
    withCredentials: true
})

// 请求拦截器
request.interceptors.request.use(
    // 请求成功
    config => {

        if (config.method === 'post') {
            config.headers['X-CSRFToken'] = sessionStorage.getItem('csrf_token')
        }

        return config
    },
    // 请求失败
    error => {
        console.log('请求拦截器失败 >>', error)
    }
)

// 响应拦截器
request.interceptors.response.use(
    // 响应成功
    response => {
        return response.data
    },

    // 响应失败
    error => {
        let message = ''
        let status = error.response.status
        switch (status) {
            case 401:
                message = 'token过期'
                break
            case 403:
                message = '无权访问'
                break
            case 404:
                message = '地址错误'
                break
            case 500:
                message = '服务器问题'
                break
            default:
                message = '网络出现问题'
                break
        }
        Notify.create({
            message:message,
            icon:'error',
            iconColor:'grey-2',
            type:'negative',
            timeout:3000
        })

        return Promise.reject(error)
    }
)

export default request