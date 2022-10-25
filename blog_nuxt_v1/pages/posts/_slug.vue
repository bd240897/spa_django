<template>
  <div>
    <Header :h1=post.h1 />
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <nav aria-label="breadcrumb" class="mt-4">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><nuxt-link to="/">Главная</nuxt-link></li>
              <li class="breadcrumb-item active" aria-current="page">{{ post.h1 }}</li>
            </ol>
          </nav>
          <img class="img-fluid rounded " :src="post.image" alt="">
          <hr>
          <p v-html="post.content">
          </p>
          <div class="d-flex justify-content-end">
          <span v-for="tag in post.tags">
                <nuxt-link :to="`/tags/${tag}`" class="mr-1 badge badge-info">#{{ tag }}</nuxt-link>
          </span>
          </div>

          <hr>
          <div class="d-flex">
            <div class="mr-auto p-2 lead">Автор: {{ post.author }}</div>
            <div class="p-2">Опубликовано: {{ post.created_at }}</div>
          </div>
          <hr>
          <Comments :comments="comments" :post="post"/>
        </div>
        <Aside :tags=tags :aside=aside />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import post_detail from "@/layouts/post_detail";
import Header from "@/components/Header";
import Aside from "@/components/Aside";
import Comments from "@/components/Comments";
import {mapState} from "vuex";

export default {
  components: {
    Aside,
    Header,
    Comments,
  },
  layout: "post_detail",

  // предзагрузка
  async fetch({store, route}) {
    await store.dispatch('posts_slug/loadSinglePost', {slug: route.params.slug})
  },

  computed: {
    // загрузка данных о посте
    ...mapState('posts_slug', ['post', 'tags', 'aside', 'comments',]),
  },

  head() {
    return {
      // титул
      title: this.post.title,

      // мета-данные
      meta: [
        {
          hid: "description",
          name: "description",
          content: this.post.description
        },
        {
          property: "og:url",
          content: `http://localhost:3000${this.$route.path}`
        },
        {
          property: "og:type",
          content: "website"
        },
        {
          property: "og:title",
          content: `${this.post.title}`
        },
        {
          property: "og:description",
          content: `${this.post.description}`
        },
        {
          property: "og:site_name", content: "Мой супер-пупер блог"
        },
        {
          property: "og:locale", content: "ru_RU"
        },
        {
          property: "og:image",
          content: "ссылка на картинку"
        },
        {
          property: "og:image:alt",
          content: "Описание картинки"
        },
        {
          property: "fb:app_id", content: "23456789"
        },
        {
          name: "twitter:card", content: "summary_large_image"
        },
        {
          name: "twitter:site", content: "http://localhost:3000"
        },
        {
          name: "twitter.title",
          content: `${this.post.title}`
        },
        {
          name: "twitter:description",
          content: `${this.post.description}`
        },
        {
          name: "twitter:image:src",
          content: "http://localhost:3000/img"
        }
      ]
    };
  },
}
</script>

<style scoped>

</style>
