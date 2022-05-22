<template>
  <div class="choice">
    <ModalItem :show="showModal" :row="row" :col="col" />
  </div>
  <div :class="props.className" :id="idName" @click="click">
    {{ cellCurrentValue === 0 ? " " : cellCurrentValue }}
  </div>
</template>

<script setup lang="ts">
import { defineProps, ref, provide } from "vue";
import ModalItem from "./ModalItem.vue";
const showModal = ref(false);
const idName = ref("cell");

provide("showModal", showModal);

const props = defineProps<{
  cellCurrentValue: number | undefined;
  className: string;
  row?: number;
  col?: number;
}>();

function click() {
  if(props.className != 'cell__with__bg' || idName.value === "cell__mutable" ){ 
    showModal.value = true;
    idName.value = "cell__mutable";
  }
}
</script>

<style>
.cell {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  height: 50px;
  width: 50px;
  border: 2px solid black;
}
.cell__with__bg {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  height: 50px;
  width: 50px;
  background-color: #ff7147;
  border: 2px solid black;
}
.cell:hover {
  background-color: #55efc4;
}
#cell__mutable {
  background-color: #55efc4;
}
</style>
