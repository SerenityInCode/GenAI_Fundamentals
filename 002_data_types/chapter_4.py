# Boolean

is_boiling=True
stir_count=5
total_actions=is_boiling+stir_count   #upcasting
print(f"Total actions: {total_actions}\n")

milk_present=0 #no milk
print(f"Is milk present? : {bool(milk_present)}\n")


water_hot=True
tea_leaves_added=False

can_serve=water_hot and tea_leaves_added
print(f"Can serve Chai?: {can_serve}\n")

# water_hot=True
# tea_leaves_added=True

# can_serve=water_hot and tea_leaves_added
# print(f"Can serve Chai?: {can_serve}\n")

tea_leaves_added=True
ginger_added=False
can_serve=tea_leaves_added or ginger_added
print(f"Can serve Chai? : {can_serve}\n")


milk=True
can_serve= not milk
print(f"Can serve Chai? : {can_serve}")