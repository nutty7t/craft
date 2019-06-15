<template>
  <div id="upload">
    <form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <input
        type="file"
        ref="file"
        accept="application/gzip"
        @change="onSelect"/>
      <button v-if="!isUploading && !uploadSuccess">Upload</button>
      <span v-else>{{ uploadProgress }}%</span>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      file: '',
      isUploading: false,
      uploadProgress: 0,
      uploadSuccess: false
    }
  },
  methods: {
    onSelect () {
      const file = this.$refs.file.files[0]
      this.file = file
    },
    async onSubmit () {
      this.isUploading = true
      const formData = new FormData()
      formData.append('file', this.file)
      try {
        const config = {
          headers: { 'Content-Type': 'multipart/form-data' },
          onUploadProgress: (function (event) {
            const uploaded = event.loaded * 100
            const totalSize = event.total
            this.uploadProgress = parseInt(Math.round(uploaded / totalSize))
          }).bind(this)
        }
        await axios.post("/upload", formData, config)
        this.uploadSuccess = true
        alert("Success!")
      } catch (error) {
        console.log(error.response)
        alert(error.response.data)
      }
      this.isUploading = false
    }
  }
}
</script>

<style scoped lang="scss">
#upload {
    width: 50%;
    margin: auto;
}
</style>
