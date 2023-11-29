<script>
import SearchBar from "@/components/SearchBar.vue";
import ResultList from "@/components/ResultList.vue";
import {ref} from "vue";

export default {
  components: {ResultList, SearchBar},
  data() {
    return {
      sample_queries : ["Rocket", "Javascript Game", "Explosive Car", "Mushrooms Bridge", "Acid Water",
    "Volcano Eruption", "Homemade Yogurt", "Phone Radiations", "Colored Fire"],
      three_suggestion: []
    };
  },
  setup() {
    const searchBarRef = ref(null)

    return {
      searchBarRef
    }
  },
  mounted() {
    this.generateSuggestion()
    console.log(this.searchBarRef)
  },
  computed: {
    query() {
      return this.$store.state.query
    },
  },
  watch: {
    query: {
      immediate: false,
      deep: false,
    }
  },
  methods: {
    resetQuery() {
      if (this.query) {
        this.searchBarRef.resetQuery()
        this.$store.dispatch("resetQuery")
        this.generateSuggestion()
      }
    },
    generateSuggestion() {
      const shuffled = this.sample_queries.sort(() => 0.5 - Math.random());
      this.three_suggestion = shuffled.slice(0, 3)
    },
    async fetchSuggested(event) {
      let sugg_query = event.target.innerHTML
      await this.$store.dispatch("fetchQuery", sugg_query)
      this.searchBarRef.setQuery(sugg_query)
    }
  }
};
</script>

<template>
    <div id="results" v-if="query">
      <ResultList></ResultList>
    </div>

    <div id="welcome" v-else>
      <h1> Welcome to Science Hub!</h1>
      <h2> Here you can find science experiments for middle and high schools and much more! </h2>
      <h3> Start your search by typing your interest or have a look at the suggested topics. </h3>
      <div v-for="query in this.three_suggestion" class="query-suggestion" @click="fetchSuggested($event)">
        {{query}}
      </div>
    </div>

    <div id="search-bar">
        <img src="./assets/logo.png" alt="Your Image Alt Text" @click="resetQuery()"/>
        <SearchBar ref="searchBarRef"></SearchBar>
    </div>
</template>

<style scoped>

#results {
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 20px 100px 20px 100px;
}

#search-bar {
  width: 60%;
  height: 100vh;
  position: fixed;
  top: 50%;
  right: -5%;
  transform: translateY(-50%);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

img {
  width: 50%;
  cursor: pointer;
}

.query-suggestion {
  background-color: transparent;
  color: hsl(196, 76%, 39%);
  padding: 8px 16px;
  margin-block: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 50%;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.query-suggestion:hover {
  background-color: black;
}

#welcome {
  width: 60%;
  height: 100vh;
  position: fixed;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

h1 {
  font-size: 70px;
  margin-block: 10px;
}

h2 {
  font-size: 20px;
  margin-block: 10px;
}
h3 {
  margin-block: 10px;
}
@media (min-width: 1024px) {

}
</style>
