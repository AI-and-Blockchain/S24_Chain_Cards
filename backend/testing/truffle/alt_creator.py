import requests
import os
import json
from pprint import pprint
from web3 import Web3, HTTPProvider
import sys
sys.path.append('/home/mick/Documents/S24_Chain_Cards/backend/AI_comp')
from ai import starter_pack

blockfrost_api_key = "ipfsp4RZYMEmRUGPMX0fOGdUnaE5ynrNWDg3"

base_endpoint = "https://ipfs.blockfrost.io/api/v0"

headers={"project_id":f'{blockfrost_api_key}'}

web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/e13984f0796b4718a19486917341098c"))
contract_path = '/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/build/contracts/PlanesWalker.json'
contract_address = "0x5E72959b89d271Da4E79a0caf49EAd7c291777A2"

with open(contract_path) as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def generate_matadata(Character):
    metadata = {
        "name": Character.Name,
        "race": Character.Race,
        "class": Character.Class,
        "stats": Character.Stats,
        # "image": Character.Image,
        "backstory": Character.Backstory,
        "equipment": Character.Equipment,
    }
    return metadata

def store_metadata(metadata):
    data = open("metadata.json", "w")
    json.dump(metadata, data)
    data.close()

    with open("metadata.json", "rb") as f:
        response = requests.post(f'{base_endpoint}/ipfs/add', headers=headers, files={'file':f})

    ipfs_hash = response.json()['ipfs_hash']
    pprint(ipfs_hash)

    response = requests.post(f'{base_endpoint}/ipfs/pin/add', headers=headers)
    metadata_uri = f'{base_endpoint}/ipfs/gateway/{ipfs_hash}'
    os.remove("metadata.json")
    return metadata_uri

def mint_nft(owner_address, metadata_uri):
    tx_hash = contract.functions.safeMint(owner_address, metadata_uri)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def retrieve_metadata(ipfs_hash):
    with open('retrieved_data', 'wb') as f:
        response = requests.get(f'{base_endpoint}/ipfs/gateway/{ipfs_hash}',headers=headers)
        f.write(response)


for character in starter_pack:
    metadata = generate_matadata(character)
    owner_address = '0xBBAc2417C41aD50A37dF157Fee60B4CD34f802b7'
    metadata_uri = store_metadata(metadata)
    mint_receipt = mint_nft(owner_address, metadata_uri)
    print(f"NFT for {character.Name} minted. Transaction hash: {mint_receipt.transactHash.hex()}")





