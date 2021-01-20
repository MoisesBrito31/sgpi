<template>
  <div>
    <div v-for="(i,index) in Itens" :key="index">
      <p>{{i.nome}}</p>
      <p>{{i.preco}}</p>
      <p>{{i.descricao}}</p>
    </div>
    
  </div>
</template>

<script>

export default {
  name: 'Home',
  data(){
    return{
      Itens:[]
    }
  },
  async created(){
    await this.load()
  },
  methods:{
    async load(){
      var res = await fetch("http://localhost:8000/api/itens/",{
        method: 'get',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
        }
      })
      this.Itens = await res.json()
      console.log(this.Itens)
    }
  }
}
</script>
