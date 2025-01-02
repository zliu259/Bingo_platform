<template>

  <el-row :gutter="20">
    <el-col :span="16"><div class="grid-content ep-bg-purple" />
      <div class="table">
        <Table/>
      </div>
    </el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple" />
      <div class = "form">
        <h1>Create New Client</h1>
        <Form/>
      </div>
    </el-col>
  </el-row>

</template>
<script lang="ts" setup>
import { ref } from 'vue'
import Table from './table.vue'
import Form from './form.vue'
</script>
<style>
.table {
  margin: 20px;
}
.button{
  margin: 20px;
}
</style>