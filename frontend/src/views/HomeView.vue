<template>
  <div>
    <ItemTb dominio="http://10.0.0.105:8000" />
  </div>
</template>

<script>
import ItemTb from '../components/Item/Table'
export default {
  name: 'Home',
  components:{
    ItemTb
  }
}
</script>
