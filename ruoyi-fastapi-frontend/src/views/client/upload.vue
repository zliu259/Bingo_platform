<template>
  <div>
    <el-upload
        class="upload-demo"
        action="https://upload.bingocommunications.com.au/"
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
  data() {
    return {
      uploadedUrl: "",
      headers: {
        // 这里可以添加 Authorization 头，比如 JWT token（如果需要身份验证）
        // Authorization: "Bearer YOUR_TOKEN"
      },
      extraData: {
        // 如果需要附加参数，可以放这里
      },
    };
  },
  methods: {
    beforeUpload(file) {
      const isLt5M = file.size / 1024 / 1024 < 5;
      if (!isLt5M) {
        this.$message.error("File size cannot exceed 5MB!");
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

<style>
.upload-demo {
  text-align: center;
}
</style>