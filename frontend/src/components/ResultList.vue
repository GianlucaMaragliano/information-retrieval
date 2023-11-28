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
      Map.prototype.inc = function(s) {
        if (this.has(s)) {
          this.set(s, this.get(s) + 1);
        } else {
          this.set(s, 1);
        }
      }
      let subjects = []
      let subj_map = new Map()
      this.$store.state.results.forEach(el => {
            subjects.push(el.subject)
            subj_map.inc(el.subject)
          }
      )
      // let test = Array.from(subj_map.keys())
      // return [...new Set(test.filter(n => n))]
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
    },
    scrollToTop() {
      console.log("Clicked")
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
}
</script>

<template>

  <h3 id="tmp" v-if="query"> Found {{results.length}} results for "{{query}}" with {{subjects.length}} different subjects</h3>
  <button id="button2" class="show-more-button" v-if="counter > 0 && query" @click="changeMode()">
    {{clustering ? 'Show per Experiment' : 'Show per Subject'}}
  </button>

  <h3 v-if="counter > 0 && !this.clustering"> Showing {{counter}} most relevant</h3>

  <div v-if="!this.clustering">
    <div id="scroll-to-top" @click="scrollToTop">
      <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          class="arrow-icon"
      >
        <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 10l7-7m0 0l7 7m-7-7v18"
        />
      </svg>
    </div>
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

 #button2 {
   display: flex;
   flex-direction: column;
   align-items: center;
    justify-content: center;
   margin-left: 200px;
   margin-bottom: 15px;
 }

 .show-more-button {
   background-color: transparent;
   color: hsl(196, 76%, 39%);
   padding: 8px 16px;
   border: none;
   border-radius: 4px;
   cursor: pointer;
   width: 50%;
 }

 .show-more-button:hover {
   background-color: black;
 }

 #scroll-to-top {
   position: fixed;
   bottom: 20px;
   left: 50px;
   cursor: pointer;
 }

 .arrow-icon {
   width: 24px;
   height: 24px;
   fill: none;
   stroke: hsl(208, 100%, 43%);
 }
</style>