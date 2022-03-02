<script setup>
defineProps({url: {
    type: String,
    required: true
}})
defineEmits(['get-list', 'change-page-num'])
</script>
<script>
export default {
    data() {
        return {
            column: '',
            condition: '',
            value: ''
        }
    },
    methods: {
        filter() {
            let queries = {
                key: `${this.column}${this.condition ? '__' + this.condition : ''}`,
                value: this.value,
                page: 1
            }
            this.$emit('change-page-num', 1)
            this.$router.replace({ name: "tables", query: queries })
            let query = `?${queries.key}=${queries.value}`
            this.$emit('get-list', this.url + query)
        },
        changeValueType() {
            let value = document.querySelector('#value')

            switch(this.column) {
                case 'title':
                    value.type = 'text'
                    break;
                case 'date':
                    value.type = 'date'
                    break;
                default:
                    value.type = 'number'
                    break;
                
            }
        }
    }
}
</script>

<template>
  <form class="row g-3" @submit.prevent="filter()">
      <div class="col-auto">
        <select class="form-control" v-model="column" @change="changeValueType()" name="column" required>
            <option value="">-</option>
            <option value="date">Дата</option>
            <option value="title">Название</option>
            <option value="quantity">Количество</option>
            <option value="distance">Расстояние</option>
        </select>
      </div>
      <div class="col-auto">
        <select class="form-control" v-model="condition" name="condition">
            <option value="">Равно</option>
            <option value="contains">Содержит</option>
            <option value="gt">Больше</option>
            <option value="lt">Меньше</option>
        </select>
      </div>
      <div class="col-auto">
        <input id="value" class="form-control" v-model="value" name="value" required>
      </div>
      <div class="col-auto">
        <button class="btn btn-primary" type="vutton" >Фильтровать</button>
      </div>
  </form>
</template>
