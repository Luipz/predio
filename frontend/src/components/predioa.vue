<template>
  <div>
    <ul> 
        <li :key="predioa.id" v-for="predioa  in predioas.data.allPredios" >
          {{predioa.carBrand +' '+ predioa.licensePlate}}
        </li>
    </ul>    
  </div>
</template>
<script>

import gql from 'graphql-tag'
  export default {
    name: 'predioList',    
    data () {
      return {
        predioas: ''
      }
    },    

    methods:
    {
      async leerPredioas(){
        const predioasGraphql = await this.$apollo.query({
        query: gql`query {
                   allPredios {
                      id
                      carBrand
                      licensePlate
                    }
                  }`,     
        })
        this.predioas = predioasGraphql
      }      
    },
    mounted () {
      this.leerPredioas()
    }
  }
</script>