<script setup>
defineOptions({
    name: 'DiaryActionBar'
})
</script>

<template>
    <div class="actionbar-container">
        <div class="create-btn">
            <q-btn
                class="create"
                size="10px"
                icon="edit_note"
                :to="{name:'create'}">
            </q-btn>
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
    background-color: rgba(255, 255, 255, 0.75);

    .create-btn {
        position: fixed;
        top: 102px;
        left: 990px;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        color: #5c7370;
    }
}
</style>