<script>
  import Table from '@/components/Table.vue'
  import Paginator from '@/components/Paginator.vue'
  import Filter from '@/components/Filter.vue'
  export default {
    name: 'Tables',
    data() {
      return {
        url: 'http://localhost:8000/api/v1/tables',
        tableList: {},
        pageNumber: this.$route.query.page || 1
      }
    },
    components: {Table, Paginator, Filter},
    created() {
      console.log(this.getQueryPage())
      this.loadTableList(this.url + this.getQueryPage())
    },
    methods: {
      async loadTableList(url=this.url) {
        let response = await fetch(url)
        this.tableList = await response.json()
          console.log(this.tableList)
      },
      getQueryPage() {
        if (!(this.$route.query.page > this.tableList.count) && (this.$route.query.page > 0)) {
          return `?page=${this.$route.query.page}`
        } else {
          this.$router.replace({ name: "tables", query: {} })
          return ''
        }
      },
      changePageNum(num) {
        this.pageNumber = num
      }
    },
  }
</script>

<template>
  <main>
    <Filter
      :pageNumber="this.pageNumber"
      @change-page-num="this.changePageNum"
      :url="url"
      @get-list="this.loadTableList"></Filter>
    <table  class="table">
      <thead>
        <tr>
          <th>Дата</th>
          <th>Название</th>
          <th>Количество</th>
          <th>Расстояние</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="table in tableList.results" :key="table">
          <Table :table="table"></Table>
        </tr>
        <Paginator
          :pageNumber="this.pageNumber"
          :prev="this.tableList.previous"
          :next="this.tableList.next"
          :count="this.tableList.count"
          :url="this.url"
          @change-page-num="this.changePageNum"
          @get-list="this.loadTableList"></Paginator>
      </tbody>
    </table>
  </main>
</template>
