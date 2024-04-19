<script setup>
import { ref, onMounted ,computed} from 'vue';
import {ethers} from 'ethers';
const characters = ref([]);
const winner = ref([]);
const selectedCharacter1 = ref('Select Character 1');
const selectedCharacter2 = ref('Select Character 2');
function selectCharacter(character, index) {
  if (index === 1) {
    selectedCharacter1.value = character.name;
  } else {
    selectedCharacter2.value = character.name;
  }
}
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
async function initWeb3() {
  const rpcUrl = 'https://sepolia.infura.io/v3/e13984f0796b4718a19486917341098c';
  const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
  const contractABI = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "have",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "want",
				"type": "address"
			}
		],
		"name": "OnlyCoordinatorCanFulfill",
		"type": "error"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "OwnershipTransferRequested",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "requestId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256[]",
				"name": "randomWords",
				"type": "uint256[]"
			}
		],
		"name": "RequestFulfilled",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "requestId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint32",
				"name": "numWords",
				"type": "uint32"
			}
		],
		"name": "RequestSent",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "acceptOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "requestId",
				"type": "uint256"
			},
			{
				"internalType": "uint256[]",
				"name": "randomWords",
				"type": "uint256[]"
			}
		],
		"name": "rawFulfillRandomWords",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "requestRandomWords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "requestId",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint64",
				"name": "subscriptionId",
				"type": "uint64"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "str1",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "str2",
				"type": "int256"
			}
		],
		"name": "battle",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_requestId",
				"type": "uint256"
			}
		],
		"name": "getRequestStatus",
		"outputs": [
			{
				"internalType": "bool",
				"name": "fulfilled",
				"type": "bool"
			},
			{
				"internalType": "uint256[]",
				"name": "randomWords",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "lastRequestId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "requestIds",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "s_requests",
		"outputs": [
			{
				"internalType": "bool",
				"name": "fulfilled",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "exists",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
];
  const contractAddress = '0xcb809EcB2Fb42408A090672c6560DB7F8C95689e';
  const defaultAddress = '0xA50e4b19b5Ad9FbaB69Aff8Cc96C8c071Bfa76cf'
  try {
    const wallet = new ethers.Wallet("2f67646d4bc58ea4e07bc98ef759704d4fcbf91aee3db3871f30863ad804a47f",provider)
    const signer = provider.getSigner();
    const contract = new ethers.Contract(contractAddress, contractABI,wallet);
    const data = await contract.battle("130", "2");
    console.log(data);
    if(data){
      winner.value=1;
      }
  else{
    winner.value=2;
  }
  } catch (error) {
    console.error('Error interacting with the contract:', error);
  }
};
const combatDescription = computed(() => {
  return `Winner is: ${winner.value}`;
});
</script>

<style scoped>
.container {
  display: flex;

  padding: 20px;
}

.drop-left {
  /* justify-content: left; */
  position: relative;
  top: 20px;
  left: -250px;
  flex: 1;
}

.drop-right {
  position: relative;
  top: 0px;
  left: 700px;
  flex: 1;
}

.battle-button {
  bottom: -300px;
  justify-content: center;
  margin: 0 20px;
}
</style>
<template>
  <div class="container">
    <div class="drop-left">
      <a-dropdown>
        <a class="ant-dropdown-link" @click="selectCharacter(character, 1)">
          Select Character 1 <a-icon type="down" />
        </a>
        <template #overlay>
          <a-menu>
            <a-menu-item v-for="character in characters.slice(0, 10)" :key="character.name + '1'">
              <a href="javascript:void(0);">{{ character.name }}</a>
            </a-menu-item>
          </a-menu>
        </template>
      </a-dropdown>
    </div>
    <div class="drop-right">
      <a-dropdown>
        <a class="ant-dropdown-link" @click.prevent>
          Select Character 2 <a-icon type="down" />
        </a>
        <template #overlay>
          <a-menu>
            <a-menu-item v-for="character in characters.slice(10, 20)" :key="character.name + '2'">
              <a href="javascript:void(0);">{{ character.name }}</a>
            </a-menu-item>
          </a-menu>
        </template>
      </a-dropdown>
    </div>

    <a-button type="primary" class="battle-button" @click="initWeb3">Battle</a-button>
    <div v-if="winner">
    <a-alert v-if="winner" type="info" message="Combat finished" :description="combatDescription" show-icon />
      </div>


  </div>
</template>

<script>
import {
  Layout, // This import includes LayoutHeader, LayoutContent, LayoutFooter
  Menu,
  Alert,
  Button,
  MenuItem,
  Breadcrumb,
  BreadcrumbItem,
  Dropdown
} from 'ant-design-vue';

export default {
  name: 'App',
  components: {
    AAlert :Alert,
    ALayout: Layout,
    AButton: Button,
    ALayoutHeader: Layout.Header,
    ALayoutContent: Layout.Content,
    ALayoutFooter: Layout.Footer,
    AMenu: Menu,
    AMenuItem: MenuItem,
    ADropdown: Dropdown,
    ABreadcrumbItem: BreadcrumbItem
  }
};
</script>
