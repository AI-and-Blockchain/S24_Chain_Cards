<script setup>
</script>


<template>
  <a-layout class="layout">
    <a-layout-header>
      <div>Welcome to the Chain Card</div>
    </a-layout-header>
    <main>
      <div id="app" class="container">
        <a-button type="primary" @click="connectWallet">Connect to MetaMask</a-button><br>
        <div v-if="account" class="message">
          <a-alert type="success" message="Wallet Connected" :description="`Address: ${account}`" show-icon /><br>
          <a-button type="primary" @click="">Start</a-button>
        </div>
      </div>
    </main>
  </a-layout>
</template>

<!-- <template>
    <header>
      <div>Welcome to the Chain Card</div>
    </header>
    <main>
      <div id="app" class="container">
        <a-button type="primary" @click="connectWallet">Connect to MetaMask</a-button>
        <div v-if="account" class="message">
          <a-alert type="success" message="Wallet Connected" :description="`Address: ${account}`" show-icon />
        </div>
      </div>
    </main>
</template> -->


<script>
import { ref, computed } from 'vue';
import { ethers } from 'ethers';
import { Button as AButton, Alert as AAlert, Layout as ALayout, LayoutHeader as ALayoutHeader, LayoutContent as ALayoutContent } from 'ant-design-vue';


export default {
  name: 'App',
  components: {
    AButton,
    AAlert,
    ALayout,
    ALayoutHeader,
    ALayoutContent
  },
  setup() {
    const account = ref(null);

    const walletDescription = computed(() => {
      return `Address: ${account.value}`;
    });

    async function connectWallet() {
      if (typeof window.ethereum !== 'undefined') {
        try {
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          account.value = accounts[0];
        } catch (error) {
          console.error('Failed to connect wallet:', error);
        }
      } else {
        alert('Please install MetaMask!');
      }
    }

    return { account, connectWallet, walletDescription };
  },
};
</script>

<style>
.header{

}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px;
  width: 100%;
}

.message {
  width: 100%;
  margin-top: 15px;
  align-items: center;
}

</style>