<template>
    <div class="agregar"><form action="" > 
        <label for="carbrand"> carBrand</label><br>
            <input type="text" class="form-control" id="carbrand" v-model="predio.car_brand" name="carbrand" placeholder="carbrand"><br>
            <label for="licenseplate">licensePlate</label><br>
            <input type="text" class="form-control" id="licenseplate" v-model="predio.license_plate" name="carbrand" placeholder="licenseplate"><br>
            <button @click.prevent="agregar()"> nuevo predio</button><br>
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

