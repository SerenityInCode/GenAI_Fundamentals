chai_order={"type" : "Masala Chai", "size" : "large", "sugar_level" : 2}
print(f"Chai order is: {chai_order}")

chai_recipe={}
chai_recipe['base'] = 'black_tea'
chai_recipe['liquid'] = 'milk'

print(f"Recipe base: {chai_recipe['base']}")
print(f"Chai recipe is: {chai_recipe}")
del chai_recipe['liquid']
print(f"Chai recipe is: {chai_recipe}")

#membership testing
print(f" Is sugar in the order?: {'sugar_level' in chai_order}")

chai_order = {'type':'Ginger Chai', 'size' : 'medium', 'customer_note' : 'Please add more sugar!','sugar_level' : 3}
print(f"Order Details (keys): {chai_order.keys()}")
print(f"Order Details (values): {chai_order.values()}")
print(f"Order Details (items): {chai_order.items()}")

#remove last item
last_item = chai_order.popitem()
print(f"Removed last item is: {last_item}")

#updating dictionary 
extra_spices={'cardamom': 'crushed', 'ginger' : 'sliced'}
chai_order.update(extra_spices)
print(f"Updated chai order is: {chai_order}")

#get()
note = chai_order.get("customer_note","No note:(")
print(f"Customer note is : {note}")