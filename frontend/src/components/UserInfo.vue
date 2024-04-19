<!-- <script setup>
import {useWallet} from './userWallet'


const { account } = useWallet();
</script>

<template>
  <div>
    {{account}}
  </div>
</template> -->

<!-- <script> -->
<script setup>
import { ref, onMounted } from 'vue';

const characters = ref([]);

onMounted(() => {
  fetch('/metadata.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      characters.value = data;
    })
    .catch(error => {
      console.error('Error loading the metadata:', error);
    });
});


// import { ref, onMounted } from 'vue';

// const characters = ref([]);

// onMounted(async () => {
//   try {
//     const response = await fetch('/metadata.json');
//     characters.value = await response.json();
//     characters.value = data;
//     console.log(characters.value);  
//   } catch (error) {
//     console.error('Error loading the characters:', error);
//   }
// });
</script>
<template>
  <div>
    <h1>Characters</h1>
    <div v-for="character in characters" :key="character.name" class="Character">
      <h2>{{ character.name }}</h2>
      <p><strong>Race:</strong> {{ character.race }}</p>
      <p><strong>Class:</strong> {{ character.class }}</p>
      <p><strong>Stats:</strong> {{ character.stats }}</p>
      <!-- <img :src="character.image" :alt="character.name" width="200"> -->
      <p><strong>Backstory:</strong> {{ character.backstory }}</p>
      <p><strong>Equipment:</strong> {{ character.equipment }}</p>
    </div>
  </div>
</template>
<style>
.character {
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 20px;
}
</style>
<!-- <script>
import { ref, onMounted } from 'vue';
export default {
  data() {
    return {
      characters: []
    };
  },
  mounted() {
    fetch('C:/Users/13521/Desktop/chaincard/metadata.json') // Adjust path if your JSON is located elsewhere
    .then(response => response.json())
    .then(data => {
      this.characters = data;
    })
    .catch(error => console.error('Error loading the characters:', error));
  }
};
</script> -->

<!-- <style>
.character {
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 20px;
}
</style> -->
// export default{
//   props:['account']
// };
// export default {
//   mounted() {
//     this.initWeb3();
//   },
//   methods: {
//     async initWeb3() {
//       const rpcUrl = 'https://sepolia.infura.io/v3/e13984f0796b4718a19486917341098c'; // Replace with your actual RPC URL
//       const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
//       const contractABI = [/* ABI array here */];
//       const contractAddress = '0xYourContractAddressOnTestnet';

//       try {
//         const signer = provider.getSigner();
//         const contract = new ethers.Contract(contractAddress, contractABI, signer);
//         const data = await contract.ContractMethod(parm1, parm2);
//         console.log(data);
//       } catch (error) {
//         console.error('Error interacting with the contract:', error);
//       }
//     }
//   }
// }
<!-- </script> -->
