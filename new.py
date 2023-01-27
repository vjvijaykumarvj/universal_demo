# print the ATM System Management
username = 'vijay'
password = 'vijay'

u_name = input('Enter Username')
p_password = input('Enter Password')

if username == u_name or password ==p_password:
    print("""
    1. Deposite
    2. Withdraw
    3. Mini Statement
    4. Exit
    """)
    amount = 1000
    option = int(input('Enter Option'))
    if option == 1:
        dep = int(input('Enter Amount'))
        amount +=dep
        print('Total Amount',amount)
    elif option == 2:
        withd = int(input('Enter Option'))
        amount -=withd
        print('Total Amount',amount)
    elif option == 3:
        print('#################')
        print('Hello Welcome To ATM')
        print('Username',username)
        print('Total Amount',amount)
        print('Thanks You For Visit')
        print('##################')
    else:
        print('Please select Any Option')