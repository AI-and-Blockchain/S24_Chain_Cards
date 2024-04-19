<script setup>
import { ref, onMounted } from 'vue';
import UserInfo from './UserInfo.vue';
import Combat from './Combat.vue';
import Trade from './Trade.vue';
import {useWallet} from './userWallet'


const { account } = useWallet();


const selectedKeys = ref(['1']); // Default selected menu item

// function checkForConnectedWallet() {
//   try {
//     const storedAccount = localStorage.getItem('connectedWallet');
//     if (storedAccount) {
//       account.value = storedAccount;
//     }
//   } catch (error) {
//     console.error('Failed to check for connected wallet:', error);
//   }
// }

// onMounted(async () => {
//   await checkForConnectedWallet();
// });

</script>

<template>
  <a-layout class="layout">
    <a-layout-header>
      <div class="logo" />
      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">Cards</a-menu-item>
        <a-menu-item key="2">combet</a-menu-item>
        <a-menu-item key="3">trade</a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <UserInfo v-if="selectedKeys[0] === '1'"/>
      <Combat v-if="selectedKeys[0] === '2'"/>
      <Trade v-if="selectedKeys[0] === '3'"/>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Chain card
    </a-layout-footer>
  </a-layout>
</template>

<script>
import { 
  Layout, // This import includes LayoutHeader, LayoutContent, LayoutFooter
  Menu,
  MenuItem,
  Breadcrumb,
  BreadcrumbItem
} from 'ant-design-vue';

export default {
  name: 'App',
  components: {
    ALayout: Layout,
    ALayoutHeader: Layout.Header,
    ALayoutContent: Layout.Content,
    ALayoutFooter: Layout.Footer,
    AMenu: Menu,
    AMenuItem: MenuItem,
    ABreadcrumb: Breadcrumb,
    ABreadcrumbItem: BreadcrumbItem
  }
};
</script>

<style scoped>
.site-layout-content {
  min-height: 280px;
  padding: 24px;
  background: #fff;
}
#components-layout-demo-top .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}
.ant-row-rtl #components-layout-demo-top .logo {
  float: right;
  margin: 16px 0 16px 24px;
}
[data-theme='dark'] .site-layout-content {
  background: #141414;
}
</style>
