<template>
    <div>
        <b-modal centered @ok="deletarItem" v-model="showModalDel" title="Apagar Cliente" no-stacking>
            <p>Deseja Ralmente deletar O Responsável <strong>{{delItem.nome}}</strong>?</p>
        </b-modal>
        <b-modal size="lg" v-model="showModalAdd" ok-only @hide="fazLoad">
            aqui adiciona
            <!--<ClienteAdd :dominio=dominio @cadastrou="clienteCdt=true;showModalAdd=false"
            @cadastrouVarios="clienteCdt=true" />-->
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
        <b-table small responsive :filter='filtro' striped hover :items=Responsaveis :fields=tbFields head-variant="dark" >
            <template #cell(acao)="row">
                <b-button class="mr-1" size='sm' @click="LinhaDetalhes(row)" variant="light">
                    <b-icon size='md' icon='arrow-down'></b-icon>
                </b-button>
                <b-button class="mr-1" size='sm' @click="ItenDel(row.item)" variant="light">
                    <b-icon size='md' icon='trash'></b-icon>
                </b-button>
            </template>
            <template #row-details="row">
                    <!--<ClienteView :clienteID="row.item.id" :dominio="dominio" />-->
                aqui o view do {{row.item.id}}
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
export default {
    components:{
    },
    props:{
        dominio: String,
        filtroCliente: String,
    },
    data(){
    return{
        ResponsavelCtd:false,
        showModalAdd:false,
        delItem:{'id':0,'name':''},
        showModalDel:false,
        erro:false,
        loadFim:true,
        filtro: '',
        podeLimpar: true,
        tbFields:[
            {key:'nome',label:'Nome',sortable:true,},
            {key:'cargo.nome',label:'Cargo',sortable:true, },
            {key:'email',label:'E-Mail',sortable:true, },
            {key:'telefone',label:'Phone',sortable:true, },
            {key:'acao',label:'Ações' },
        ],
      Responsaveis:[],
      Cargos:[],
      RespFiltro:[],
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
    load(){
        if(this.filtroCliente!==undefined){
            this.RespFiltro=[]
            this.carregaDataFiltro()
        }else{
            this.carregaData()
        }
    },
    async carregaData(index){
        if(index===undefined){index=''}
        else{index=`${index}/`}
        fetch(`${this.dominio}/api/clientes-responsavel/${index}`,{
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
            if(res.length!==undefined){
                this.Responsaveis = res
                this.carregaCargo()
            }else{
                this.Responsaveis.push(res)
            }  
          }else{
              this.erro = true
          }
      }).catch(erro=>{
          this.erro = true
          console.log(erro)
          });
    },
    async carregaCargo(){
      fetch(`${this.dominio}/api/clientes-cargo/`,{
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
            this.Cargos = res
            this.atualizaItens()
          }else{
              this.erro = true
          }
      }).catch(erro=>{
          this.erro = true
          console.log(erro)
          });
    },
    async carregaDataFiltro(){
      fetch(`${this.dominio}/api/clientes-relacao?empresa=${this.filtroCliente}&/`,{
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
            if(res.length!==undefined){
                for(var x=0 ; x<res.length;x++){
                    this.RespFiltro.push(res[x].funcionario)
                }
            }else{
                this.RespFiltro.push(res.funcionario)
            }
            for(var y=0 ; y<this.RespFiltro.length;y++){
                this.carregaData(this.RespFiltro[y])
            }
            this.carregaCargo()
          }else{
              this.erro = true
          }
      }).catch(erro=>{
          this.erro = true
          console.log(erro)
          });
    },
    atualizaItens(){
        for(var x=0; x< this.Responsaveis.length; x++){
            for(var y=0 ; y< this.Cargos.length;y++){
                if(this.Responsaveis[x].cargo === this.Cargos[y].id){
                    this.Responsaveis[x].cargo = this.Cargos[y]
                }
            }
        }
        this.loadFim = false
    },
    fazLoad(){
        if(this.respCdt){
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
        fetch(`${this.dominio}/api/clientes-responsavel/${this.delItem.id}/`,{
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
