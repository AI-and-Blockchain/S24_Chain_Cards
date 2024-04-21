import{ref} from 'vue';

const account = ref(null);

export function useWallet(){
    return{
        account
    }
}