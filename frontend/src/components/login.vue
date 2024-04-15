<script setup>
import { useRouter } from 'vue-router';
import { ref, computed } from 'vue';
const headerStyle = {
  textAlign: 'center',
  color: '#fff',
  height: 64,
  paddingInline: 50,
  lineHeight: '64px',
  backgroundColor: '#7dbcea',
};

const account = ref(null);

const walletDescription = computed(() => {
  return `Address: ${account.value}`;
});

const router = useRouter();

async function connectWallet() {
  if (typeof window.ethereum !== 'undefined') {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      account.value = accounts[0];
      localStorage.setItem('connectedWallet', account.value); // Store the connected wallet address in local storage
      goToMainPage();
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  } else {
    alert('Please install MetaMask!');
  }
}



async function goToNextPage() {
  router.push('/main');
}
</script>

<template>
  <a-layout class="layout">
    <a-layout-header :style="headerStyle">
      Welcome to the Chain Card
    </a-layout-header>
    <main>
      <div id="app" class="container">
        <a-button type="primary" @click="connectWallet">Connect to MetaMask</a-button>
        <div v-if="account" class="message">
          <a-alert type="success" message="Wallet Connected" :description="walletDescription" show-icon />
          <div>
            <a-button type="primary" @click="goToNextPage">Start</a-button>
          </div>
        </div>
      </div>
    </main>
  </a-layout>
</template>



<script>


import { Button as AButton, Alert as AAlert, Layout as ALayout, LayoutHeader as ALayoutHeader, LayoutContent as ALayoutContent } from 'ant-design-vue';

export default {
  name: 'App',
  components: {
    AButton,
    AAlert,
    ALayout,
    ALayoutHeader,
    ALayoutContent
  }
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  padding: 60px;
  width: 100%;
}

main {
  width: 100%;
}

.message {
  width: 100%;
  margin-top: 15px;
}
</style>