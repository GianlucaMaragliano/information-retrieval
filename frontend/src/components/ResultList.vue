<script>
import Document from "@/components/Document.vue";

export default {
  components: {Document},
  data() {

  },
  computed: {
    results() {
      return this.$store.state.results
    }
  },
  watch: {
    results: {
      immediate: false,
      deep: false,
      handler(newValue, oldValue) {
        console.log(newValue);
      }
    }
  },
}
</script>

<template>
  <ul v-for="item in results">
    <Document :document="item"></Document>
  </ul>

</template>

<style scoped>

</style>