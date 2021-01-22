<template>
    <div>
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
                <b-button size='md' variant='primary'>
                    <b-icon icon='plus-circle'></b-icon>
                </b-button>
            </b-col>
        </b-row>
        <b-table :filter='filtro' sticky-header striped hover :items=Itens :fields=tbFields head-variant="dark" >
            <template #cell(acao)="row">
                <b-button class="mr-1" size='sm' @click="ItenDel(row.item.id)" variant="primary">
                    <b-icon size='md' icon='pen'></b-icon>
                </b-button>
                <b-button class="mr-1" size='sm' @click="ItenDel(row.item.id)" variant="danger">
                    <b-icon size='md' icon='trash'></b-icon>
                </b-button>
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
    },
    data(){
    return{
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
      Itens:[]
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
    async load(){
      var v = await fetch(`${this.dominio}/api/itens/`,{
        method: 'get',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
          'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
        }
      }).then(function(response){
          if(response.ok){
              return response
          }else{
              throw "erro no api do servidor"
          }          
      })
      .catch(function(erro){
          console.log(erro)
          //alert(erro)
          });

      if(v === undefined){
          this.erro = true
      }else{
            this.erro = false
            this.Itens = await v.json()

            this.loadTipo()
            this.loadFabricante()
            this.loadFim = false
      }
    },
    async loadTipo(){
        this.Itens.forEach(async ele =>{
            var res = await fetch(`${this.dominio}/api/itens/tipo/${ele.tipo}`,{
                methods:'get',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
                }
            })
            var retorno = await res.json()
            ele.tipo = {'id':ele.tipo,'nome':retorno.nome}
        })
    },
    async loadFabricante(){
        this.Itens.forEach(async element => {
            var res = await fetch(`${this.dominio}/api/itens/fabricante/${element.fabricante}`,{
                methods:'get',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Authorization': `Token ${window.localStorage.getItem('api-token')}` 
                }
            })
            var retorno = await res.json()
            element.fabricante={'id':element.fabricante,'nome':retorno.nome}
            });
    },
    limpaPesquisa(){
        this.filtro = ''
    },
    ItenDel(valor){
        alert(valor)
    }
    }
}
</script>
