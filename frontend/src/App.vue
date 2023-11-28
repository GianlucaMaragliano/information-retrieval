<script>
import SearchBar from "@/components/SearchBar.vue";
import ResultList from "@/components/ResultList.vue";
export default {
  components: {ResultList, SearchBar},
  data() {
    return {
      message: "",
      // img: cloud2
    };
  },
  mounted() {
    try {
      fetch("http://localhost:5000")
          .then((response) => response.text())
          .then((data) => {
            this.message = data;
          });
    } catch (e) {
      console.log(e)
    }
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
      this.$store.dispatch("resetQuery")
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
  </div>
    <div id="search-bar">
        <img src="./assets/logo.png" alt="Your Image Alt Text" @click="resetQuery()"/>
        <SearchBar></SearchBar>
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



@media (min-width: 1024px) {

}
</style>
