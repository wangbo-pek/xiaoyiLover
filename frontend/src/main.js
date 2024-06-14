import {createApp} from 'vue'
import App from './App.vue'

import {Notify, Quasar} from 'quasar'
import quasarLang from 'quasar/lang/zh-CN'
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'

import router from "@/router/index.js";
import pinia from "@/store/index.js";


const app = createApp(App)

app.use(Quasar, {
    plugins: {Notify},
    lang: quasarLang,
})

app.use(pinia)
app.use(router)

app.mount('#app')