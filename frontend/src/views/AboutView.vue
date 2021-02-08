<template>
  <div>
    <ClienteView dominio="http://10.0.0.105:8000" />
  </div>
</template>

<script>
import ClienteView from '../components/cliente/Table'
export default {
  name:'AboutView',
  components:{
    ClienteView
  }
}
</script>
