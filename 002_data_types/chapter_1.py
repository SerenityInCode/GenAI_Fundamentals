# Numbers are immutable
# For the same variable, it gives different referencing id in the memory even though the output you look is changing

sugar_amount=2
print(f"Initial sugar_amount: {id(sugar_amount)}")
sugar_amount=12
print(f"After sugar_amount: {id(sugar_amount)}")
