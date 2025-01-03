<template>
  <div>
    <div id="header">
      <h1>Client List</h1>
      <el-button class="button" type="primary" @click="refreshTable">Refresh</el-button>
    </div>
    <el-table v-loading="loading" :data="tableData" style="width: 100%">
      <el-table-column prop="name" label="Client" sortable/>
      <el-table-column prop="abn" label="ABN" />
      <el-table-column prop="contact" label="Contact" />
      <el-table-column prop="method" label="Method">
        <template #default="scope">
          <el-tag v-for="method in scope.row.method.split(',')" :key="method" type="success" style="margin-right: 4px;">
            {{ method }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="details" label="Details" />
      <el-table-column prop="client_id" label="Client ID" />
      <el-table-column fixed="right" label="Operations">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="handleEdit(scope.row)">
            Edit
          </el-button>
          <el-button link type="danger" size="small" @click="handleClick(scope.row)">
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
import { useClientStore } from '@/store/clientStore'

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

const clientStore = useClientStore()
const handleEdit = (row) => {
  clientStore.setClient(row)
}

onMounted(() => {
  fetchClientList()
})
</script>

<style>
#header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-left: 10px;
  margin-bottom: 10px;
}
</style>