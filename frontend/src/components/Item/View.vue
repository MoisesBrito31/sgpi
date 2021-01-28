<template>
    <div>
    <b-modal size="lg" v-model="showModalEdit" ok-only>
        <ItemEdit :itemID=itemID :dominio=dominio @cadastrou="editou"/>
    </b-modal>
    <b-overlay rounded="sm" :show="!loadFim">
        <div class="card">
            <div class="card-header row">
                <div class="card-title form-inline col">
                    <h2>{{Item.nome}} (<a target="blank" :href="`https://www.bannerengineering.com/us/en/products/part.${Item.codigo}.html`">{{Item.codigo}}</a>)</h2>                
                </div>
                <div class="text-right col">
                        <b-button @click="showModalEdit=true" variant="light">
                        <b-icon icon="pencil" variant="dark"></b-icon>
                    </b-button>
                </div>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-auto m-auto pb-5">
                        <b-img v-show="Item.img!==null" :src=Item.img v-bind="imgProps"></b-img>
                    </div>
                    <div class="col-6 pb-5" style="min-width: 350px;">
                        <div class="form-group">
                            <label><strong><h5> Descriçao:</h5></strong></label>
                            <p>
                                {{Item.descricao}}
                            </p>
                        </div>
                        <div class="row mt-5">
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Fabricante:</h5></strong></label>
                                    <p>{{Item.fabricante}}</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Linha:</h5></strong></label>
                                    <p>{{Item.linha}}</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Tipo:</h5></strong></label>
                                    <p>{{Item.tipo}}</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Familia:</h5></strong></label>
                                    <p>{{Item.familia}}</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Preço:</h5></strong></label>
                                    <p>R$   {{Item.preco}}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col form-inline">
                         <div class="col-auto p-2 m-2 text-center" v-show="Item.cad!==''">
                            <a target="_blank" :href="Item.cad">
                                 <b-icon icon="file-earmark-text" font-size="70" variant="dark"></b-icon>
                            </a>
                            <h4 class="h5 text-center">CAD</h4>
                        </div>
                        <div class="col-auto p-2 m-2 text-center" v-show="Item.datasheet!==''">
                            <a target="_blank" :href="Item.datasheet">
                                <b-icon icon="file-earmark-text" font-size="70" variant="dark"></b-icon>
                            </a>
                            <h5 class="h5 text-center">DataSheet</h5>
                        </div>
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
import ItemEdit from './Edit'
export default {
    components:{
        ItemEdit
    },
    data(){
        return{
            showModalEdit:false,
            Item:{},
            item:'',
            fabricante:'',
            linha:'',
            tipo:'',
            familia:'',
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
            this.Item = this.item
            this.item.fabricante = this.fabricante.nome
            this.item.linha = this.linha.nome
            this.item.tipo = this.tipo.nome
            this.item.familia = this.familia.nome
        },
        load(){
            this.loadItem(this.itemID)
        },
        async loadItem(index){
            fetch(`${this.dominio}/api/itens/${index}/`,{
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
                    this.item = res
                    this.loadFabricante(this.item.fabricante)
                }else{
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
        },
        async loadFabricante(index){
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
                    this.fabricante = res
                    this.loadLinha(this.item.linha)
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
        },
        async loadLinha(index){
             fetch(`${this.dominio}/api/itens-linha/${index}/`,{
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
                    this.linha = res
                    this.loadTipo(this.item.tipo)
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
        },
        async loadTipo(index){
             fetch(`${this.dominio}/api/itens-tipo/${index}/`,{
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
                    this.tipo = res
                    this.loadFamilia(this.item.familia)
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
        },
        async loadFamilia(index){
             fetch(`${this.dominio}/api/itens-familia/${index}/`,{
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
                    this.familia = res
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
        itemID: Number,
    }
    
}
</script>