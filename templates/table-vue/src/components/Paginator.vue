<script setup>
defineProps({
  count: {
    type: Number,
    required: true
  },
  next: {
      type: String,
  },
  prev: {
      type: String
  },
  url: {
      type: String
  },
  pageNumber: {
      type: Number,
  }
})
defineEmits(['get-list', 'change-page-num'])
</script>
<script>
export default {
    methods: {
        nextPage() {
            this.$emit('get-list', this.next)
            this.$emit('change-page-num', this.pageNumber+1)
            this.$router.replace({ name: "tables", query: {page: this.pageNumber}})
        },
        prevPage() {
            this.$emit('get-list', this.prev)
            this.$emit('change-page-num', this.pageNumber-1)
            this.$router.replace({ name: "tables", query: {page: this.pageNumber}})
        }
    }

}
</script>

<template>
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link" href="#" v-if="prev" @click="prevPage()" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li class="page-item" :class="{active: i == this.pageNumber}"><a class="page-link" href="#">{{ pageNumber }}</a></li>
    <li class="page-item">
      <a class="page-link" href="#" v-if="next" @click="nextPage()" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
</template>
