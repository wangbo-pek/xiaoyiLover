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

    .create-btn {
        position: absolute;
        top: 15px;
        left: 50px;
        font-family: "Courier New",serif;
    }

    .category-selection{
        position: absolute;
        top: 15px;
        left: 170px;
        width: 300px;
        font-family: "Courier New",serif;
    }

    .tag-selection{
        position: absolute;
        top: 15px;
        left: 500px;
        width: 300px;
        font-family: "Courier New",serif;
    }
}
</style>