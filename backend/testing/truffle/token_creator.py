import os
import json
import nft_storage
from web3 import Web3, HTTPProvider
from pprint import pprint
from dotenv import load_dotenv
from nft_storage.api import nft_storage_api
from nft_storage.model.get_response import GetResponse
from nft_storage.model.error_response import ErrorResponse
from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse
from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse

import sys
sys.path.append('/home/mick/Documents/S24_Chain_Cards/backend/AI_comp')
from ai import starter_pack

load_dotenv()

configuration = nft_storage.Configuration(
    host = "https://api.nft.storage"
)

configuration = nft_storage.Configuration(
    access_token = os.getenv("NFTStorage_API_KEY")
)

web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/e13984f0796b4718a19486917341098c"))
# web3.eth.defaultAccount = web3.eth.accounts[0]

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

    with nft_storage.ApiClient(configuration) as api_client:
        api_instance = nft_storage_api.NFTStorageAPI(api_client)
        body = open("/home/mick/Documents/S24_Chain_Cards/backend/metadata.json")
    api_response = api_instance.store(body)
    pprint(api_response)
    os.remove("metadata.json")

