<script>
import Document from "@/components/Document.vue";

export default {
  components: {Document},
  data() {

  },
  computed: {
    results() {
      return this.$store.state.results
    },
    query() {
      return this.$store.state.query
    }
  },
  watch: {
    results: {
      immediate: false,
      deep: false,
      handler(newValue, oldValue) {
        console.log(newValue);
      }
    },
    query: {
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

  <h3 v-if="query"> Found {{results.length}} results for "{{query}}"</h3>
  <ul v-for="item in results">
    <Document :document="item"></Document>
  </ul>

</template>

<style scoped>

</style>