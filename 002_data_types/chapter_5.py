import sys
from decimal import Decimal
from fractions import Fraction

ideal_temp=95.5
current_temp=95.4999999999

print(f"Ideal temperature is: {ideal_temp}")
print(f"Current temperature is: {current_temp}")
print(f"Difference temperature is: {ideal_temp - current_temp}")
print(sys.float_info)