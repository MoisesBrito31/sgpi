<template>
<div>
    <b-overlay rounded="sm" :show="logado">
        <b-form>
        <b-form-group label="Usuário:"
            :state=userOK :invalid-feedback=userInvalido>
            <b-input-group>
                <b-input-group-prepend is-text>
                    <b-icon-person></b-icon-person>
                </b-input-group-prepend>
                <b-form-input id='username'
                    type="text"
                    placeholder="Usuario" v-model="user.username">
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="Senha:" :state=senhaOK :invalid-feedback=senhaInvalida>
            <b-input-group>
                <b-input-group-prepend is-text>
                    <b-icon-key></b-icon-key>
                </b-input-group-prepend>
                <b-form-input id='password'
                    :type=senhaType
                    placeholder="Senha" v-model="user.password">
                </b-form-input>
                <b-button  @mousedown="mostraSenha" @mouseup="mostraSenha" :variant=senhaClass> <b-icon icon='brightness-alt-high'></b-icon> </b-button>
            </b-input-group>
        </b-form-group>
        <b-alert
            variant="danger"
            dismissible
            fade
            :show="loginFalha"
            @dismissed="showDismissibleAlert=false">
                Usuário ou Senha Incorreto(s)!
        </b-alert>
        <b-form-group class="mt-3 pt-3">
            <b-button @click="chamaLogin" v-bind:class="{disabled:!podelogar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Login</span>
            </b-button>
        </b-form-group>
    </b-form>
        <template #overlay>
            <div class="text-center">
                <b-icon icon="check-circle" animation="throb" font-scale="5" variant="success"></b-icon>
            </div>
        </template>
    </b-overlay>
    
</div>
</template>

<script>
export default {
    data(){
        return{
            logado:false,
            loginFalha: false,
            espera:false,
            senhaType:'password',
            senhaClass:'dark',
            senhaShow: true,
            user:{
                username: '',
                password: ''
            }
        }
    },
    computed:{
        userOK(){
            var valor = this.user.username.length
            return valor>0 && this.user.username.indexOf(' ')<0 
        },
        userInvalido(){
            var valor = this.user.username.length
            if(valor<=0){return "Campo Obrigatorio"}
            else if(this.user.username.indexOf(' ')>0){return "espaço não é permitido"}
            else{return 'ok'}
        },
        senhaOK(){
            return this.user.password.length>5
        },
        senhaInvalida(){
            if(this.user.password.length<=0){
                return "senha Necessária!"
            }else if(this.user.password.length<6){
                return "Senha deve conter no minimo 6 caractáres"
            }else{
                return "ok"
            }
        },
        podelogar(){
            return this.userOK && this.senhaOK
        }
    },
    methods:{
        chamaLogin(){
            this.loginFalha=false;
            if(this.podelogar){
                this.espera = true
                this.login()
                }
        },
        async login() {
            console.log('inicio...')
            var res = await fetch(
                'http://localhost:8000/api-token-auth',{
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json;charset=utf-8'
                    },
                    body: JSON.stringify(this.user)
                }
            )
            var resposta = await res.json()
            if (resposta.token !== undefined){
                window.localStorage.setItem('api-token',resposta.token)
                this.logado = true
                this.espera = false
                setTimeout(function(){location.href='/'},1000)
            }else{
                this.loginFalha=true
                this.espera=false
            }
            
       },
       mostraSenha: function(){
           if(this.senhaShow===true){
               this.senhaShow = false;
               this.senhaClass = 'light';
               this.senhaType = 'text';
           }else{
               this.senhaShow = true;
               this.senhaClass = 'dark';
               this.senhaType = 'password';
           }
       }
    }
}
</script>