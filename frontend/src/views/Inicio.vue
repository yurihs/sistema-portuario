<template>
    <div></div>
</template>

<script>
export default {
  name: 'Inicio',
  data () {
    return {
    }
  },
  mounted () {
    this.$emit('message', 'Início');

    if(!localStorage.getItem('auth_token')){
        this.$router.push('/Login');
    }
  }
}
</script>

<style scoped>

</style>