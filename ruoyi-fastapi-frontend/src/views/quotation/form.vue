<template>
  <el-form :model="quotation" label-width="120px">
    <el-form-item label="ID">
      <el-input v-model="quotation.id" readonly></el-input>
    </el-form-item>
    <el-form-item label="Select Client">
      <el-select v-model="selectedClient" placeholder="Select client" @change="updateClientDetails">
        <el-option v-for="client in clients" :key="client.id" :label="client.contact+'-'+client.name" :value="client"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Client Name">
      <el-input v-model="quotation.client_name" readonly></el-input>
    </el-form-item>
    <el-form-item label="Client Contact">
      <el-input v-model="quotation.client_contact" readonly></el-input>
    </el-form-item>
    <el-form-item label="Client Details">
      <el-input v-model="quotation.client_details" readonly></el-input>
    </el-form-item>
    <el-form-item label="Client ID">
      <el-input v-model="quotation.client_id" readonly></el-input>
    </el-form-item>
    <el-form-item label="Select Provider">
      <el-select v-model="selectedProvider" placeholder="Select provider" @change="updateProviderDetails">
        <el-option v-for="provider in providers" :key="provider.id" :label="provider.name" :value="provider"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Provider ID">
      <el-input v-model="quotation.provider_id" readonly></el-input>
    </el-form-item>
    <el-form-item label="Date">
      <el-input v-model="quotation.date" readonly></el-input>
    </el-form-item>
    <el-form-item label="Type">
      <el-select v-model="quotation.type" placeholder="Select type">
        <el-option label="Translation C->E" value="Translation C->E"></el-option>
        <el-option label="Translation E->C" value="Translation E->C"></el-option>
        <el-option label="Interpreting" value="Interpreting"></el-option>
        <el-option label="Other" value="Other"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Work Load">
      <el-input-number v-model="quotation.load">
      </el-input-number>
      <el-alert type="info" show-icon :closable="false">
      <p>"Work Load - Estimated working hours 预计所需要的人工时</p>
    </el-alert>
    </el-form-item>
    <el-form-item label="Statistics">
      <el-table :data="quotation.statistics">
        <el-table-column prop="item" label="Item">
          <template #default="scope">
            <el-input v-model="scope.row.item"></el-input>
          </template>
        </el-table-column>
        <el-table-column prop="categories" label="Categories" width="600px">
          <template #default="scope">
            <el-select v-model="scope.row.categories" placeholder="Select category" @change="updateUnitPrice(scope.row)">
              <el-option label="Translation C->E （per 1k Chinese Characters)" value="Translation C->E （per 1k Chinese Characters)"></el-option>
              <el-option label="Translation E->C （per 1k English Words)" value="Translation E->C （per 1k English Words)"></el-option>
              <el-option label="Audio Transcription and Translation E<->C (per second)" value="Audio Transcription and Translation E<->C (per second)"></el-option>
              <el-option label="Video Transcription and Translation E<->C (per second)" value="Video Transcription and Translation E<->C (per second)"></el-option>
              <el-option label="Image Process (per image)" value="Image Process (per image)"></el-option>
              <el-option label="Interpreting (per h)" value="Interpreting (per h)"></el-option>
              <el-option label="Others" value="Others"></el-option>
            </el-select>
          </template>
        </el-table-column>
        <el-table-column prop="unitprice" label="Unit Price (AUD)">
          <template #default="scope">
            <el-input v-model="scope.row.unitprice" type="number"></el-input>
          </template>
        </el-table-column>
        <el-table-column prop="quantities" label="Quantities">
          <template #default="scope">
            <el-input v-model="scope.row.quantities" type="number" @input="updateRowPrice(scope.row)"></el-input>
          </template>
        </el-table-column>
        <el-table-column prop="price" label="Price (AUD)">
          <template #default="scope">
            <el-input v-model="scope.row.price" type="number" readonly></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Operations">
          <template #default="scope">
            <el-button @click="removeRow(scope.$index)">Remove</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button @click="addRow">Add Row</el-button>
    </el-form-item>
    <el-form-item label="Price">
      <el-input v-model="quotation.price" readonly></el-input>
    </el-form-item>
    <el-form-item label="GST">
      <el-switch v-model="quotation.gst" active-value="yes" inactive-value="no" @change="calculateTotalPrice"></el-switch>
    </el-form-item>
    <el-form-item label="Total Price">
      <el-input v-model="quotation.total_price" readonly></el-input>
    </el-form-item>
    <el-form-item label="Created By">
      <el-input v-model="quotation.created_by"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { v7 as uuidv7 } from 'uuid'
