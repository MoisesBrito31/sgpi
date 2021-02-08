<template>
    <div>
        <b-modal size="lg" v-model="modalIndu" ok-only @hide="induCadastrou">
            <InduAdd @cadastrou="induCdt=true;modalIndu=false" @cadastrouVarios="induCdt=true" :dominio=dominio />
        </b-modal>
        <div class="card-header mb-3">
            <h4 v-if="clienteID!==undefined">Edição de Cliente</h4>
            <h4 v-else>Cadastro de Cliente</h4>
        </div>
        <b-form>
        <b-form-group label="Nome:" :state="nomeOK"  invalid-feedback="Nome Esperado">
            <b-input-group>
                <b-form-input :state="nomeOK" 
                    type="text" placeholder="Nome" v-model="obj.nome" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="Indústria:" :state=induOK invalid-feedback="Indústria Esperada" class="mr-5">
            <b-input-group>
                <b-form-select class="mr-2" :state=induOK v-model="obj.industria" :options=Industrias ></b-form-select>
                <b-button @click="modalIndu=true"  variant='primary'>
                        <b-icon icon='plus'></b-icon>
                </b-button>
            </b-input-group>           
        </b-form-group>
        <b-form-group label="Endereço:" >
            <b-input-group>
                <b-form-input 
                    type="text" placeholder="Endereço" v-model="obj.endereco" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="CNPJ:" >
            <b-input-group>
                <b-form-input 
                    type="text" placeholder="CNPJ" v-model="obj.cnpj" trim >
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
import InduAdd from '../cliente/industria/Add-Edit'
export default {
    components:{
        InduAdd,
    },
    data(){
        return{
            modalIndu:false,
            induCdt:false,
            erro:false,
            erroMsg:'OK',
            cadastroFalha:false,
            espera:false,
            obj: {'nome':'','industria':'','endereco':'','cnpj':'',img:''},
            img: '',
            Industrias:[]
        }
    },
    computed:{
        nomeOK(){
            return this.obj.nome.length>0
        },
        induOK(){
            return this.obj.industria!==0 && this.obj.industria!==''
        },
        podeCadastrar(){
            return this.nomeOK && this.induOK
        }
    },
    created(){
        this.load()
    },
    methods:{
        dataReset(){
            this.obj={'nome':'','industria':'','endereco':'','cnpj':'',img:''},
            this.img= ''
        },
        dataFormat(){
            const form = document.getElementById('img')
            const file = form.files[0]
            const formdata = new FormData()
            if(file!==undefined){formdata.append('logo',file,file.name)}
            if(this.obj.id!==undefined){formdata.append('id',this.obj.id)}
            formdata.append('nome',this.obj.nome)
            formdata.append('endereco',this.obj.endereco)
            formdata.append('cnpj',this.obj.cnpj)    
            formdata.append('industria',this.obj.industria)        
            return formdata
        },
        async dataLoad(index){
            fetch(`${this.dominio}/api/clientes/${index}/`,{
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
                var pk = ''
                if(this.obj.id!==undefined){
                    met='put'
                    pk=`${this.obj.id}/`
                }
            this.espera=true
            fetch(`${this.dominio}/api/clientes/${pk}`,{
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
            console.log(this.clienteID)
            if (this.clienteID!==undefined){
                this.dataLoad(this.clienteID)
            }
            this.carregaIndustrias()
        },
        async carregaIndustrias(){
            fetch(`${this.dominio}/api/clientes-industria/`,{
                methods:'get',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
                }
            }).then(response=>{
                if(response.status === 200){
                    return response.json()
                }else{
                    throw 'falha no servidor'
                }
            }).then(res=>{
                for(var x=0 ; x< res.length; x++){
                    this.Industrias.push({'value':res[x].id,'text':res[x].nome})
                }
            })
        },
        induCadastrou(){
            if(this.induCdt){
                this.Industrias = []
                this.carregaIndustrias()
                this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
            }
            this.induCdt=false
        },
    },
    props:{
        dominio: String,
        clienteID : Number,
    },
}
</script>