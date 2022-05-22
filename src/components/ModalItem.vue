/* eslint-disable no-undef */
<template>
  <teleport to="body">
    <div class="choice" v-if="show">
      <ChoiceCard
        :choices="[
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
        ]"
        :row="row"
        :col="col"
      />
    </div>
  </teleport>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import ChoiceCard from "./ChoiceCard.vue";

defineProps<{
  show: boolean;
  row?: number;
  col?: number;
}>();
</script>

<style scoped></style>
