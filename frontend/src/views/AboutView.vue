<template>
  <div>
    <ItemView :itemID=65 dominio="http://10.0.0.105:8000"/>
  </div>
</template>

<script>
import ItemView from '../components/Item/View'
export default {
  name:'AboutView',
  components:{
    ItemView
  }
}
</script>
