<template>
  <div>
    <el-select
        v-if="!loading && !error"
        v-model="selectedClient"
        placeholder="Select a client. Create a new client if not listed."
    >
      <el-option
          v-for="(client, index) in clients"
          :key="index"
          :label="client.contact + ' from ' + client.name"
          :value="client.client_id"
      />
    </el-select>

    <div v-else-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-if="selectedClient">
      <p>Selected Client ID: <br><br><strong>{{ selectedClient }}</strong></p><br>
      <p>Client: {{ selectedClientDetails.name }}</p>
      <p>ABN: {{ selectedClientDetails.abn }}</p>
      <p>Contact: {{ selectedClientDetails.contact }}</p>
      <p>Method: {{ selectedClientDetails.method }}</p>
      <p>Details: {{ selectedClientDetails.details }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { getClientList } from '@/api/business/business';

interface Client {
  name: string;
  abn: string;
  contact: string;
  method: string;
  details: string;
}

const clients = ref<Client[]>([]);
const selectedClient = ref<string | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await getClientList();
    console.log('Full API Response:', response);

    // Handle varying response structures
    if (Array.isArray(response)) {
      clients.value = response; // Clients are directly in response
    } else if (response && Array.isArray(response.data)) {
      clients.value = response.data; // Clients are in response.data
    } else if (response && response.result && Array.isArray(response.result.clients)) {
      clients.value = response.result.clients; // Nested structure
    } else {
      throw new Error('Invalid response format');
    }
  } catch (err) {
    console.error('Error fetching client list:', err);
    error.value = 'Failed to fetch client list. Please try again later.';
  } finally {
    loading.value = false;
  }
});
const selectedClientDetails = ref<Client | null>(null);

watch(selectedClient, (newVal) => {
  selectedClientDetails.value = clients.value.find(client => client.client_id === newVal) || null;
});
</script>

<style scoped lang="scss">
/* Add your styles here */
</style>