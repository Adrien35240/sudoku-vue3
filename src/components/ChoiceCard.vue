<template>
    <div class="choice">
        <div class="choice__row" v-for="i in 3" :key="i">
            <div class="choice__col" v-for="j in 3" :key="j">
                <div
                    class="choice__cell"
                    @click="setCurrentCell(i, j, choices)"
                >
                    {{ choices[i - 1][j - 1] }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps, inject } from "vue";
const currentAnswer = inject("currentAnswer");
const solution = inject("solution");
const showModal = inject("showModal");
const props = defineProps<{
    choices: number[][] | undefined;
    row?: number;
    col?: number;
}>();
// TODO: delete numbers already used from choices

props.choices.map(choice=>{
  choice.map(res=>{
    console.log(res)
    console.log("currentAnswer",currentAnswer.value)

  })
})






// props.choices.map((array) =>
//     array.map((num) => {
//         console.log("num", num);
//         console.log(currentAnswer.value[0]);
//         currentAnswer.value[0].map((element, index) => {
//             console.log("element", element);
//             if (element === num) {
//                 props.choices[0][index + 1] = " ";
//             }
//         });
//     })
// );

function setCurrentCell(i: number, j: number, choices: any[][]) {
    showModal.value = false;
    currentAnswer.value[props.row - 1][props.col - 1] = choices[i - 1][j - 1];
    inject("currentAnswer", currentAnswer);
    console.log("slution", solution);
    if (JSON.stringify(currentAnswer.value) === JSON.stringify(solution)) {
        console.log("done!");
    }
}
</script>

<style scoped>
.choice {
}
.choice__row {
    display: flex;
}
.choice__cell {
    border: 1px solid #ff7147;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 45px;
    width: 45px;
}
.choice__cell:hover {
    background-color: #ff7147;
}
</style>
