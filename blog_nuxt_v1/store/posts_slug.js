import axios from "axios";

export default {
  state: () => ({
    post: [],
    tags: [],
    aside: [],
    comments: []
  }),
  getters: {

  },
  actions: {
    async loadComments({commit, rootState}, {slug}) {
      // """Загрузить коментарии для поста"""
      const comments = await this.$axios.get(rootState.baseURL + `/api/comments/${slug}`).catch(({ response })=>{console.log(response)});
      commit('SET_COMMENTS', comments.data)
    },

    async loadSinglePost({commit, rootState, dispatch}, {slug}) {
      // """Загрузить все данные для поста"""

      // action
      await dispatch('loadComments', {slug: slug})

      // req
      const post = await this.$axios.get(rootState.baseURL + `/api/posts/${slug}`);
      const tags = await this.$axios.get(rootState.baseURL + `/api/tags/`);
      const aside = await this.$axios.get(rootState.baseURL + `/api/aside/`);

      // mutations
      commit('SET_POST', post.data)
      commit('SET_TAGS', tags.data)
      commit('SET_ASIDE', aside.data)
    }
  },
  mutations: {
    SET_POST (state, post) {
      state.post = post
    },
    SET_TAGS (state, tags) {
      state.tags = tags
    },
    SET_ASIDE (state, aside) {
      state.aside = aside
    },
    SET_COMMENTS (state, comments) {
      state.comments = comments
    },
  },
}


