<script setup>
import {useWallet} from './userWallet'


const { account } = useWallet();
</script>

<template>
  <div>
    {{account}}
  </div>
</template>

<!-- <script> -->

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
