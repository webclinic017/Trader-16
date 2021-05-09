import os
import json

__bank_path = os.path.join('data', 'bank.json')


def set_cash(user, cash):
    user = str(user)
    if os.path.exists(__bank_path):
        with open(__bank_path, 'r') as file:
            data = json.load(file)
            if data:
                data[user] = cash
                with open(__bank_path, 'w') as f:
                    json.dump(data, f)
                return

    with open(__bank_path, 'w') as file:
        json.dump({user: cash}, file)


def get_cash(user):
    user = str(user)
    if os.path.exists(__bank_path):
        with open(__bank_path, 'r') as file:
            data = json.load(file)
            if data:
                if user in data:
                    return int(data[user])

    return None
