<template>
    <div>
        <b-modal centered @ok="deletarItem" v-model="showModalDel" title="Apagar Cliente" no-stacking>
            <p>Deseja Ralmente deletar O Cliente <strong>{{delItem.nome}}</strong>?</p>
            <p>Todos os Relatórios Relacionados serão Apagados também</p>
        </b-modal>
        <b-modal size="lg" v-model="showModalAdd" ok-only @hide="fazLoad">
            <ClienteAdd :dominio=dominio @cadastrou="clienteCtd=true;showModalAdd=false"
            @cadastrouVarios="clienteCtd=true" />
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
                    <b-button v-show="buscando" @click="filtro=''" size='sm' variant='light'>
                        <b-icon icon='x-circle'></b-icon>
                    </b-button>
                </b-input-group>
            </b-form-group>
            </b-col>
            <b-col cols="6" class="text-right">
                <b-button @click="showModalAdd=true" size='md' variant='primary'>
                    <b-icon icon='plus-circle'></b-icon>
                </b-button>
            </b-col>
        </b-row>
        <b-table small responsive :filter='filtro' striped hover :items=Clientes :fields=tbFields head-variant="dark" >
            <template #cell(acao)="row">
                <b-button class="mr-1" size='sm' @click="LinhaDetalhes(row)" variant="light">
                    <b-icon size='md' icon='arrow-down'></b-icon>
                </b-button>
                <b-button class="mr-1" size='sm' @click="ItenDel(row.item)" variant="light">
                    <b-icon size='md' icon='trash'></b-icon>
                </b-button>
            </template>
            <template #row-details="row">
                <ClienteView :clienteID="row.item.id" :dominio="dominio" />
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
import ClienteAdd from '../cliente/Add-Edit'
import ClienteView from '../cliente/View'
export default {
    components:{
        ClienteAdd,
        ClienteView,
    },
    props:{
        dominio: String,
    },
    data(){
    return{
        clienteCtd:false,
        showModalAdd:false,
        delItem:{'id':0,'name':''},
        showModalDel:false,
        erro:false,
        loadFim:true,
        filtro: '',
        podeLimpar: true,
        tbFields:[
            {key:'nome',label:'Cliente',sortable:true,},
            {key:'industria.nome',label:'Indústria',sortable:true, },
            {key:'endereco',label:'Endereço',sortable:true, },
            {key:'acao',label:'Ações' },
        ],
      Clientes:[],
      Industrias:[],
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
      },
    async load(){
      fetch(`${this.dominio}/api/clientes/`,{
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
            this.Clientes = res
            this.loadIndustria()
          }else{
              this.erro = true
          }
      }).catch(erro=>{
          this.erro = true
          console.log(erro)
          });
    },
    async loadIndustria(){
            fetch(`${this.dominio}/api/clientes-industria/`,{
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
                this.Industrias = res
                this.atualizaItens()
            }).catch(erro=>{
                        this.erro = true
                        console.log(erro)
                    });
    },
    atualizaItens(){
        for (var x=0; x<this.Clientes.length;x++){
                for(var y=0; y<this.Industrias.length;y++){
                    if (Number(this.Clientes[x].industria)==Number(this.Industrias[y].id)){
                        this.Clientes[x].industria=this.Industrias[y]
                    }
                }
            }
        this.loadFim = false
    },
    fazLoad(){
        if(this.clienteCtd){
            this.load()
            this.$bvToast.toast('Cadastrado com Sucesso',{
                        title:'Ação Executada com sucesso',
                        variant:'success',
                        solid:true
                    })
        }
        this.clienteCtd=false
    },
    ItenDel(valor){
        this.delItem = valor
        this.showModalDel = true
    },
    async deletarItem(){
        fetch(`${this.dominio}/api/clientes/${this.delItem.id}/`,{
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
