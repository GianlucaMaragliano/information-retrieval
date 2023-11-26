<script>
import SearchBar from "@/components/SearchBar.vue";
import ResultList from "@/components/ResultList.vue";

export default {
  components: {ResultList, SearchBar},
  data() {
    return {
      message: "",
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
};
</script>

<template>
  <header>
    <ResultList></ResultList>
  </header>

  <main>
    <div>
      <h1>{{ message }}</h1>
    </div>
    <SearchBar></SearchBar>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
