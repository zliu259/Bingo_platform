<template>
  <div id="container">
    <div id="table-container">
      <Table ref="tableRef" id="table"></Table>
    </div>
    <div id="form-container">
      <Form @providerCreated="handleProviderCreated" id="form"></Form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Table from './table.vue'
import Form from './form.vue'

const tableRef = ref(null)

const handleProviderCreated = () => {
  tableRef.value.fetchProviders()
}
</script>

<style scoped lang="scss">
#container {
  display: flex;
  justify-content: space-between;
}

#table-container {
  flex: 2;
  margin-right: 20px;
}

#form-container {
  flex: 1;
}
</style>