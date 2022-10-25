import axios from "axios";


export default {
  state: () => ({}),
  getters: {},
  actions: {
    async submitForm({state, rootState}, contactFormData) {
      console.log('submitting data...');
      await this.$axios({
        method: 'post',
        url: rootState.baseURL + '/api/feedback/',
        data: contactFormData
      }).then(function (response) {
        console.log(response);
      }).catch(function (response) {
        console.log(response);
      });
      this.$router.push("/success");
    },
  },
  mutations: {},
}


