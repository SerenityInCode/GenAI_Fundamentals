# #walrus operator- :=

# num = 13
# remainder = num % 5

# if remainder:
#     print(f"Not divisible. Remainder is {remainder}")

# value=16
# if remainder:=value % 5 :
#     print(f"Remainder is {remainder}")


# available_sizes = ['small', 'medium', 'large']

# if (requested_size:= input("Choose your cup size: ")) in available_sizes:
#     print(f"Your cup size is: {requested_size}")
# else:
#     print("Unknown cup size")


flavours=['masala', 'ginger', 'lemon', 'mint']
print(f"Available flavours are: {flavours}")

while (flavour:= input("Choose your flavour: ")) not in flavours:
    print(f"Your {flavour} chai is not available!")
    break

print(f"Your {flavour} chai is here:)")
