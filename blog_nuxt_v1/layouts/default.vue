<!--аналог base html-->

<template>
  <div>
    <Navbar />
    <Slider />
    <div class="container">
      <!-- Это собственно встроенный компонент, который отвечает за вывод контента находящегося внутри страницы в директории page. -->

      <Nuxt />
    </div>
    <Footer />
  </div>
</template>


<script>

// импортируем
import Navbar from "~/components/Navbar";
import Slider from "~/components/Slider";
import Footer from "~/components/Footer";

// регистрируем наш компонент:
export default {
  name: "default",
  components: {
    Footer,
    Slider,
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
