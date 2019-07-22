def calculate_balance(balance, plans, users, history):
    new_user_list = list(balance.keys())

    for conversion in history:
        user = conversion['user']
        user_tariff = users.get(user, 'cheap')
        billing = conversion['duration'] * plans[user_tariff]
        balance[user] = balance[user] - billing
    
    print(balance)


