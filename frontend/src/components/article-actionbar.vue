<script setup>
defineOptions({
    name: 'ArticleActionBar'
})

import {reactive, ref} from 'vue'

let d = [
    '1',
    '2',
    '3'
]

let e = ref(undefined)

</script>

<template>
    <div class="actionbar-container">

        <div class="create-btn">
            <q-btn
                class="c-btn"
                size="15px"
                label="Create"
                color="teal-5"
                text-color="black"
                :to="{name:'create'}"

            ></q-btn>
        </div>

        <div class="category-selection">
            <q-select
                class="c-selection"
                v-model="e"
                :options="d"
                label="Filter Category"
                outlined
                label-color="black"
                bg-color="teal-5"
                color="white"
                dense
                clearable
            ></q-select>
        </div>

        <div class="tag-selection">
            <q-select
                class="t-selection"
                v-model="e"
                :options="d"
                label="Filter Tag"
                standout
                label-color="black"
                bg-color="teal-5"
                color="white"
                dense
                clearable
            ></q-select>
        </div>

    </div>
</template>

<style scoped lang="scss">
.actionbar-container {
    position: fixed;
    top: $header-high;
    left: 0;
    width: 75%;
    height: 70px;
    z-index: 98;
    background-image: linear-gradient(to right, rgba(255, 255, 255, 0.9), rgba(250, 245, 250, 0.85), rgba(250, 250, 245, 0.8), rgba(255, 255, 255, 0.75));

    .create-btn {
        position: fixed;
        top: 95px;
        left: 50px;

    }

    .category-selection {
        position: fixed;
        top: 95px;
        left: 170px;
        width: 300px;
    }

    .tag-selection {
        position: fixed;
        top: 95px;
        left: 500px;
        width: 300px;
    }
}
</style>