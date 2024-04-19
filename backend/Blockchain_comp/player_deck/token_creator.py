import requests
import os
import json
from pprint import pprint
from web3 import Web3, HTTPProvider
import sys
# File paths are written with the assumption this is being run from its current location, the truffle directory.
sys.path.append('/../../AI_comp')
from ai import starter_pack

private_key = "2f67646d4bc58ea4e07bc98ef759704d4fcbf91aee3db3871f30863ad804a47f"

# token_creator takes the 10 characters created by ChatGPT 3.5 in ai.py, stores their information
# in easily accessible json files, then mints an NFT with all the appropriate information.

blockfrost_api_key = "ipfsp4RZYMEmRUGPMX0fOGdUnaE5ynrNWDg3"

base_endpoint = "https://ipfs.blockfrost.io/api/v0"

headers={"project_id":f'{blockfrost_api_key}'}

web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/e13984f0796b4718a19486917341098c"))
contract_path = 'build/contracts/PlanesWalker.json'
contract_address = "0x5E72959b89d271Da4E79a0caf49EAd7c291777A2"

with open(contract_path) as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Character.Image should be commented out during testing, as DALL-E requires a small fee to run.
def generate_metadata(Character):
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

# In the first open() function, "w" as an input only stores the metadata for one character, while "a" stores the metadata for all generated characters.
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
    nonce = web3.eth.get_transaction_count(owner_address)
    tx_dict = contract.functions.safeMint(owner_address, metadata_uri).build_transaction({
        "nonce": nonce,
        "gasPrice": web3.eth.gas_price,
        "from": owner_address
    })
    signed_tx = web3.eth.account.sign_transaction(tx_dict, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def retrieve_metadata(ipfs_hash):
    with open('retrieved_data', 'wb') as f:
        response = requests.get(f'{base_endpoint}/ipfs/gateway/{ipfs_hash}',headers=headers)
        f.write(response)


for character in starter_pack:
    metadata = generate_metadata(character)
    owner_address = '0xBBAc2417C41aD50A37dF157Fee60B4CD34f802b7'
    metadata_uri = store_metadata(metadata)
    mint_receipt = mint_nft(owner_address, metadata_uri)
    print(f"NFT for {character.Name} minted. Transaction hash: {mint_receipt.transactionHash.hex()}")





  