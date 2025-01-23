<template>
  <div>
    <el-upload
        class="upload-demo"
        action="https://upload.liuzihao1997.workers.dev"
        :show-file-list="true"
        :on-success="handleSuccess"
        :on-error="handleError"
        :before-upload="beforeUpload"
        :headers="headers"
        :data="extraData"
        name="file"
        drag
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">Drag file here or <em>click to upload</em></div>
      <div class="el-upload__text">{{this.taskId}}</div>
    </el-upload>

    <div v-if="uploadedUrl">
      <p>File uploaded successfully: <a :href="uploadedUrl" target="_blank">{{ uploadedUrl }}</a></p>
    </div>
  </div>
</template>

<script>
import { UploadFilled } from "@element-plus/icons-vue";

export default {
  components: { UploadFilled },
  props: {
    taskId: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      uploadedUrl: "",
      headers: {},
      extraData: {
        folderPath: this.taskId, // Specify directory path
        taskId: this.taskId // Include taskId in extraData
      },
    };
  },
  methods: {
    beforeUpload(file) {
      const isLt5M = file.size / 1024 / 1024 < 100;
      if (!isLt5M) {
        this.$message.error("File size cannot exceed 100MB!");
        return false;
      }
      return true;
    },
    handleSuccess(response) {
      if (response.success) {
        this.uploadedUrl = response.url;
        this.$message.success("File uploaded successfully!");
      } else {
        this.$message.error("Upload failed!");
      }
    },
    handleError(err) {
      this.$message.error("Upload failed: " + err.message);
    },
  },
};
</script>