<template>
  <div>
    <Navbar />
    <Nuxt />
    <Footer />
  </div>
</template>


<script>
import Navbar from "~/components/Navbar";
import Footer from "~/components/Footer";

export default {
  name: 'post_detail',
  components: {
    Footer,
    Navbar,
  },
  head() {
    return {
      link: [
        { rel: "canonical", href: `http://localhost:3000${this.$route.path}`}
      ]
    }
  },
};
</script>

<style>

</style>
