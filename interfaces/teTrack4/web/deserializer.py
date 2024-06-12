from pydantic import BaseModel
from typing import List
import array
import json

class Token(BaseModel):
    tokenId: str
    balance: str

class Tokens(BaseModel):
    items: List[Token]

class Account(BaseModel):
    id: str
    tokens: Tokens

class Accounts(BaseModel):
    items: List[Account]

class IndexedData(BaseModel):
    accounts: Accounts

class IndexedNFTs(BaseModel):
    data: IndexedData

filePath = 'interfaces/teTrack4/data/indexedNFTs.json'

def deserializeData() -> IndexedNFTs:
    f = open(filePath)
    data = json.load(f)
    indexedNfts = IndexedNFTs(**data)
    return indexedNfts