#-----------------------------
import math
def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"you'll be needed {cans} for paint the wall")
#-----------------------------
height_int = int(input("Insert the wall's height: "))
width_int = int(input("Insert the wall's width: "))
coverage = 5

paint_calc(height = height_int, width = width_int, cover = coverage)