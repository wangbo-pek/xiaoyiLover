<script setup>
defineOptions({
    name: 'Sidebar'
})
</script>

<template>
    <div class="sidebar-container">

        <div class="weather-container">
            <q-card class="weather-area">

                <div class="column weather-location-area">
                    <span class="weather-location">北京</span>
                </div>

                <div class="column weather-info-area">
                    <div class="row weather-info-area-row">
                        <div class="col-3">
                            <q-icon class="weather-icon" name="light_mode" size="50px"></q-icon>
                        </div>

                        <div class="col-5">
                            <div class="column temperature">
                                <span class="temperature-text">35C°</span>
                            </div>
                            <div class="column weather-info">
                                <span class="weather-info-text">晴转多云</span>
                            </div>
                        </div>

                        <div class="col-3">
                            <div class="column air_speed">
                                <span class="air-speed-text">风速</span>
                            </div>
                            <div class="column air_humidity">
                                <span class="air-humidity-text">60</span>
                            </div>
                            <div class="column air_quality">
                                <span class="air-quality-text">75</span>
                            </div>
                        </div>
                    </div>
                </div>
            </q-card>
        </div>

    </div>
</template>

<style scoped lang="scss">
</style>