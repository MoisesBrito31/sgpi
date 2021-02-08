<template>
    <div class="animate__animated animate__fadeInDown">
    <b-modal size="lg" v-model="showModalEdit" ok-only>
        <ClienteEdit :clienteID=clienteID :dominio=dominio @editou="editou"/>
    </b-modal>
    <b-overlay rounded="sm" :show="!loadFim">
        <div class="card">
            <div class="card-header row">
                <div class="card-title form-inline col">
                    <h2>{{Obj.nome}} </h2>               
                </div>
                <div class="text-right col">
                        <b-button @click="showModalEdit=true" variant="light">
                        <b-icon icon="pencil" variant="dark"></b-icon>
                    </b-button>
                </div>
            </div>
            <div class="card-body">
                <div class="row m-auto">
                    <div class="col-auto m-auto pb-5">
                        <b-img v-show="Obj.logo!==null" :src=obj.logo v-bind="imgProps"></b-img>
                    </div>
                    <div class="col">
                        <div class="form-group">
                            <label><strong><h5>Industria:</h5></strong></label>
                            <p>{{Obj.industria}}</p>
                        </div>
                    </div>
                    <div class="col">
                        <div class="form-group">
                            <label><strong><h5>Endereço:</h5></strong></label>
                            <p>{{Obj.endereco}}</p>
                        </div>
                    </div>
                    <div class="col">
                        <div class="form-group">
                            <label><strong><h5>CNPJ:</h5></strong></label>
                            <p>{{Obj.cnpj}}</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-auto m-auto">
                        <div class="text-center text-dark m-2 p-1">
                            <h3>Responsaveis</h3> 
                        </div>
                        <RespView :filtroCliente="clienteID" :dominio="dominio" />
                    </div>
                    <div class="col-auto m-auto">
                        <RespView :filtroCliente="clienteID" :dominio="dominio" />
                    </div>
                </div>
            </div>
        </div>
        <template #overlay>
            <div class="text-center">
                <div v-if="erro">
                    <b-icon icon="x-circle" :animation="erroAnima" font-scale="4" ></b-icon>
                    <p class="text-danger">{{erroMsg}}</p>
                </div>
                <div v-else>
                    <b-icon icon="arrow-clockwise" animation="spin" font-scale="4"></b-icon>
                </div>
            </div>
        </template>
    </b-overlay>
    </div>
</template>

<script>
import ClienteEdit from '../cliente/Add-Edit'
import RespView from '../cliente/responsavel/Table'
export default {
    components:{
        ClienteEdit,
        RespView
    },
    data(){
        return{
            showModalEdit:false,
            Obj:{},
            obj:{},
            industria:{},
            erro:false,
            erroMsg:'OK',
            loadFim:false,    
            imgProps:{ width: 200, height: 200}        
        }
    },
    created(){
        this.load()
    },
    methods:{
        editou(){
            this.showModalEdit=false
            this.load()
            this.$bvToast.toast('Editado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true})
        },
        dataFormat(){
            this.Obj = this.obj
            this.obj.industria = this.industria.nome
        },
        load(){
            this.loadData(this.clienteID)
        },
        async loadData(index){
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
                    this.loadIndustria(this.obj.industria)
                }else{
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
        },
        async loadIndustria(index){
             fetch(`${this.dominio}/api/clientes-industria/${index}/`,{
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
                    this.industria = res
                    this.loadFim=true
                    this.dataFormat()
                    this.erro=false
                    this.erroMsg = 'OK'
                }else{
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
        }
    },
    props:{
        dominio: String,
        clienteID: Number,
    }
    
}
</script>