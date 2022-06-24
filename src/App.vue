<script setup lang="ts">
import BoardTemplate from "./components/BoardItem.vue";
import { default as data } from "./utils/data.json";
import { ref, provide } from "vue";
let puzzle = data.puzzle;
const currentAnswer = ref(puzzle);
provide("currentAnswer", currentAnswer);
//provide("solution", data.solution);
</script>

<template>
  <div class="app">
    <h2 class="title">Sudoku</h2>
    <BoardTemplate :data="data" />
    <p>
      Build with <a href="httnps://vuejs.org/" target="_blank">Vue3</a> | Hosted
      on <a href="https://vercel.com/" target="_blank">Vercel</a> Made by
      <a href="https://github.com/Adrien35240" target="_blank">@Adrien35240</a>
    </p>
  </div>
</template>

<style>
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title{
  font-size: 2rem;
  margin: 1rem;
  font-weight: bold;
}
h2 {
  text-align: center;
}
p {
  margin-top: 1rem;
  width: 200px;
}
</style>
