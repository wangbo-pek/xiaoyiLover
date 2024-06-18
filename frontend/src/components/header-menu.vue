<script setup>
defineOptions({
    name: 'Menu'
})
</script>

<template>
    <div class="menu-btn">
        <q-btn
            flat
            class="articles-btn"
            size="20px"
            label="Article"
            :to="{name:'articles'}"
        ></q-btn>

        <q-btn
            flat
            class="tags-btn"
            size="20px"
            label="Tags"
            :to="{name:'tags'}"
        ></q-btn>

        <q-btn
            flat
            class="diary-btn"
            size="20px"
            label="Diary"
            :to="{name:'diary'}"
        ></q-btn>

        <q-btn
            flat
            class="about-btn"
            size="20px"
            label="About"
            :to="{name:'about'}"
        ></q-btn>

    </div>
</template>

<style scoped lang="scss">
.menu-btn {
    font-family: "Courier",serif;
    height: $header-high;
    line-height: $header-high;

    .articles-btn {
        text-transform: none;
        margin-left: 2px;
        width: 120px;
    }

    .tags-btn {
        text-transform: none;
        margin-left: 2px;
        width: 120px;
    }

    .diary-btn {
        text-transform: none;
        margin-left: 2px;
        width: 120px;
    }

    .about-btn {
        text-transform: none;
        margin-left: 2px;
        width: 120px;
    }
}
</style>