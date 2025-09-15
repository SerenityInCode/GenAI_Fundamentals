#continue- if skips the loop
#break- breaks out of the loop
flavours = ['Ginger', 'Out of Stock', 'Lemon', 'Discontinued', 'Tulsi']

for flavour in flavours:
    # print(f"{flavour} is found")
    if flavour == 'Out of Stock':
        continue
    if flavour == 'Discontinued':
        break
    print(f"{flavour} item found")
    
print("Outside the loop")    