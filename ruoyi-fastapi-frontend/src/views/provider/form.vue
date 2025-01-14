<template>
  <el-form :model="provider" label-width="120px">
    <h1 class="h1">New Provider</h1>
    <el-form-item label="ID">
      <el-input v-model="provider.id" readonly></el-input>
    </el-form-item>
    <el-form-item label="Name">
      <el-input v-model="provider.name"></el-input>
    </el-form-item>
    <el-form-item label="ABN">
      <el-input v-model="provider.abn"></el-input>
    </el-form-item>
    <el-form-item label="Address">
      <el-input v-model="provider.address"></el-input>
    </el-form-item>
    <el-form-item label="Contact">
      <el-input v-model="provider.contact"></el-input>
    </el-form-item>
    <el-form-item label="Bank">
      <el-input v-model="provider.bank"></el-input>
    </el-form-item>
    <el-form-item label="BSB">
      <el-input v-model="provider.bsb"></el-input>
    </el-form-item>
    <el-form-item label="Account">
      <el-input v-model="provider.account"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue'
import { v7 as uuidv7 } from 'uuid'
import { createProvider } from '@/api/business/business.js'
import { ElMessage, ElLoading } from 'element-plus'

const emit = defineEmits(['providerCreated'])

const provider = ref({
  id: uuidv7(),
  name: '',
  abn: '',
  address: '',
  contact: '',
  bank: '',
  bsb: '',
  account: ''
})

const submitForm = async () => {
  const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  try {
    const response = await createProvider(provider.value)
    ElMessage({
      message: response.message,
      type: 'success',
    })
    emit('providerCreated')
    console.log('Provider created:', response)
  } catch (error) {
    ElMessage({
      message: 'Failed to create provider',
      type: 'error',
    })
    console.error('Failed to create provider:', error)
  } finally {
    loading.close()
  }
}
</script>

<style scoped lang="scss">
/* Add your styles here */
.el-form {
  padding: 20px;
}
.h1 {
  text-align: center;
}
</style>