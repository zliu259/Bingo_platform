<template>
  <div>
    <el-form @submit.prevent="submitForm" :model="newTask" label-position="top">
      <p>{{newTask.id}}</p>
      <el-form-item label="Project ID">
        <el-select v-model="newTask.project_id" placeholder="Select Project">
          <el-option
            v-for="project in projects"
            :key="project.id"
            :label="project.name"
            :value="project.id"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="User">
        <el-select v-model="newTask.user" placeholder="请选择用户">
          <el-option
            v-for="user in users"
            :key="user.userId"
            :label="user.userName"
            :value="user.userId"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="Created By">
        <el-input v-model="newTask.created_by" required></el-input>
      </el-form-item>
      <el-form-item label="Instruction">
        <el-input type="textarea" v-model="newTask.instruction" required></el-input>
      </el-form-item>
      <el-form-item label="Type">
        <el-select v-model="newTask.type" placeholder="Select Type">
          <el-option label="Translating" :value="0"></el-option>
          <el-option label="Interpreting" :value="1"></el-option>
          <el-option label="Quoting/Estimating" :value="2"></el-option>
          <el-option label="Data Processing" :value="3"></el-option>
          <el-option label="Document Generating" :value="4"></el-option>
          <el-option label="Reviewing" :value="5"></el-option>
          <el-option label="Others" :value="6"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Due">
        <el-date-picker v-model="dueDate" type="datetime" placeholder="Select Date and Time" required></el-date-picker>
        <p v-if="timeDifference">Due in {{ timeDifference }}</p>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">Create Task</el-button>
      </el-form-item>
    </el-form>
    <Uploader :taskId="newTask.id" />
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { ElForm, ElFormItem, ElInput, ElSelect, ElOption, ElButton, ElLoading, ElMessage, ElDatePicker } from 'element-plus';
import { v7 as uuidv7 } from 'uuid';
import { getTaskList, createTask, getQuotationList, getMemberList } from '@/api/business/business';
import Uploader from './upload.vue';

const tasks = ref([]);
const projects = ref([]);
const users = ref([]);
const dataLoaded = ref(false);
const newTask = ref({
  id: uuidv7(),
  project_id: '',
  user: '',
  created_by: '',
  instruction: '',
  status: 0, // Default value
  active: 1, // Default value
  type: null,
  due: null
});
const dueDate = ref(new Date());

watch(dueDate, (newVal) => {
  if (newVal) {
    newTask.value.due = new Date(newVal).getTime();
  }
});

const timeDifference = computed(() => {
  if (!dueDate.value) return null;
  const now = new Date();
  const diff = new Date(dueDate.value).getTime() - now.getTime();
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  return `${days} days, ${hours} hours, and ${minutes} minutes`;
});

onMounted(async () => {
  try {
    const userResponse = await getMemberList();
    // 确保数据格式正确
    if (userResponse.data && Array.isArray(userResponse.data)) {
      users.value = userResponse.data;
    } else {
      console.error('Invalid user data format:', userResponse);
      ElMessage.error('获取用户列表失败');
    }
    // ...其他数据加载
  } catch (error) {
    console.error('Failed to load users:', error);
    ElMessage.error('获取用户列表失败');
  }
  const taskResponse = await getTaskList();
  tasks.value = taskResponse.data;
  const projectResponse = await getQuotationList();
  projects.value = projectResponse.data;
  dataLoaded.value = true;
});

const submitForm = async () => {
  const loading = ElLoading.service({
    lock: true,
    text: 'Submitting...',
    background: 'rgba(0, 0, 0, 0.7)'
  });

  try {
    await createTask(newTask.value);
    const response = await getTaskList();
    tasks.value = response.data;
    newTask.value = {
      id: uuidv7(),
      project_id: '',
      user: '',
      created_by: '',
      instruction: '',
      status: 0, // Default value
      active: 1, // Default value
      type: null,
      due: null
    };
    dueDate.value = new Date();
    ElMessage.success('Task created successfully!');
  } catch (error) {
    ElMessage.error('Failed to create task.');
  } finally {
    loading.close();
  }
};
</script>

<style scoped lang="scss">
/* Add your styles here */
</style>