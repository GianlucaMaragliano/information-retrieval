<script>

import Document from "@/components/Document.vue";

export default {
  components: {Document},
  data () {
    return {
      clicked: true,
      isArrowRotated: false,
    }
  },
  props: {
    results: Array,
    topic: String
  },
  methods: {
    show() {
      this.clicked = !this.clicked;
      this.isArrowRotated = !this.isArrowRotated;
    }
  },
  computed: {
    inherent_res() {
      let res = []
      this.results.forEach(el => {
        if (el.subject === this.topic)
          res.push(el)
      })
      return res
    },
    watch: {
      inherent_res: {
        immediate: false,
        deep: false,
        handler(newValue, oldValue) {
          console.log(newValue);
        }
      }
    }
  }
}

</script>

<template>

  <div class="header">
  <img id="logo" src="../assets/atom.svg" alt="Your Image Alt Text"/>
  <h2> {{this.topic}}: {{inherent_res.length}} result </h2>
  <div @click="show">
      <img src="../assets/triangle.svg" alt="Your Image Alt Text" class="arrow-icon"/>
  </div>
  </div>
  <div v-if="clicked">

  </div>

  <ul v-else v-for="exp in inherent_res">
      <Document :document="exp"></Document>
  </ul>

</template>

<style scoped>
  .arrow-icon {
    width: 15px;
    margin-inline: 15px;
    cursor: pointer;
  }

  .header{
    display: flex;
    flex-direction: row;
    margin-block: 10px;
    align-items: center;
  }

  #logo {
    width: 25px;
    margin-inline: 10px;
  }
</style>