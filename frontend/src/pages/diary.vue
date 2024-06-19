<script setup>

defineOptions({
    name: 'Diary'
})

import DiaryActionBar from "@/components/diary-actionbar.vue";
import DiaryList from "@/components/diary-list.vue";



</script>

<template>
    <div class="diary-container desktop-only">
        <div class="column diary-actionbar">
            <DiaryActionBar></DiaryActionBar>
        </div>
        <div class="column diary-list">
            <DiaryList></DiaryList>
        </div>
    </div>
    <div class="placeholder"></div>
</template>

<style scoped lang="scss">

.diary-container {
    .diary-actionbar {
        position: absolute;
        top: $header-high;
        left: 0;
        width: 75%;
        height: $actionbar-high;
    }

    .diary-list {
        position: absolute;
        top: calc($header-high + $actionbar-high);
        left: 0;
        width: 75%;
        height: 100vh;
    }
}
</style>