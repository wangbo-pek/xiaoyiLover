<script setup>
defineOptions({
    name: 'DiaryList'
})

import useDiaryStore from "@/store/diary.js";

let diaryStore = useDiaryStore()

</script>

<template>
    <div class="diary-container">
        <div class="row">
            <template v-for="(item, index) in diaryStore.diaryList" :key="index">
                <div class="col-4 diary-col">
                    <q-card class="diary-cell">
                        <div class="diary-date-area">
                            <span class="diary-date-text">{{ item.created_date }}</span>
                        </div>
                        <div class="diary-title-area">
                            <span class="diary-title-text">{{ item.title }}</span>
                        </div>
                        <q-img class="diary-cover" src="https://cdn.quasar.dev/img/parallax2.jpg" fit="cover"/>
                        <div class="weather-temperature-mood-area">
                            <span class="diary-weather">{{ item.weather }}</span>
                            <span class="diary-temperature">{{ item.temperature }}C°</span>
                            <span class="diary-mood">{{ item.mood }}</span>
                        </div>
                    </q-card>
                </div>
            </template>
        </div>
    </div>
</template>

<style scoped lang="scss">
.diary-container {
    position: absolute;
    top: 10px;
    left: 5%;
    width: 90%;

    .diary-col {
        margin-bottom: 45px;

        .diary-cell {
            width: 85%;
            height: 300px;
            background-image: linear-gradient(to right, rgba(96, 204, 213, 0.9), rgba(92, 220, 210, 0.87), rgba(94, 225, 179, 0.84));

            .diary-date-area {
                padding: 5px 0 5px 10px;

                .diary-date-text {
                    font-size: 16px;
                    font-weight: 700;
                }
            }

            .diary-title-area {
                padding: 5px 0 5px 10px;

                .diary-title-text {
                    font-size: 16px;
                    font-weight: 700;
                }
            }

            .diary-cover {

            }

            .weather-temperature-mood-area {
                padding: 5px 0 5px 10px;

                .diary-weather {
                    margin-right: 10px;
                    font-size: 14px;
                    font-weight: 300;
                }

                .diary-temperature {
                    margin-right: 10px;
                    font-size: 14px;
                    font-weight: 300;
                }

                .diary-mood {
                    margin-right: 10px;
                    font-size: 14px;
                    font-weight: 300;
                }
            }
        }

    }
}
</style>