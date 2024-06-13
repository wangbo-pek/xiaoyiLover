<script setup>
defineOptions({
    name: 'Title'
})

import {useRouter} from "vue-router";

const $router = useRouter()
function jumpToHome() {
    $router.push({
        name:'home'
    })
}
</script>

<template>
    <div class="menu-title">
        <span class="title-btn cursor-pointer" @click="jumpToHome">xiaoyi_love</span>
    </div>
</template>

<style scoped lang="scss">
.menu-title {
    height: $header-high;
    line-height: $header-high;

    .title-btn {
        text-transform: none;
        width: 300px;
        margin-left: 70px;
        font-family: "Nanum Pen Script",cursive;
        font-size: 50px;
    }
}


</style>