<template>
  <div>
    <ItemTb dominio="http://localhost:8000"/>
  </div>
</template>

<script>
import ItemTb from '../components/Item-tb.vue'
export default {
  name: 'Home',
  components:{
    ItemTb
  }
}
</script>
