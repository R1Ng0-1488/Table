<script setup>
defineProps({
  table: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <th>{{ table.date }}</th>
  <th>{{ table.title }}</th>
  <th>{{ table.quantity }}</th>
  <th>{{ table.distance }}</th>
</template>

