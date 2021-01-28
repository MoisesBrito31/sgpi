<template>
    <div>
        <h2>Login de usuario</h2>
        <hr>
        <Login @logou="logado" dominio="http://10.0.0.105:8000" />
    </div>
</template>

<script>
import Login from '../components/Login'
export default {
    components:{
        Login
    },
    methods:{
        logado(){
            setTimeout(location.href='/',2000)
        }
    }
}
</script>