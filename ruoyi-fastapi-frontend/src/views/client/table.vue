<template>
  <div>
    <el-button type="primary" @click="refreshTable">Refresh</el-button>
    <el-table v-loading="loading" :data="tableData" style="width: 100%">
      <el-table-column prop="name" label="Client" width="240" sortable/>
      <el-table-column prop="abn" label="ABN" width="240" />
      <el-table-column prop="contact" label="Contact" width="240" />
      <el-table-column prop="method" label="Method" width="240">
        <template #default="scope">
          <el-tag v-for="method in scope.row.method.split(',')" :key="method" type="success" style="margin-right: 4px;">
            {{ method }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="details" label="Details" width="300" />
      <el-table-column prop="client_id" label="Client ID" width="300" />
      <el-table-column fixed="right" label="Operations" min-width="120">
        <template #default="scope">
          <el-button link type="danger" @click="handleClick(scope.row)">
            Remove
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { getClientList, deleteClient } from '@/api/business/business'

const loading = ref(true)
const tableData = ref([])

const fetchClientList = async () => {
  loading.value = true
  try {
    const response = await getClientList()
    tableData.value = response || []
  } catch (error) {
    console.error('Failed to fetch client list:', error)
  } finally {
    loading.value = false
  }
}

const refreshTable = () => {
  fetchClientList()
}

const handleClick = async (row) => {
  try {
    console.log('Delete client:', row.client_id)
    await deleteClient({ id: row.client_id })
    refreshTable()
  } catch (error) {
    console.error('Failed to delete client:', error)
  }
}

onMounted(() => {
  fetchClientList()
})
</script>