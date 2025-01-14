<template>
  <div id="table" v-loading="loading">
    <el-table :data="providers" style="width: 100%">
      <el-table-column prop="name" label="Name" width="300" />
      <el-table-column prop="address" label="Address" />
      <el-table-column prop="contact" label="Contact" />
      <el-table-column prop="abn" label="ABN" />
      <el-table-column prop="bank" label="Bank" />
      <el-table-column prop="account" label="Account" />
      <el-table-column prop="bsb" label="BSB" />
      <el-table-column prop="id" label="ID" />
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted, defineExpose } from 'vue'
import { getProviderList } from '@/api/business/business.js'
import { ElLoading } from 'element-plus'

const providers = ref([])
const loading = ref(true)

const fetchProviders = async () => {
  try {
    const response = await getProviderList()
    providers.value = response
  } catch (error) {
    console.error('Failed to fetch providers:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProviders()
})

defineExpose({
  fetchProviders
})
</script>

<style scoped lang="scss">
#table {
  padding: 20px;
}
/* Add your styles here */
</style>