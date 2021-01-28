<template>
    <div>
         <b-modal size="lg" v-model="modalFabricante" ok-only @hide="fabriCadastrou">
            <FabriAdd :dominio=dominio @cadastrou="fabriCdt=true;modalFabricante=false" 
                @cadastrouVarios="fabriCdt=true" />
        </b-modal>
        <b-modal size="lg" v-model="modalLinha" ok-only @hide="linhaCadastrou">
            <LinhaAdd :dominio=dominio @cadastrou="linhaCdt=true;modalLinha=false" 
                @cadastrouVarios="linhaCdt=true" />
        </b-modal>
        <b-modal size="lg" v-model="modalTipo" ok-only @hide="tipoCadastrou">
            <TipoAdd :dominio=dominio @cadastrou="tipoCdt=true;modalTipo=false" 
                @cadastrouVarios="tipoCdt=true" />
        </b-modal>
         <b-modal size="lg" v-model="modalFami" ok-only @hide="famiCadastrou">
            <FamiAdd :dominio=dominio @cadastrou="tipoCdt=true;modalFami=false" 
                @cadastrouVarios="famiCdt=true" />
        </b-modal>
        <div class="card-header mb-3">
            <h4> Cadastro de Produto de Distribuição</h4>
        </div>
        <div class="card-header mb-3">
            <h4>Edição de Produto de Distribuição</h4>
        </div>
        <b-form>
        <b-form-group label="Código:" :state="codigoOK"  :invalid-feedback="codigoInvalido">
            <b-input-group>
                <b-form-input id="codigo" :state="codigoOK" 
                    type="text" placeholder="Código" v-model="Item.codigo" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="Modelo:" :state=nomeOK invalid-feedback="Modelo Esperado" >
            <b-input-group>
                <b-form-input id='nome' :state=nomeOK 
                    type="text"
                    placeholder="Modelo" v-model="Item.nome">
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form inline class="mt-4 mb-4">
           <b-form-group label="Fabricante:" :state=fabriOK class="mr-5">
                <b-input-group >
                    <b-form-select class="mr-2" :state=fabriOK v-model="Item.fabricante" :options=Fabricantes ></b-form-select>
                    <b-button @click="modalFabricante=true" variant='primary'>
                        <b-icon icon='plus'></b-icon>
                    </b-button>
                </b-input-group>           
            </b-form-group>
            <b-form-group label="Tipo:" :state=tipoOK class="mr-5">
                <b-input-group>
                    <b-form-select class="mr-2" :state=tipoOK v-model="Item.tipo" :options=Tipos ></b-form-select>
                    <b-button @click="modalTipo=true" variant='primary'>
                        <b-icon icon='plus'></b-icon>
                    </b-button>
                </b-input-group>           
            </b-form-group>
                <b-form-group label="Linha:" :state=linhaOK class="mr-5">
                <b-input-group>
                    <b-form-select class="mr-2" :state=linhaOK v-model="Item.linha" :options=Linhas ></b-form-select>
                    <b-button @click="modalLinha=true" variant='primary'>
                        <b-icon icon='plus'></b-icon>
                    </b-button>
                </b-input-group>           
            </b-form-group>
            <b-form-group label="Família:" :state=famiOK class="mr-5" >
                <b-input-group>
                    <b-form-select class="mr-2" :state=famiOK v-model="Item.familia" :options=Familias ></b-form-select>
                    <b-button @click="modalFami=true" variant='primary'>
                        <b-icon icon='plus'></b-icon>
                    </b-button>
                </b-input-group>           
            </b-form-group>

            <b-form-group label="Preço:" :state=precoErro class="mr-5" invalid-feedback="Número Inválido">
                <b-form-input @change="dinheiroInput"
                    type="text" :state=precoErro v-model=preco :formatter=dinheiroView >
                </b-form-input>
            </b-form-group>
        </b-form>
        <b-form-group label="Descrição:" >
            <b-form-input
                type="text"
                placeholder="Descrição" v-model="Item.descricao">
            </b-form-input>
        </b-form-group>
        <b-form-group label="Dataheet Link:" >
            <b-form-input
                type="url"
                placeholder="URL" v-model="Item.datasheet">
            </b-form-input>
        </b-form-group>
         <b-form-group label="CAD Link:" >
            <b-form-input
                type="url"
                placeholder="URL" v-model="Item.cad">
            </b-form-input>
        </b-form-group>
         <b-form-group label="Imagem:" >
             <input class="form-control" type="file" name="img" id="img">
         </b-form-group>
        <b-alert
            variant="danger"
            dismissible
            fade
            :show="cadastroFalha">
                Erro no Servidor ao Processar Requisição
        </b-alert>
        <b-form-group class="mt-3 pt-3">
             <b-button @click="Put" v-bind:class="{disabled:!podeCadastrar}"  block variant="primary">
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

