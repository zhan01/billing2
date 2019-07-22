from billing import calculate_balance

if __name__ == '__main__':
    balance = {'Alice': 100, 'Bob': 100, 'Charlie': 5000, 'Eric': 50, 'Fiona': 300}
    plans = {'cheap': 1, 'average': 2, 'expensive': 10}
    users = {'Alice': 'cheap', 'Bob': 'average', 'Charlie': 'expensive', 'Fiona': 'cheap'}
    history = [
    {'user': 'Charlie', 'duration': 50},
    {'user': 'Alice', 'duration': 10},
    {'user': 'Alice', 'duration': 20},
    {'user': 'Bob', 'duration': 2},
    {'user': 'Eric', 'duration': 15},
    ]
    calculate_balance(balance, plans, users, history)
    assert balance == {'Alice': 70, 'Bob': 96, 'Charlie': 4500, 'Eric': 35, 'Fiona': 300}


    balance = {'Alice': 180, 'Bob': 150, 'Charlie': 2000, 'Eric': 600, 'Fiona': 300}
    plans = {'cheap': 1, 'average': 2, 'expensive': 10}
    users = {'Alice': 'cheap', 'Bob': 'average', 'Charlie': 'expensive', 'Fiona': 'cheap'}
    history = [
    {'user': 'Charlie', 'duration': 50},
    {'user': 'Alice', 'duration': 10},
    {'user': 'Alice', 'duration': 20},
    {'user': 'Bob', 'duration': 2},
    {'user': 'Eric', 'duration': 15},
    ]
    calculate_balance(balance, plans, users, history)
    assert balance == {'Alice': 150, 'Bob': 146, 'Charlie': 1500, 'Eric': 585, 'Fiona': 300}


    balance = {'Alice': 100, 'Bob': 100, 'Charlie': 5000, 'Eric': 50, 'Fiona': 300}
    plans = {'cheap': 1, 'average': 2, 'expensive': 10}
    users = {'Alice': 'cheap', 'Bob': 'average', 'Charlie': 'expensive', 'Fiona': 'cheap'}
    history = [
    {'user': 'Charlie', 'duration': 100},
    {'user': 'Alice', 'duration': 100},
    {'user': 'Alice', 'duration': 200},
    {'user': 'Bob', 'duration': 20},
    {'user': 'Eric', 'duration': 150},
    ]
    calculate_balance(balance, plans, users, history)
    assert balance == {'Alice': -200, 'Bob': 60, 'Charlie': 4000, 'Eric': -100, 'Fiona': 300}