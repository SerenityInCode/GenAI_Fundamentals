#Set is mutable
# You can add items to it, but it will reference to the same variable with the same id

spice_mix=set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice_mix set: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Garlic")
spice_mix.add("Chillies")
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice_mix set: {spice_mix}")
