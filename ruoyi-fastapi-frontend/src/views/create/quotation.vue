<template>
  <el-form :model="form" label-position="left">
    <el-form-item label="Quotation ID">
      <el-input style="margin-bottom: 20px" v-model="form.quotationId" placeholder="Quotation ID" readonly></el-input>
    </el-form-item>
    <el-table :data="form.items" style="width: 100%">
      <el-table-column label="Item" align="center" width="400">
        <template #default="scope">
          <el-select v-model="scope.row.itemName" placeholder="Select or add item" allow-create filterable>
            <el-option v-for="item in items" :key="item.name" :label="item.name" :value="item.name"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column prop="unitPrice" label="Unit price (AUD)" align="center">
        <template #default="scope">
          <el-input v-model="scope.row.unitPrice" prefix-icon="el-icon-money"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="quantity" label="Quantity" align="center">
        <template #default="scope">
          <el-input-number v-model="scope.row.quantity" :min="1"></el-input-number>
        </template>
      </el-table-column>
      <el-table-column label="Total (AUD)" align="center">
        <template #default="scope">
          {{ (scope.row.unitPrice * scope.row.quantity).toFixed(2) }}
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="100">
        <template #default="scope">
          <el-button type="danger" link @click="removeItem(scope.$index)">Remove</el-button>
        </template>
        <template #header>
          <el-button type="primary" size="small" plain @click="addItem">Add item</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-row>
      <el-col :span="12">
        <div style="text-align: left; margin-top: 10px;">
          <el-form-item label="Instruction">
            <el-input v-model="form.instruction" type="textarea" />
          </el-form-item>
          <el-form-item label="Note">
            <el-input v-model="form.note" type="textarea" />
          </el-form-item>
        </div>
      </el-col>
      <el-col :span="12">
        <div style="text-align: right; margin-top: 10px;">
          <p>Sub-total: {{ subTotal.toFixed(2) }}</p>
          <p>Discount: -{{ discountAmount.toFixed(2) }}</p>
          <p>Discounted Total: {{ discountedTotal.toFixed(2) }}</p>
          <p>GST Amount: {{ gstAmount.toFixed(2) }}</p>
          <p><strong>Total Amount (AUD): {{ finalQuotation.toFixed(2) }}</strong></p>
        </div>
      </el-col>
    </el-row>

    <el-form-item label="Discount Rate (%)"  style=" width: 300px;">
      <el-input-number v-model="form.discountRate" :min="0" :max="100" />
    </el-form-item>
    <el-form-item label="Include GST (10%)" style="width: 300px;">
      <el-switch v-model="form.includeGST" />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, computed, watch } from 'vue'
import { v7 as uuidv7 } from 'uuid'

const form = reactive({
  quotationId: uuidv7(),
  clientName: '',
  items: [
    { itemName: '', unitPrice: 0, quantity: 1 }
  ],
  discountRate: 0,
  includeGST: false,
  note: '',
  instruction: ''
})

const items = reactive([
  { name: 'Translation Chinese to English (per 1k characters)', unitPrice: 350.00 },
  { name: 'Translation English to Chinese (per 1k word)', unitPrice: 200.00 },
  { name: 'Audio transcription (per second)', unitPrice: 1.50 },
  { name: 'Video transcription (per second)', unitPrice: 2.00 },
  { name: 'Data processing (per 1MB)', unitPrice: 0.10 },
  { name: 'Image processing (per item)', unitPrice: 5.00 },
  { name: 'Document (fixed price per item)', unitPrice: 50.00 },
  { name: 'Others', unitPrice: 0.00 }
])

const addItem = () => {
  form.items.push({ itemName: '', unitPrice: 0, quantity: 1 })
}

const removeItem = (index: number) => {
  form.items.splice(index, 1)
}

const subTotal = computed(() => {
  return form.items.reduce((sum, item) => sum + item.unitPrice * item.quantity, 0)
})

const discountAmount = computed(() => {
  return subTotal.value * (form.discountRate / 100)
})

const discountedTotal = computed(() => {
  return subTotal.value - discountAmount.value
})

const gstAmount = computed(() => {
  return form.includeGST ? discountedTotal.value * 0.1 : 0
})

const finalQuotation = computed(() => {
  return discountedTotal.value + gstAmount.value
})

const onSubmit = () => {
  console.log('Form data:', form)
}

// Watch for changes in itemName and update unitPrice accordingly
watch(
    () => form.items.map(item => item.itemName),
    (newValues, oldValues) => {
      newValues.forEach((newValue, index) => {
        const selectedItem = items.find(item => item.name === newValue)
        if (selectedItem) {
          form.items[index].unitPrice = selectedItem.unitPrice
        }
      })
    }
)
</script>