<script>
import SearchBar from "@/components/SearchBar.vue";
import ResultList from "@/components/ResultList.vue";
import cloud2 from "@/assets/circle.png";
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
};
</script>

<template>
    <div id="results">
      <ResultList></ResultList>
    </div>
    <div id="search-bar"  :style="{ 'background-image': 'url(' + img + ')', 'background-repeat': 'no-repeat', 'background-position': 'center'}">
        <img src="./assets/science.webp" alt="Your Image Alt Text" />
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
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 50%;
  right: -25%;
  transform: translateY(-50%);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

img {
  width: 30%;
}



@media (min-width: 1024px) {

}
</style>
