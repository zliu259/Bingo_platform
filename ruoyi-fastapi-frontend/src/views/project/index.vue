<template>

  <el-row :gutter="20">
    <el-col :span="10"><div class="grid-content ep-bg-purple" />
      <div class="table">
        <Table/>
      </div>
    </el-col>
    <el-col :span="14"><div class="grid-content ep-bg-purple" />
      <div class = "form">
        test
      </div>
    </el-col>
  </el-row>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
import Table from './table.vue'
</script>

<style>
.table {
  margin: 20px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>