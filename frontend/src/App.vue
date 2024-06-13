<script setup>
import {onMounted} from "vue";
import request from "@/utils/request.js";
import {getAllCategory} from '@/api/get_articles.js'


function getToken() {
    request.get('/get_token/').then((response) => {
        let token = response.csrf_token
        console.log('@token >>', token)
        sessionStorage.setItem('csrf_token', token)
    })
}

onMounted(()=>{
    getToken()
    getAllCategory()
})
</script>

<template>
    <div style="font-family: Courier,serif">
        <router-view></router-view>
    </div>

</template>

<style lang="scss">
</style>

