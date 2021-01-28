<template>
    <div>
        <b-modal centered @ok="deletarItem" v-model="showModalDel" title="Apagar Item" no-stacking>
            <p>Deseja Ralmente deletar o Item <strong>{{delItem.nome}}</strong>?</p>
        </b-modal>
        <b-modal size="lg" v-model="showModalAdd" ok-only @hide="fazLoad">
            <ItemAdd @cadastrou="showAdd(false)" @cadastrouVarios="cdtVarios=true" :dominio=dominio />
        </b-modal>
        <b-overlay rounded="sm" :show="loadFim">
            <b-row class="m-auto">
            <b-col cols="6">
            <b-form-group >
                <b-input-group>
                    <b-input-group-prepend is-text>
                        <b-icon :variant="lupaVariant" :animation="lupaAnima" icon='search'></b-icon>
                    </b-input-group-prepend>
                    <b-input v-model="filtro"  type='text'></b-input>
                    <b-button v-show="buscando" @click="limpaPesquisa" size='sm' variant='light'>
                        <b-icon icon='x-circle'></b-icon>
                    </b-button>
                </b-input-group>
            </b-form-group>
            </b-col>
            <b-col cols="6" class="text-right">
                <b-button @click="showAdd(true)" size='md' variant='primary'>
                    <b-icon icon='plus-circle'></b-icon>
                </b-button>
            </b-col>
        </b-row>
        <b-table small responsive :filter='filtro' striped hover :items=Itens :fields=tbFields head-variant="dark" >
            <template #cell(acao)="row">
                <b-button class="mr-1" size='sm' @click="LinhaDetalhes(row)" variant="light">
                    <b-icon size='md' icon='arrow-down'></b-icon>
                </b-button>
                <b-button class="mr-1" size='sm' @click="ItenDel(row.item)" variant="light">
                    <b-icon size='md' icon='trash'></b-icon>
                </b-button>
            </template>
            <template #row-details="row">
                <b-collapse :id=row.item.id>
                    <ItemView :itemID=row.item.id :dominio=dominio />
                </b-collapse>
            </template>
        </b-table>
            <template #overlay>
            <div class="text-center">
                <b-icon :icon="erroIcone" :animation="erroAnima" font-scale="4"></b-icon>
            </div>
        </template>
        </b-overlay>
    </div>
</template>

<script>
import ItemAdd from './Add'
import ItemView from './View'
export default {
    components:{
        ItemAdd,
        ItemView
    },
    props:{
        dominio: String,
    },
    data(){
    return{
        cdtVarios:false,
        showModalAdd:false,
        delItem:{'id':0,'name':''},
        showModalDel:false,
        erro:false,
        loadFim:true,
        filtro: '',
        podeLimpar: true,
        tbFields:[
            {key:'codigo',label:'Código',sortable:true,},
            {key:'nome',label:'Modelo',sortable:true,},
            {key:'fabricante.nome',label:'Fabricante',sortable:true, },
            {key:'tipo.nome',label:'Tipo',sortable:true, },
            {key:'acao',label:'Ações' },
        ],
      Itens:[],
      Tipos:[],
      Fabricantes:[],
    }
  },
  created(){
    this.load()
  },
  computed:{
      buscando(){
          if (this.filtro===null || this.filtro==''){
              return false
          }else{
              return this.filtro.length>0
          }
      },
      lupaAnima(){
          if(this.buscando){
              return "throb"
          }else{
              return ""
          }
      },
      lupaVariant(){
          if(this.buscando){
              return "success"
          }else{
              return "dark"
          }
        },
        erroIcone(){
            if (this.erro){
                return 'x-circle'
            }else{
                return 'arrow-clockwise'
            }
        },
        erroAnima(){
            if (this.erro){
                return ''
            }else{
                return 'spin'
            }
        }
  },
  methods:{
      LinhaDetalhes(linha){
          linha.toggleDetails()
          setTimeout(()=>{this.$root.$emit('bv::toggle::collapse',linha.item.id)},10)
      },
    async load(){
      fetch(`${this.dominio}/api/itens/`,{
        method: 'get',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
        }
      }).then(response=>{
          if(response.status===200){
              return response.json()
          }else{
              this.erro = true
              throw "erro no api do servidor"
          }          
      }).then(res=>{
          if(res!==undefined){
            this.erro = false
            this.Itens = res
            this.loadTipo()
          }else{
              this.erro = true
          }
      }).catch(erro=>{
          this.erro = true
          console.log(erro)
          });
    },
    async loadTipo(){
            fetch(`${this.dominio}/api/itens-tipo/`,{
                method:'get',
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
                this.Tipos = res
                this.loadFabricante()
            }).catch(erro=>{
                        this.erro = true
                        console.log(erro)
                    });
    },
    async loadFabricante(){
            fetch(`${this.dominio}/api/itens-fabricante/`,{
                method:'get',
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
                this.Fabricantes = res
                this.atualizaItens()
            }).catch(erro=>{
                        this.erro = true
                        console.log(erro)
                 });
    },
    atualizaItens(){
        for (var x=0; x<this.Itens.length;x++){
                for(var y=0; y<this.Tipos.length;y++){
                    if (Number(this.Itens[x].tipo)==Number(this.Tipos[y].id)){
                        this.Itens[x].tipo=this.Tipos[y]
                    }
                }
                for(var z=0; z<this.Fabricantes.length;z++){
                    if (Number(this.Itens[x].fabricante)==Number(this.Fabricantes[z].id)){
                        this.Itens[x].fabricante=this.Fabricantes[z]
                    }
                }
            }
        this.loadFim = false
    },
    limpaPesquisa(){ this.filtro = '' },
    fazLoad(){
        if (this.cdtVarios){
            this.cdtVarios=false
            this.load()
        }
    },
    showAdd(valor){
        this.showModalAdd = valor
        if(!valor){
            this.load()
             this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
        }
    },
    ItenDel(valor){
        this.delItem = valor
        this.showModalDel = true
    },
    async deletarItem(){
        fetch(`${this.dominio}/api/itens/${this.delItem.id}/`,{
                method:'delete',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
                }
            }).then(response=>{
                console.log(response.status)
                if(response.status === 204){
                    this.$bvToast.toast('Deletado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
                    this.load()
                }else{
                    throw 'falha no servidor'
                }
            }).catch(erro=>{
                        this.$bvToast.toast('Não foi possível deletar',{
                        title:'Falha ao Processar',
                        variant:'danger',
                        solid:true
                    })
                        this.load()
                        console.log(erro)
                 });
    }
}
}
</script>
