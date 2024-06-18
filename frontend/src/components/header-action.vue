<script setup>
defineOptions({
    name: 'Action'
})


import {reactive} from "vue";

let searchInputValue = reactive({
    value:null,
    isShow:false
})

</script>

<template>
    <div class="action-btn">
        <q-btn
            class="search-btn"
            size="10px"
            rounded
            icon="search"
            @click="searchInputValue.isShow=true"
        ></q-btn>
        <q-input
            class="search-input"
            v-if="searchInputValue.isShow"
            v-model="searchInputValue.value"
            dense
            clearable
            autofocus
            @blur="searchInputValue.isShow=false;searchInputValue.value=null"
        ></q-input>
        <q-btn
            class="access-btn"
            size="10px"
            rounded
            icon="fingerprint"
        ></q-btn>
        <q-btn
            class="coffee-btn"
            size="10px"
            rounded
            icon="local_cafe"
        ></q-btn>

        <q-btn
            class="message-btn"
            size="10px"
            rounded
            icon="forum"
        ></q-btn>
    </div>

</template>

<style scoped lang="scss">
.action-btn {
    height: $header-high;
    line-height: $header-high;

    .search-btn {
        position: fixed;
        top:30px;
        right:550px;
        margin-left: 20px;
        background-color: teal;
        color: #d3dede;
    }

    .search-input {
        position: fixed;
        top:20px;
        right:265px;
        width: 18%;
        color: teal;
    }

    .access-btn {
        position: fixed;
        top:30px;
        right:10px;
        margin-left: 20px;
        background-color: teal;
        color: #d3dede;
    }

    .coffee-btn {
        position: fixed;
        top:30px;
        right:85px;
        margin-left: 20px;
        background-color: teal;
        color: #d3dede;
    }

    .message-btn {
        position: fixed;
        top:30px;
        right:160px;
        margin-left: 20px;
        background-color: teal;
        color: #d3dede;
    }
}
</style>