<script>import FabriAdd from './fabricante/Add-Edit'
import LinhaAdd from './linha/Add-Edit'
import TipoAdd from './tipo/Add-Edit'
import FamiAdd from './familia/Add-Edit'
export default {
    components:{
        FabriAdd,
        LinhaAdd,
        TipoAdd,
        FamiAdd,
    },
    data(){
        return{
            fabriCdt:false,
            modalFabricante:false,
            linhaCdt:false,
            modalLinha:false,
            tipoCdt:false,
            modalTipo:false,
            famiCdt:false,
            modalFami:false,
            cadastroFalha:false,
            espera:false,
            preco:0,
            precoErro:null,
            img:'',
            Item:{
                codigo:'',
                nome:'',
                descricao:'',
                preco:0,
                datasheet:'',
                cad:'',
                fabricante:0,
                linha:0,
                tipo:0,
                familia:0,
                },
            Fabricantes:[],
            Tipos:[],
            Linhas:[],
            Familias:[],
        }
    },
    computed:{
        codigoOK(){
            return this.Item.codigo.length>4
        },
        codigoInvalido(){
            var qtd = this.Item.codigo.length
            if(qtd<1){return "Código Esperado"}
            else if(qtd<5){return "Código deve ter 5 ou + Caractéres"}
            else{return "OK"}
        },
        nomeOK(){
            return this.Item.nome.length>0
        },
        fabriOK(){
            return this.Item.fabricante>0
        },
        tipoOK(){
            return this.Item.tipo>0
        },
        linhaOK(){
            return this.Item.linha>0
        },
        famiOK(){
            return this.Item.familia>0
        },
        podeCadastrar(){
            return this.codigoOK && this.nomeOK && this.fabriOK &&
            this.tipoOK && this.linhaOK && this.famiOK &&
            this.precoErro===null
        }
    },
    created(){
        this.load()
    },
    methods:{
        dataReset(){
            this.Item =  {
                codigo:'',
                nome:'',
                descricao:'',
                preco:0,
                datasheet:'',
                cad:'',
                fabricante:0,
                linha:0,
                tipo:0,
                familia:0,
                }
            document.getElementById('img').value = ''
        },
        dataFormat(){
            const form = document.getElementById('img')
            const file = form.files[0]
            console.log(file)
            const formdata = new FormData()
            if(file!==undefined){formdata.append('img',file,file.name)}
            formdata.append('id',this.Item.id)
            formdata.append('nome',this.Item.nome)
            formdata.append('codigo',this.Item.codigo)
            formdata.append('fabricante',this.Item.fabricante)
            formdata.append('tipo',this.Item.tipo)
            formdata.append('familia',this.Item.familia)
            formdata.append('linha',this.Item.linha)
            formdata.append('preco',this.Item.preco)
            formdata.append('descricao',this.Item.descricao)
            formdata.append('cad',this.Item.cad)
            formdata.append('datasheet',this.Item.datasheet)
            console.log(formdata.codigo)
            return formdata
        },
        async Put(){ 
            if(this.podeCadastrar){
            this.espera=true
            fetch(`${this.dominio}/api/itens/${this.Item.id}/`,{
                method:'put',
                headers:{
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}`                     
                },
                body:this.dataFormat()
            }).then(response=>{
                if(response.status===200){
                    this.espera=false
                    this.$emit('cadastrou')
                    
                }else{
                    this.cadastroFalha=true
                    this.espera=false
                }
            })
            }
        },
        load(){
            this.loadItem(this.itemID)
        },
        dadosFormat(){
            this.Item = this.item
            this.preco = this.item.preco
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
                    this.carregaFabricante()
                }else{
                    throw "erro no api do servidor"
                }
            }).catch(erro=>{
                this.erro=true
                this.erroMsg = erro
                console.log(erro)
            });
        },      
        async carregaFabricante(){
            fetch(`${this.dominio}/api/itens-fabricante/`,{
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
                    this.Fabricantes.push({'value':res[x].id,'text':res[x].nome})
                }
                this.carregaTipo()
                
            })
        },
        async carregaTipo(){
             fetch(`${this.dominio}/api/itens-tipo/`,{
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
                    this.Tipos.push({'value':res[x].id,'text':res[x].nome})
                }
                this.carregaLinha()
            })
        },
        async carregaLinha(){
            fetch(`${this.dominio}/api/itens-linha/`,{
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
                    this.Linhas.push({'value':res[x].id,'text':res[x].nome})
                }
                this.carregaFamilia()
            })
        },
        async carregaFamilia(){
            fetch(`${this.dominio}/api/itens-familia/`,{
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
                    this.Familias.push({'value':res[x].id,'text':res[x].nome})
                }
                this.dadosFormat()
            })
        },
        dinheiroView(valor){
            if(!valor) {return ''}
            valor = valor.toString()
            if(valor.trim().indexOf('R$   R$')>-1){return ''}
            if(valor.length===0){return ''}
            if (valor.length<5){
                return `R$   ${valor}`
            }else{
                valor = `R$   ${valor.substring(5,valor.length)}`
                return valor
            }
        },
        dinheiroInput(){
                this.precoErro = null
                var st = this.preco.toString()
                var valor = Number(st.substring(5,st.length))
                this.Item.preco = valor
                if (isNaN(this.Item.preco)){
                    this.Item.preco = 0
                    this.precoErro = false
                }
        },
        fabriCadastrou(){
            if(this.fabriCdt){
                this.fabriCdt=false
                this.Fabricantes = []
                this.carregaFabricante()
                this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
            }
        },
        linhaCadastrou(){
            if(this.linhaCdt){
                this.linhaCdt=false
                this.Linhas = []
                this.carregaLinha()
                this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
            }
        },
        tipoCadastrou(){
            if(this.linhaCdt){
                this.tipoCdt=false
                this.Tipos = []
                this.carregaTipo()
                this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
            }
        },
        famiCadastrou(){
            if(this.famiCdt){
                this.famiCdt=false
                this.Familias = []
                this.carregaFamilia()
                this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
            }
        },
    },
    props:{
        dominio: String,
        itemID: String,
    },
}
</script>