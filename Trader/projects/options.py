import os
import json

__options_path = os.path.join('data', 'options.json')


def set_opt(user, bar=None, per=None):
    user = str(user)
    if os.path.exists(__options_path):
        with open(__options_path, 'r') as file:
            data = json.load(file)
            if data:
                if user in data:
                    if bar:
                        data[user]['bar'] = bar
                    if per:
                        data[user]['per'] = per
                else:
                    data[user] = {'per': per, 'bar': bar}

                with open(__options_path, 'w') as f:
                    json.dump(data, f)
                return

    with open(__options_path, 'w') as file:
        json.dump({user: {'per': per, 'bar': bar}}, file)


def get_opt(user):
    user = str(user)
    if os.path.exists(__options_path):
        with open(__options_path, 'r') as file:
            data = json.load(file)
            if data:
                if user in data:
                    return data[user]

    return None
