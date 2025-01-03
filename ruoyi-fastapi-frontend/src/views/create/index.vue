<template>
  <div>
    <el-divider><h1>Basic Information</h1></el-divider>
  </div>
  <div id="main">
    <el-card style="width: 480px; height: 1000px; margin: 20px">
      <template #header>
        <div class="card-header">
          <span>Setp 1 - Select Client</span>
        </div>
      </template>
        <div class="client">
          <ClientForm />
        </div>
    </el-card>
    <el-card style="width: 560px; height: 1000px; margin: 20px">
      <template #header>
        <div class="card-header">
          <span>Setp 2 - Upload Files</span>
        </div>
      </template>
      <div class="client">
        <FileUpload />
      </div>
    </el-card>
    <el-card style="width: 1200px; height: 1000px; margin: 20px">
      <template #header>
        <div class="card-header">
          <span>Setp 3 - Quotation</span>
        </div>
      </template>
      <div class="client">
        <Quotation />
      </div>
    </el-card>
  </div>

</template>

<script lang="ts" setup>
import { ref } from 'vue'
import ClientForm from './client_form.vue'
import FileUpload from './upload.vue'
import Quotation from './quotation.vue'
</script>

<style scoped lang="scss">
.client {
  padding: 20px;
}
#main
{
  display: flex;
  justify-content: center;
}

</style>
