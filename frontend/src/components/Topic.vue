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
    ineherent_res() {
      let res = []
      this.results.forEach(el => {
        if (el.subject === this.topic)
          res.push(el)
      })
      return res
    },
    watch: {
      ineherent_res: {
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

  <h2> {{this.topic}}: {{ineherent_res.length}} result </h2>
  <div @click="show">
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
  <div v-if="clicked">

  </div>

  <ul v-else v-for="exp in ineherent_res">
      <Document :document="exp"></Document>
  </ul>

</template>

<style scoped>
  .arrow-icon {
    width: 24px;
    height: 24px;
    fill: none;
    stroke: hsl(208, 100%, 43%);
    transition: transform 0.3s;
    transform: rotate(180deg); /* Rotate the arrow when the class is present */
  }
</style>