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
  <a v-bind:href=document.link target="_blank" rel="noreferrer">
    {{document.title}}
  </a>
  <p v-if="document.tescription"> {{this.str_limit(document.Description, 90)}}</p>
  <p v-else> {{this.str_limit(document.explanation, 90)}}</p>
</template>

<style scoped>

</style>