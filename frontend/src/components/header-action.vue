<script setup>
defineOptions({
    name:'Action'
})
</script>

<template>
    <div class="action-btn">
        <q-btn class="icon-btn" size="12px" rounded icon="fingerprint"></q-btn>
        <q-btn class="icon-btn" size="12px" rounded icon="local_cafe"></q-btn>
        <q-btn class="icon-btn" size="12px" rounded icon="search"></q-btn>
    </div>

</template>

<style scoped lang="scss">
.action-btn {
    height: $header-high;
    line-height: $header-high;

    .icon-btn {
        margin-left: 20px;
    }
}
</style>