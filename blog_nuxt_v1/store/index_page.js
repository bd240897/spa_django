
export default {
  state: () => ({
    posts: [],
    total: [],
    next: [],
    previous: [],
    current_page: 0,
    text_in: 'text_in',
  }),
  getters: {

  },
  actions: {
    async loadAllPosts({commit, rootState}, {query_page}) {
      let page = query_page !== undefined ? `?page=${query_page}` : '';
      const { data } = await this.$axios.get(rootState.baseURL + `/api/posts/${page}`);
      let next = data.next != null ? data.next.split('/')[5] : data.next;
      let previous = data.previous != null ? data.previous.split('/')[5] : data.previous;
      let current_page = query_page !== undefined ? query_page : '1';

      commit('SET_POSTS', data.results)
      commit('SET_TOTAL', Math.ceil(data.count / 6))
      commit('SET_NEXT', next)
      commit('SET_PREVIOUS', previous)
      commit('SET_CURRENT_PAGE', Number(current_page))
    }
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
  },
}
