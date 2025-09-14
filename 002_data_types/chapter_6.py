# Strings

chai_type="Ginger chai"
customer_name="Priya"
print(f"Order for {customer_name}: {chai_type} please!!")

chai_description="Aromatic and bold"
print(f"First word is: {chai_description [0:8]}")
print(f"Second word is: {chai_description[12:]}")
print(f"Between word is: {chai_description[8:12:1]}")
print(f"Every second letter is: {chai_description[0::2]}")
print(f"Reverse order of chai_description is: {chai_description[::-1]}")

label_text="Qué tal"
encoded_label=label_text.encode("utf-8")
print(f"No encoded text is: {label_text}")
print(f"Encoded text is: {encoded_label}")
decoded_label=encoded_label.decode("utf-8")
print(f"Decoded label is: {decoded_label}")