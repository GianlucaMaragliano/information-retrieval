<script>
import Document from "@/components/Document.vue";

export default {
  components: {Document},
  data() {
    return {
      showMore: false,
    };
  },
  computed: {
    results() {
      return this.$store.state.results
    },
    query() {
      return this.$store.state.query
    },
    displayedResults() {
      if (this.showMore) {
        return this.results
      } else {
        return this.results.slice(0, 10)
      }
    },
    counter() {
      if (this.query && this.showMore) {
        return this.$store.state.results.length
      } else if (this.query) {
        return 10
      }
      return 0
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
  methods: {
    showMoreResults() {
      this.showMore = !this.showMore;
    }
  }
}
</script>

<template>

  <h3 v-if="query"> Found {{results.length}} results for "{{query}}".</h3>
  <h3 v-if="counter > 0"> Showing {{counter}} most relevant</h3>
  <ul v-for="item in displayedResults" :key="item.id">
    <Document :document="item"></Document>
  </ul>
  <div id="button">
    <button v-if="results.length > 10" @click="showMoreResults" class="show-more-button">
      {{ showMore ? 'Show Less' : 'Show More' }}
    </button>
  </div>
</template>

<style scoped>
 h3 {
   margin-bottom: 15px;
 }

 #button {
   display: flex;
   flex-direction: column;
   align-items: center;
 }

 .show-more-button {
   background-color: transparent;
   color: hsla(160, 100%, 37%, 1);
   padding: 8px 16px;
   border: none;
   border-radius: 4px;
   cursor: pointer;
   width: 50%;
 }

 .show-more-button:hover {
   background-color: black;
 }
</style>