# List

ingredients=['water','milk','black tea']
ingredients.append('sugar')
print(f"List of ingredients is: {ingredients}")
ingredients.remove("water")
print(f"List of ingredients is: {ingredients}")

# Extending an existing list
spice_options=['ginger','cardamom']
chai_ingredients=['milk','sugar']
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

# Inserting an item
chai_ingredients.insert(2,'black tea')
print(f"Chai ingredients: {chai_ingredients}")

# Removing last item
last_item=chai_ingredients.pop()
print(f"Last item: {last_item}")

print(f"Updated list: {chai_ingredients}")

# Reversing
chai_ingredients.reverse()
print(f"Reversed list is: {chai_ingredients}")

# Sorting
chai_ingredients.sort()
print(f"Sorted list is: {chai_ingredients}")


# Minimum and maximum
sugar_levels=[1,2,3,4,5]
print(f"Maximum level of sugar is: {max(sugar_levels)}")
print(f"Minimum level of sugar is: {min(sugar_levels)}")

#Operators overloading
base_liquid=['water','milk']
flavour=['ginger']
full_liquid_mix=base_liquid+flavour
print(f"Full liquid mix is: {full_liquid_mix}")

strong_brew=['black tea'] * 3
print(f"Strong brew: {strong_brew} ")

# bytearray
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinna",b"Card")
print(f"Bytes: {raw_spice_data}")