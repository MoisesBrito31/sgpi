import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
import '../node_modules/bootstrap-vue/dist/bootstrap-vue.css'
import '../node_modules/animate.css/animate.min.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.prototype.$frontend = "http://localhost:8000"

new Vue({
  router,
  created:function(){
    this.dominio = "http://localhost:8000"
  },
  render: h => h(App)
}).$mount('#app')
