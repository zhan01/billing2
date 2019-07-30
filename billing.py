def calculate_balance(balance, plans, users, history):
    new_user_list = list(balance.keys())

    for conversation in history:
        user = conversation['user']
        user_tariff = users.get(user, 'cheap')
        billing = conversation['duration'] * plans[user_tariff]
        balance[user] = balance[user] - billing

    print(balance)
