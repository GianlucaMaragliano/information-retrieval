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
  <a v-bind:href=document.Link target="_blank" rel="noreferrer">
    {{document.Title}}
  </a>
  <p>{{this.str_limit(document.Description, 90)}}</p>
</template>

<style scoped>

</style>