
export default {
  state: () => ({

  }),
  getters: {},
  actions: {
    async addComment({commit, rootState}, {text}) {
      try {
        let response = await this.$axios.post(rootState.baseURL + '/comments/', {
          post: this.$props.post.slug,
          username: this.user.username,
          text: this.new_comment,
        })
        this.new_comment = '';
        this.comments.splice(0, 0, response.data)
        console.log(response)
      }
      catch (err) {
        console.log(err)
      }
    },
    //
    //
    // async loadSearch({commit, rootState}, {query_q, query_page}) {
    //   let page_and_search = query_page !== undefined ? `?page=${query_page}&q=${query_q}` : `?q=${query_q}`;
    //   const { data } = await this.$axios.get(encodeURI(rootState.baseURL + `/api/posts/${page_and_search}`));
    //   let next = data.next != null ? data.next.split('/')[5] : data.next;
    //   let previous = data.previous != null ? data.previous.split('/')[5] : data.previous;
    //   let current_page = query_page
    //   let search_query = query_q
    //
    //   commit('SET_POSTS', data)
    //   commit('SET_TOTAL', Math.ceil(data.count / 6))
    //   commit('SET_NEXT', next)
    //   commit('SET_PREVIOUS', previous)
    //   commit('SET_CURRENT_PAGE', Number(current_page))
    //   commit('SET_SEARCH_QUERY', search_query)
    // },

  },
  mutations: {
    SET_POSTS (state, posts) {
      state.posts = posts
    },
    SET_TOTAL (state, total) {
      state.total = total
    },
    SET_NEXT (state, next) {
      state.next = next
    },
    SET_PREVIOUS (state, previous) {
      state.previous = previous
    },
    SET_CURRENT_PAGE (state, current_page) {
      state.current_page = current_page
    },
    SET_SEARCH_QUERY (state, search_query) {
      state.current_page = search_query
    },
  },
}


