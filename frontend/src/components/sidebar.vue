<script setup>
defineOptions({
    name: 'Sidebar'
})

import {onMounted} from "vue";
import useExtraInfoStore from "@/store/extraInfo.js";

let extraInfoStore = useExtraInfoStore()


onMounted(() => {
    setInterval(() => {
        const randomElement = extraInfoStore.quotes[Math.floor(Math.random() * extraInfoStore.quotes.length)]
        extraInfoStore.quote = {
            author: randomElement.author,
            content: randomElement.content
        }
    }, 60000)
})

</script>

<template>
    <div class="sidebar-container">
        <div class="row weather-container">
            <div class="col-3 weather-icon">
                <q-icon name="light_mode" size="50px" color="teal-8"></q-icon>
            </div>
            <div class="col-3 temperature-weather-info">
                <div class="column temperature-info">
                    <span class="temperature-text">{{ extraInfoStore.weatherInfo.temperature }}C°</span>
                </div>

                <div class="column weather-info">
                    <span class="weather-text">{{ extraInfoStore.weatherInfo.weather }}</span>
                </div>
            </div>

            <div class="col-6 air-info">
                <div class="column air-speed-info">
                    <span class="air-speed-text">Air Speed: {{ extraInfoStore.weatherInfo.air_speed }}</span>
                </div>
                <div class="column air-quality-info">
                    <span class="air-quality-text">Air Quality: {{ extraInfoStore.weatherInfo.air_quality }}</span>
                </div>
                <div class="column air-humidity-info">
                    <span class="air-humidity-text">Air Humidity: {{ extraInfoStore.weatherInfo.air_humidity }}</span>
                </div>
            </div>
        </div>
        <div class="quotes-container">
            <div class="content-info">
                <span class="content-text">{{ extraInfoStore.quote.content }}</span>
            </div>
            <div class="author-info">
                <span class="author-text">—— {{ extraInfoStore.quote.author }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.sidebar-container {

    .weather-container {
        position: relative;
        top: 30px;
        right: -15px;
        width: 90%;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        padding: 15px 10px 15px 15px;
        border-radius: 10px;

        .weather-icon {
            padding-top: 6px;
            padding-left: 5px;
        }

        .temperature-weather-info {
            .temperature-info {
                .temperature-text {
                    font-size: 26px;
                }
            }

            .weather-info {
                .weather-text {
                    font-size: 14px;
                }
            }
        }

        .air-info {
            .air-speed-info {
                .air-speed-text {
                    font-size: 14px;
                }
            }

            .air-quality-info {
                .air-quality-text {
                    font-size: 14px;
                }
            }

            .air-humidity-info {
                .air-humidity-text {
                    font-size: 14px;
                }

            }
        }
    }

    .quotes-container {
        position: relative;
        top: 55px;
        right: -15px;
        width: 90%;
        background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));
        padding: 15px 10px 15px 15px;
        border-radius: 10px;

        .content-info {
            .content-text {
                font-size: 16px;
                font-weight: 700;
            }
        }

        .author-info {
            .author-text {
                position: relative;
                top: 0;
                right: -180px;
                font-size: 14px;
                font-weight: 700;
            }
        }
    }
}

</style>