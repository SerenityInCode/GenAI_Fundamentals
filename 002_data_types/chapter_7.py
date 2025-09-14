# Tuples

masala_spices=("cloves","cardamom","cinnamon")
(spice1,spice2,spice3)=masala_spices
print(f"Name of Spice 1 is: {spice1}")
print(f"Name of Spice 2 and 3: {spice2},{spice3}")

ginger_ratio,cardamom_ratio=2,1
print(f"Ratio of G:{ginger_ratio} and Ratio of C:{cardamom_ratio}")
ginger_ratio,cardamom_ratio=cardamom_ratio,ginger_ratio
print(f"Ratio of G:{ginger_ratio} and Ratio of C:{cardamom_ratio}")

#Membership testing
print(f"Is cinnamon in Masala spice?: {'Cinnamon' in masala_spices}")  #gives False as it is case sensitive
print(f"Is cinnamon in Masala spice?: {'cinnamon' in masala_spices}")  #gives True 