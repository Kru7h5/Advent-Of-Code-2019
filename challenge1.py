"""
-- Fuel required --
fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

# Libraries:
import math as m

def DoubleChecker(tot, fuel):
    if fuel <= 0:
        return (tot)
    else:
        tot+=fuel
        return DoubleChecker(tot, (m.floor(int(fuel)/3) - 2))

# mass of each module stored in input1.txt
masses = open("input1.txt", "r")
FuelCounterUpper = 0
for mass in masses:
    FuelCounterUpper += DoubleChecker(0,(m.floor(int(mass)/3) - 2))
print(FuelCounterUpper)