height, radius = input().split(" ")
height = float(height)
radius = float(radius)

volume = 3.1415926536 * radius * radius * height

print("{:.2f}".format(volume) + " cubic inches")