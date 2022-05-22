/* eslint-disable no-undef */
<template>
  <div class="board">
    <span class="row" v-for="i in currentGrid.length" :key="i">
      <span class="col" v-for="j in currentGrid.length" :key="j"
        ><CellItem
          :className="
            currentGrid[i - 1][j - 1] != 0 ? 'cell__with__bg' : 'cell'
          "
          :cellCurrentValue="currentGrid[i - 1][j - 1]"
          :row="i"
          :col="j"
      /></span>
    </span>
  </div>
</template>

<script setup lang="ts">
import { inject } from "vue";
import CellItem from "./CellItem.vue";
const currentGrid = inject("currentAnswer");
</script>

<style scoped>
.row {
  display: flex;
  margin-bottom: -2px;
}
.row:nth-child(3n-9) {
  margin-bottom: 0px;
}
.col {
  margin-right: -2px;
}
.col:nth-child(3n-9) {
  margin-right: 0px;
}
.choice {
  position: absolute;
}
</style>
