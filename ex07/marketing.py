import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def get_call_center():
    return set(clients) - set(recipients)

def get_potential_clients():
    return set(participants) - set(clients)

def get_loyalty_program():
    return set(clients) - set(participants)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit(1)

        
    task = sys.argv[1].strip()

    if task == "call_center":
        result = get_call_center()
    elif task == "potential_clients":
        result = get_potential_clients()
    elif task == "loyalty_program":
        result = get_loyalty_program()
    else:
        print("Unknown task")
        sys.exit(1)

    for email in result:
        print(email)
