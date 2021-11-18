<template>
    <div class="agregar"><form action="" > 
        <label for="carbrand"> carBrand</label><br><br>
            <input type="text" class="form-control" id="carbrand" v-model="predio.car_brand" name="carbrand" placeholder="carbrand"><br><br>
            <label for="licenseplate">licensePlate</label><br><br>
            <input type="text" class="form-control" id="licenseplate" v-model="predio.license_plate" name="carbrand" placeholder="licenseplate"><br><br>
            <br><button @click.prevent="agregar()"> agregar predio</button><br><br>
            </form></div>
</template>

<script>
import gql from 'graphql-tag'

export default {
    name: "agregar",
    data(){
        return {
            predio:{
                car_brand: null,
                license_plate: null
            }
        }
    },
    methods: {
        agregar(){
            this.$apollo.mutate({
                mutation: gql`mutation add {
                    addPredio(					
                      carBrand: "${this.predio.car_brand}"
                      licensePlate: "${this.predio.license_plate}"
                    )
                    {
                    predio {
                            carBrand
                        } 
                    }
                }`, 
                variables: {
                    predio: this.predio
                }
            })
        }
    }
}

</script>

