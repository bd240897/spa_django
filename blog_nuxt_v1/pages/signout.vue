<template>
  <div></div>
</template>

<script>
export default {
  name: "signout",
  layout: "post_detail",
  async created() {
    await this.$auth.logout()
    this.$auth.user
    this.$router.push('/')
  },
}
</script>
