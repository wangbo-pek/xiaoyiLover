<script setup>
import Title from "@/components/header_title.vue";
import Menu from "@/components/header-menu.vue";
import Action from "@/components/header-action.vue";

defineOptions({
    name: 'Layout'
})
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
                <div class="col-3 sidebar">sidebar</div>
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
            top:0;
            left:0;
            z-index: 99;
        }

        .menu {
            position: fixed;
            top:0;
            left:25%;
            z-index: 99;
        }

        .action {
            position: fixed;
            top:0;
            left:75%;
            z-index: 99;
        }
    }

    .placeholder {
        height: $header-high;
        position: fixed;
            top:0;
            left:0;
    }

    .middle {
        height: calc(100vh - $header-high - $footbar-high);


        .content {
            //background-color: #679864;
        }

        .sidebar {
            background-color: #a57fb2;
        }


    }


    .footer {
        height: $footbar-high;
        background-color: #7be7ef;
    }
}

</style>

