<template>
  <div>
    <el-form
        v-if="!submissionSuccess"
        :model="form"
        label-width="auto"
        style="max-width: 600px"
        v-loading="loading"
        label-position="top"
    >
      <el-form-item label="Client ID">
        <el-input v-model="form.client_id" readonly />
      </el-form-item>
      <el-form-item label="Client name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="ABN">
        <el-input v-model="form.abn" />
      </el-form-item>
      <el-form-item label="Contact Person">
        <el-input v-model="form.contact" />
      </el-form-item>

      <el-form-item label="Contact Method">
        <el-select
            v-model="form.method"
            placeholder="please select the method"
            multiple
        >
          <el-option label="Email" value="Email" />
          <el-option label="Wechat" value="Wechat" />
          <el-option label="Phone" value="Phone" />
          <el-option label="Post" value="Post" />
          <el-option label="Others" value="Others" />
        </el-select>
      </el-form-item>

      <el-form-item label="Contact Details">
        <el-input v-model="form.details" />
      </el-form-item>

      <el-form-item label="Note">
        <el-input v-model="form.note" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Create</el-button>
      </el-form-item>
    </el-form>
    <el-result v-else icon="success" title="Success" sub-title="Client created successfully" />
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { createClient } from '@/api/business/business'
import { v7 as uuidv7 } from 'uuid'

const form = reactive({
  name: '',
  abn: '',
  contact: '',
  method: '',
  details: '',
  note: '',
  client_id: uuidv7(),
  created_by: 'admin',
  created_time: new Date().toISOString(),
})

const submissionSuccess = ref(false)
const loading = ref(false)

const onSubmit = async () => {
  console.log('submit!')
  const data = form
  form.method = form.method.toString()
  console.log(data)
  loading.value = true
  try {
    const response = await createClient(data)
    console.log('Submission successful', response)
    if (response.code === 200)
      submissionSuccess.value = true
  } catch (error) {
    console.error('Submission failed', error)
  } finally {
    loading.value = false
  }
}
</script>