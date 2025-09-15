names=['Manisha', 'Bhavya', 'Nidhi', 'Aish']
bills=[50, 80, 45, 60]

for name,amount in zip(names,bills):          #zip combines list
    print(f"{name} paid {amount} rupees!")