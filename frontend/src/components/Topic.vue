<script>

import Document from "@/components/Document.vue";

export default {
  components: {Document},
  props: {
    results: Array,
    topic: String
  },
  computed: {
    ineherent_res() {
      let res = []
      this.results.forEach(el => {
        if (el.subject === this.topic)
          res.push(el)
      })
      return res
    },
    watch: {
      ineherent_res: {
        immediate: false,
        deep: false,
        handler(newValue, oldValue) {
          console.log(newValue);
        }
      }
    }
  }
}

</script>

<template>

  <h2> {{this.topic}}: {{ineherent_res.length}} result </h2>
  <ul v-for="exp in ineherent_res">
    <Document :document="exp"></Document>
  </ul>

</template>

<style scoped>

</style>