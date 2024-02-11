import math

material, surface = input().split()

coefficient = 0

if surface == "CONCRETE":
    if material == "RUBBER":
        coefficient = 0.90
    elif material == "WOOD":
        coefficient = 0.62
    elif material == "STEEL":
        coefficient = 0.57
elif surface == "WOOD":
    if material == "RUBBER":
        coefficient = 0.80
    elif material == "WOOD":
        coefficient = 0.42
    elif material == "STEEL":
        coefficient = 0.30
elif surface == "STEEL":
    if material == "RUBBER":
        coefficient = 0.70
    elif material == "WOOD":
        coefficient = 0.30
    elif material == "STEEL":
        coefficient = 0.74
elif surface == "RUBBER":
    if material == "RUBBER":
        coefficient = 1.15
    elif material == "WOOD":
        coefficient = 0.80
    elif material == "STEEL":
        coefficient = 0.70
elif surface == "ICE":
    if material == "RUBBER":
        coefficient = 0.15
    elif material == "WOOD":
        coefficient = 0.05
    elif material == "STEEL":
        coefficient = 0.03

slope = round(math.degrees(math.atan(coefficient)), 1)

print(f"{coefficient:.2f} {slope}")