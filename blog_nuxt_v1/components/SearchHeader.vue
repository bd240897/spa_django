<template>
  <div class="container-fluid home-slider">
    <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" style="background-color: #343a40!important">
          <div class="w-50 mx-auto py-2">
            <form class="my-2 my-lg-0">
              <input name="q" type="text" class="form-control" placeholder="Поиск" aria-label="Поиск" v-model="q">
              <button class="btn btn-outline-success mt-3" @click.stop.prevent="searchPosts()">Поиск</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      q: '',
      posts: ''
    }
  },
  methods: {
    async searchPosts() {
      this.$store.dispatch('search/loadSearch', {query_page: '1', query_q:  this.q})
      this.$router.push("/search?q="+this.q);this.q
    },
  }
}
</script>

<style scoped>

</style>
