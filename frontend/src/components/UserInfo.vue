<template>
  <div>
    <!-- Your Vue template here -->
  </div>
</template>

<script>

export default {
  name: 'YourComponentName',
  mounted() {
    this.initWeb3();
  },
  methods: {
    async initWeb3() {
      const rpcUrl = 'https://sofia-network-url'; // Replace with your actual RPC URL
      const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
      const contractABI = [/* ABI array here */];
      const contractAddress = '0xYourContractAddressOnTestnet';

      try {
        const signer = provider.getSigner();
        const contract = new ethers.Contract(contractAddress, contractABI, signer);
        const data = await contract.ContractMethod(parm1, parm2);
        console.log(data);
      } catch (error) {
        console.error('Error interacting with the contract:', error);
      }
    }
  }
}
</script>
