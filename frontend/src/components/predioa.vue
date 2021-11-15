<template>
  <div>
    <ul>
        <li :key="predioa.id" v-for="predioa  in predioas.data.allPredios" >
          {{predioa.name}}
        </li>
    </ul>    
  </div>
</template>
<script>

import gql from 'graphql-tag'
  export default {
    name: 'PredioList',    
    //definimos la variable que almacenara el listado de ingredientes
    data () {
      return {
        predioas: ''
      }
    },    
    //declaramos un metodo que vaya a leer los ingredientes a GraphQl
    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
      async leerPredioas(){
        //desde aquí se realiza la consulta a Graphql y el resultado se guarda en una constante
        const predioasGraphql = await this.$apollo.query({
        query: gql`query {
                   allPredios {
                      id
                      carBrand
                      licensePlate
                    }
                  }`,     
        })
        //El dato obtenido de Graphql se lo asignamos a la variable ingredientes que se mostrara en el template
        this.predioas = predioasGraphql
      }      
    },

    //el metodo leerIngredientes se ejecutara cada vez que los componentes de la pagina ya esten montados
    mounted () {
      this.leerPredioas()
    }
  }
</script>