<script>
import Document from "@/components/Document.vue";
import Topic from "@/components/Topic.vue";

export default {
  components: {Topic, Document},
  data() {
    return {
      showMore: false,
      clustering: false
    };
  },
  computed: {
    results() {
      return this.$store.state.results
    },
    query() {
      return this.$store.state.query
    },
    subjects() {
      let subjects = []
      this.$store.state.results.forEach(el => subjects.push(el.subject))
      return [...new Set(subjects.filter(n => n))];
    },
    displayedResults() {
      if (this.showMore) {
        return this.results
      } else {
        return this.results.slice(0, 10)
      }
    },
    counter() {
      if (this.query && (this.showMore || this.$store.state.results.length <= 10)) {
        return 0
      } else if (this.$store.state.results.length !== 0) {
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
    subjects: {
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
    },
    changeMode() {
      this.clustering = !this.clustering;
    }
  }
}
</script>

<template>

  <h3 v-if="query"> Found {{results.length}} results for "{{query}}" with {{subjects.length}} different subjects</h3>
  <h3 v-if="counter > 0 && !this.clustering"> Showing {{counter}} most relevant</h3>
  <button v-if="counter > 0 && query" @click="changeMode()"> Show results per subject </button>

  <div v-if="!this.clustering">
    <ul v-for="item in displayedResults" :key="item.id">
      <Document :document="item"></Document>
    </ul>
    <div id="button">
      <button v-if="results.length > 10" @click="showMoreResults" class="show-more-button">
        {{ showMore ? 'Show Less' : 'Show All' }}
      </button>
    </div>
  </div>

  <div v-else>
    <ul v-for="topic in subjects">
      <Topic :results="results" :topic="topic"></Topic>
    </ul>
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
    justify-content: center;
   margin-left: -200px;
 }

 .show-more-button {
   background-color: transparent;
   color: hsl(208, 100%, 43%);
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