import { createQuotation, getClientList, getProviderList } from '@/api/business/business.js'
import { ElMessage, ElLoading } from 'element-plus'

const quotation = ref({
  id: uuidv7(),
  client_name: '',
  client_contact: '',
  client_details: '',
  client_id: '',
  provider_id: '',
  date: new Date().toISOString().slice(0, 10),
  type: '',
  status: 0,
  load: 0,
  statistics: [],
  price: '',
  gst: 'no',
  total_price: '',
  created_by: ''
})

const clients = ref([])
const providers = ref([])
const selectedClient = ref(null)
const selectedProvider = ref(null)

const fetchClients = async () => {
  try {
    const response = await getClientList()
    clients.value = response
  } catch (error) {
    console.error('Failed to fetch clients:', error)
  }
}

const fetchProviders = async () => {
  try {
    const response = await getProviderList()
    providers.value = response
  } catch (error) {
    console.error('Failed to fetch providers:', error)
  }
}

const updateClientDetails = (client) => {
  quotation.value.client_name = client.name
  quotation.value.client_contact = client.contact
  quotation.value.client_details = client.details
  quotation.value.client_id = client.client_id
}

const updateProviderDetails = (provider) => {
  quotation.value.provider_id = provider.id
}

const addRow = () => {
  quotation.value.statistics.push({
    item: '',
    categories: '',
    unitprice: 0,
    quantities: 0,
    price: 0
  })
}

const removeRow = (index) => {
  quotation.value.statistics.splice(index, 1)
  calculateTotalPrice()
}

const calculateTotalPrice = () => {
  const price = quotation.value.statistics.reduce((sum, row) => sum + parseFloat(row.price || 0), 0)
  quotation.value.price = price.toFixed(2)
  const gst = quotation.value.gst === 'yes' ? 0.1 : 0
  quotation.value.total_price = (price * (1 + gst)).toFixed(2)
}

const getUnitPrice = (category) => {
  switch (category) {
    case 'Translation C->E （per 1k Chinese Characters)':
      return 300
    case 'Translation E->C （per 1k English Words)':
      return 300
    case 'Audio Transcription and Translation E<->C (per second)':
      return 1.75
    case 'Video Transcription and Translation E<->C (per second)':
      return 1.85
    case 'Image Process (per image)':
      return 2.5
    case 'Interpreting (per h)':
      return 160
    default:
      return 0
  }
}

const updateUnitPrice = (row) => {
  row.unitprice = getUnitPrice(row.categories)
  updateRowPrice(row)
}

const updateRowPrice = (row) => {
  row.price = (row.unitprice * row.quantities).toFixed(2)
  calculateTotalPrice()
}

const submitForm = async () => {
  const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  try {
    const response = await createQuotation(quotation.value)
    ElMessage({
      message: response.message,
      type: 'success',
    })
    console.log('Quotation created:', response)
  } catch (error) {
    ElMessage({
      message: 'Failed to create quotation',
      type: 'error',
    })
    console.error('Failed to create quotation:', error)
  } finally {
    loading.close()
  }
}

onMounted(() => {
  fetchClients()
  fetchProviders()
})
</script>

<style scoped lang="scss">
/* Add your styles here */
</style>