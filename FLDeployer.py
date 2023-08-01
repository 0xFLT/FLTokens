import json

from web3 import Web3

from solcx import compile_standard, install_solc


with open("./file.extension", "r") as file:
    filename = file.read()
