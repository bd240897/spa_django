<template>
  <div>

    <div class="card my-4">
      <h5 class="card-header">Прокомментируй:</h5>
      <div class="card-body" v-if="loggedIn">

        <form @submit.prevent="addComment">
          <div class="form-group">
            <textarea class="form-control" rows="3" v-model="new_comment"></textarea>
          </div>
          <button type="submit" class="btn btn-primary" :disabled='!isComplete'>Отправить</button>
        </form>

      </div>

      <div v-else>
        <h6 class="card-header"><nuxt-link to="/signin">Авторизуйтесь</nuxt-link> или <nuxt-link to="/signup">зарегистрируйтесь</nuxt-link> чтобы оставить комментарий</h6>
      </div>
    </div>

    <div class="media mb-4" v-for="comment in comments" :key="comment.id">
      <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
      <div class="media-body">
        <h5 class="mt-0">{{comment.username}}</h5>
        {{comment.text}}
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import {mapState, mapActions} from "vuex";
export default {

  data() {
    return {
      new_comment: '',
    }
  },

  methods: {
    ...mapActions('posts_slug', ['loadComments']),
    async addComment() {
      // """Добавить комментарий"""

      // TODO нужно ли try catch
      try {
        let response = await this.$axios.post(this.$store.state.baseURL + '/api/comments/', {
          post: this.post.slug,
          username: this.user.username,
          text: this.new_comment,
        })
        this.new_comment = '';

        // повторно загрузить данные для поста через vuex
        let slug = this.post.slug
        await this.loadComments({slug})
      }
      catch (err) {
        console.log(err)
      }
    },
  },

  computed: {
    ...mapState('posts_slug', ['post', 'comments',]),
    loggedIn() {
      // """Проверить авторизирован ли пользователь"""
      return this.$auth.loggedIn
    },
    user() {
      // """Получить текущего юзера"""
      return this.$auth.user
    },
    isComplete () {
      // """Проверить заполнен ли коментарий"""
      return this.new_comment;
    },
  }
}
</script>

<style scoped>

</style>
