<template>
  <div>

    <SearchHeader @searchPosts="posts = $event"/>

    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <nav aria-label="breadcrumb" class="mt-4">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><nuxt-link to="/">Главная</nuxt-link></li>
              <li class="breadcrumb-item active" aria-current="page">Поиск</li>
            </ol>
          </nav>
          <p class="lead">Найдено записей: {{posts.count}}</p>
          <div v-for="post in posts.results" :key="post.id">
            <nuxt-link :to="`/posts/${post.slug}`"><h2>{{ post.h1 }}</h2></nuxt-link>
            <p v-html="post.description"></p>
            <hr>
          </div>
        </div>
      </div>
    </div>

    <nav aria-label="Paginate me">
      <ul class="pagination justify-content-center">
        <nuxt-link v-if="previous != null" class="page-link" :to="previous" tabindex="-1">Предыдущая</nuxt-link>
        <li v-else class="page-item disabled">
          <a class="page-link disabled" href="#" tabindex="-1">Предыдущая</a>
        </li>
        <span v-for="i in total">
          <li  v-if="current_page === i || (!$route.query.page && i === 1)" class="page-item active">
            <nuxt-link class="page-link" :to="`?page=${i}&q=${search_query}`">{{i}}</nuxt-link></li>
          <li v-else class="page-item">
            <nuxt-link class="page-link" :to="`?page=${i}&q=${search_query}`">{{i}}</nuxt-link></li>
        </span>
        <nuxt-link v-if="next != null" class="page-link" :to="next">Следующая</nuxt-link>
        <li v-else class="page-item disabled">
          <a class="page-link" href="#">Следующая</a>
        </li>
      </ul>
    </nav>

  </div>
</template>

<script>
import SearchHeader from "@/components/SearchHeader";
import axios from "axios";
import {mapState, mapGetters} from "vuex";

export default {
  name: 'search',
  components: {SearchHeader},
  layout: "post_detail",
  watchQuery: ['q', 'page'],
  async fetch({store, route}) {
    // """Предзагурзка"""
    await store.dispatch('search/loadSearch', {query_page: route.query.page, query_q: route.query.q})
  },
  data() {
    return{}
  },
  created() {},
  methods: {
    ...mapGetters('search', ['getPosts',]),
  },
  computed: {
    ...mapState('search', ['total', 'next', 'previous', 'current_page', 'search_query', 'posts']),
  },
}
</script>

<style scoped>

</style>
