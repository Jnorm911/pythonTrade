from kucoin.client import User
from collections import defaultdict
from constant import *

# User
client = User(api_key, api_secret, api_passphrase, is_sandbox=True)
userDetails = client.get_account_list()
userKey = defaultdict(list)
myWallet = None


def getWallets():
    for pairs in userDetails:
        for k, v in pairs.items():
            userKey[k].append(v)

    for i, row in enumerate(userKey["id"]):
        print("Wallet No:", i, row, client.get_account(row))


def getWallet(num):
    global myWallet
    for pairs in userDetails:
        for k, v in pairs.items():
            userKey[k].append(v)

    for i, row in enumerate(userKey["id"]):
        client.get_account(row)
    myWallet = userKey["id"][num]
    return myWallet


def selectWallet():
    num = int(input("Select Wallet: "))
    getWallet(num)

def walletString():
    wallet = myWallet
    return str(wallet)

def returnKey(api_key, api_secret, api_passphrase, is_sandbox=True):
    return api_key, api_secret, api_passphrase, is_sandbox