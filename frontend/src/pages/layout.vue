<script setup>

defineOptions({
    name: 'Layout'
})

import Title from "@/components/header_title.vue";
import Menu from "@/components/header-menu.vue";
import Action from "@/components/header-action.vue";
import Sidebar from "@/components/sidebar.vue";

</script>

<template>
    <div class="container desktop-only">
        <div class="column header">
            <div class="row">
                <div class="col-3 title">
                    <Title></Title>
                    <q-separator/>
                </div>
                <div class="col-6 menu">
                    <Menu></Menu>
                    <q-separator/>
                </div>
                <div class="col-3 action">
                    <Action></Action>
                    <q-separator/>
                </div>
            </div>
        </div>

        <div class="column placeholder"></div>

        <div class="column middle">
            <div class="row">
                <div class="col-9 content">
                    <router-view></router-view>
                </div>
                <div class="col-3 sidebar">
                    <Sidebar></Sidebar>
                </div>
            </div>
        </div>

        <div class="column fixed-bottom footer">
            footer
        </div>

    </div>
</template>

<style lang="scss" scoped>
.container {

    .header {
        height: $header-high;

        .title {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 99;
            background-image: linear-gradient(to right, rgba(90, 215, 215, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 205, 0.84));
        }

        .menu {
            position: fixed;
            top: 0;
            left: 25%;
            z-index: 99;
            background-image: linear-gradient(to right, rgba(96, 225, 205, 0.81), rgba(98, 230, 200, 0.79), rgba(100, 235, 195, 0.76));
        }

        .action {
            position: fixed;
            top: 0;
            left: 75%;
            z-index: 99;
            background-image: linear-gradient(to right, rgba(102, 235, 195, 0.73), rgba(104, 240, 190, 0.7), rgba(106, 245, 185, 0.67));
        }
    }

    .placeholder {
        height: $header-high;
        position: fixed;
        top: 0;
        left: 0;
    }

    .middle {
        height: calc(100vh - $header-high - $footbar-high);


        .content {
            //background-color: #679864;
        }

        .sidebar {
            position: fixed;
            top: $header-high;
            right: 0;
        }
    }

    .footer {
        height: $footbar-high;
        background-image: linear-gradient(to right, rgba(1, 201, 201, 0.8), rgba(1, 201, 178, 0.8), rgba(1, 201, 201, 0.8));
    }
}

</style>

