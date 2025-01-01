<template>
  <div v-if="dataLoaded">
    <el-table
        :data="filteredData"
        style="width: 100%"
    >
      <el-table-column type="expand">
        <template #default="{ row }">
          <el-steps
                :active="row.status - 1"
                finish-status="success"
                align-center
                :space="200"
          >
            <el-step title="Quotation" />
            <el-step title="Payment" />
            <el-step title="Working" />
            <el-step title="Reviewing" />
            <el-step title="Documenting" />
            <el-step title="Delivering" />
          </el-steps>
          <div class="card">
            <el-card style="width: 49%">
              <template #header>
                <div class="card-header">
                  <span><strong>Project Info</strong></span>
                </div>
              </template>
              <p class="text item">Project ID: <strong>{{ row.job_id }}</strong></p>
              <p class="text item">Date: <strong>{{ row.date }}</strong></p>
              <p class="text item">Due: <strong>{{ row.due_date }}</strong></p>
              <p class="text item">Created by: <strong>{{ row.created_by }}</strong></p>
            </el-card>
            <el-card style="width: 49%">
              <template #header>
                <div class="card-header">
                  <span><strong>Client Info</strong></span>
                </div>
              </template>
              <p class="text item">Client: <strong>{{ row.client }}</strong></p>
              <p class="text item">Contact: <strong>{{ row.contact_person }}</strong></p>
              <p class="text item">Detail: <strong>{{ row.contact_details }}</strong></p>
              <p class="text item">
                <el-tag id="tag" v-for="method in row.contact_method.replace(/^\[|\]$/g, '').split(',')" :key="method">{{ method }}</el-tag>
              </p>
            </el-card>
          </div>
          <el-card style="width: 95%; margin: 20px">
            <p class="text item">Description: <strong>{{ row.Description }}</strong></p>
            <p class="text item">Note: <strong>{{ row.Remark }}</strong></p>
          </el-card>
        </template>
      </el-table-column>
      <el-table-column label="Status" prop="status" />
      <el-table-column label="Date" prop="date" />
      <el-table-column label="Type" prop="job_type" />
      <el-table-column label="Client" prop="client" />

      <el-table-column align="right">
        <template #header>
          <el-input v-model="search" placeholder="Type to search" />
        </template>
        <template #default="scope">
          <el-button type="primary" @click="handleEdit(scope.$index, scope.row)">
            Details
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
  <div v-else>
    <el-result icon="info" title="Loading Data">
      <template #sub-title>

        <p>Please Wait</p>
      </template>
    </el-result>
    <el-progress
        :percentage="100"
        status="success"
        :indeterminate="true"
        :duration="5"
    />
  </div>
</template>

<script lang="ts" setup>
import { computed, ref, onMounted } from 'vue'
import { getProjectList } from '@/api/business/business'


interface User {
  date: string
  type: string
  name: string
  address: string
  status: string
  client: string
  job_type: string
  job_id: string
  contact_method: string
}

const search = ref('')
const tableData = ref<User[]>([])
const dataLoaded = ref(false)

const filteredData = computed(() => {
  if (!search.value) {
    return tableData.value
  }
  return tableData.value.filter(item =>
    Object.values(item).some(val =>
      String(val).toLowerCase().includes(search.value.toLowerCase())
    )
  )
})

const handleEdit = (index: number, row: User) => {
  console.log(index, row)
}

onMounted(async () => {
  try {
    const response = await getProjectList()
    console.log('API Response:', response)
    tableData.value = response || []
    dataLoaded.value = true
    console.log('tableData:', tableData.value)
  } catch (error) {
    console.error('Failed to fetch project list:', error)
    tableData.value = []
    dataLoaded.value = true
  }
})
</script>

<style scoped>
.card {
  display: flex;
  justify-content: space-between;
  margin: 20px;
}
#tag {
  margin-right: 5px;
}
</style>