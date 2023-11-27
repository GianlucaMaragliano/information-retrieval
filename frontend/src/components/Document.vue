<script>

export default {
  props: {
    document
  },
  methods: {
    str_limit(value, size) {
      if (!value) return '';
      value = value.toString();

      if (value.length <= size) {
        return value;
      }
      return value.substr(0, size) + '...';
    }
  }
}

</script>

<template>
  <div class="result-box">
    <a v-bind:href="document.link" target="_blank" rel="noreferrer" class="result-title">
      {{ document.title }}
    </a>
    <p v-if="document.tescription" class="result-text">
      {{ this.str_limit(document.Description, 90) }}
    </p>
    <p v-else class="result-text">
      {{ this.str_limit(document.explanation, 90) }}
    </p>
  </div>
</template>

<style scoped>
.result-box {
  width: 80%; /* Adjust as needed */
  border: 3px solid; /* Border color */
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 20px; /* Adjust as needed */
}

.result-title {
  display: block;
  font-size: 23px;
  font-weight: bold;
  color: hsla(160, 100%, 37%, 1);
  text-decoration: none;
  //margin-bottom: 10px; /* Adjust as needed */
}

.result-text {
  font-size: 14px;
  color: lightgray; /* Text color */
  margin: 0;
}
</style>