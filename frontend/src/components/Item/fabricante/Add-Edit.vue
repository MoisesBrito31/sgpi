<template>
    <div>
        <div class="card-header mb-3">
            <h4 v-if="fabricanteID!==undefined">Edição de Fabricante</h4>
            <h4 v-else>Cadastro de Fabricante</h4>
        </div>
        <b-form>
        <b-form-group label="Fabricante:" :state="nomeOK"  invalid-feedback="Nome Esperado">
            <b-input-group>
                <b-form-input :state="nomeOK" 
                    type="text" placeholder="Fabricante" v-model="obj.nome" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="País:" >
            <b-input-group>
                <b-form-input 
                    type="text" placeholder="País" v-model="obj.pais" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
         <b-form-group label="Imagem:" >
             <input class="form-control" type="file" name="img" id="img">
         </b-form-group>
        <b-alert
            variant="danger"
            dismissible
            fade
            :show="erro">
                Erro no Servidor - {{erroMsg}}
        </b-alert>
        <b-form-group class="mt-3 pt-3">
            <b-button v-show="obj.id===undefined" @click="Put(true)" v-bind:class="{disabled:!podeCadastrar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Cadastrar (Continuar)</span>
            </b-button>
             <b-button v-show="obj.id===undefined" @click="Put(false)" v-bind:class="{disabled:!podeCadastrar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Cadastrar (Terminar)</span>
            </b-button>
            <b-button v-show="obj.id!==undefined" @click="Put(false)" v-bind:class="{disabled:!podeCadastrar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Alterar</span>
            </b-button>
        </b-form-group>
    </b-form>
    </div>
</template>

<script>
export default {
    data(){
        return{
            erro:false,
            erroMsg:'OK',
            cadastroFalha:false,
            espera:false,
            obj: {nome:'',pais:'',img:''},
            img: '',
        }
    },
    computed:{
        nomeOK(){
            return this.obj.nome.length>0
        },
        podeCadastrar(){
            return this.nomeOK
        }
    },
    created(){
        this.load()
    },
    methods:{
        dataReset(){
            this.obj =  {nome:'',pais:'',img:''}
            this.img = ''
        },
        dataFormat(){
            const form = document.getElementById('img')
            const file = form.files[0]
            const formdata = new FormData()
            if(file!==undefined){formdata.append('img',file,file.name)}
            if(this.obj.id!==undefined){formdata.append('id',this.obj.id)}
            formdata.append('nome',this.obj.nome)
            formdata.append('pais',this.obj.pais)
            return formdata
        },
        async dataLoad(index){
            fetch(`${this.dominio}/api/itens-fabricante/${index}/`,{
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
                }
            }).then(response=>{
                if(response.status===200){
                    return response.json()
                }else{
                    this.erro = true
                    if(response.status===401){throw "Você não tem Autorização"}
                    else if(response.status===404){throw "Dados Inexistentes"}
                    else{throw "erro no api do servidor"}
                }          
            }).then(res=>{
                if(res!==undefined){
                    this.erro=false
                    this.erroMsg = 'OK'
                    this.obj = res
                }else{
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
        },
        async Put(valor){ 
            if(this.podeCadastrar){
                var met = 'post'
                if(this.obj.id!==undefined){met='put'}
            this.espera=true
            fetch(`${this.dominio}/api/itens-fabricante/`,{
                method:met,
                headers:{
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}`                     
                },
                body:this.dataFormat()
            }).then(response=>{
                if(response.status===201){
                    if(valor){
                        this.$bvToast.toast('Cadastrado com Sucesso',{
                            title:'Ação Executada com sucesso',
                            variant:'success',
                            solid:true
                        })
                        this.espera=false
                        this.dataReset()
                        this.erro=false
                        this.$emit('cadastrouVarios')
                    }
                    else{
                        this.espera=false
                        this.$emit('cadastrou')
                    }
                }else if(response.status===200){
                    this.espera=false
                    this.$emit('editou')
                }
                else{
                    this.erro=true
                    this.espera=false
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
            }
        },
        load(){
            console.log(this.fabricanteID)
            if (this.fabricanteID!==undefined){
                this.dataLoad(this.fabricanteID)
            }
        }
    },
    props:{
        dominio: String,
        fabricanteID : Number,
    },
}
</script>