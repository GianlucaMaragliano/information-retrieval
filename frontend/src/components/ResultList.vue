<script>
export default {
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
    <a v-bind:href=item.Link>
      {{item.Title}}
    </a>
  </ul>

</template>

<style scoped>

</style>