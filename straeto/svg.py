import svgwrite
import random

import os


p = "C:\\Users\\alfgr\\Desktop\\verk\\git_pages\\alfgr.github.io\\straeto\\assets\\test"

if not os.path.exists(p):
    os.makedirs(p)

fill_colors = ["red", "green", "blue", "purple", "orange", "cyan"]

nums = [56,61,62,103,104,105,106,101,63,64,73,78,81,82,84,87,91,92,93,94,95,96,'A1','A4','E1','R1','R3','R4']
for num in nums:
    dwg = svgwrite.Drawing(f"{p}\\{num}.svg", profile='tiny', size=('100px', '100px'))
    circle = dwg.circle(center=(50, 50), r=40, fill=random.choice(fill_colors))
    dwg.add(circle)

    text_x = 35 - (len(str(num)) * 7)  
    text_y = 65  
    text = dwg.text(str(num), insert=(text_x, text_y), font_size=50, fill='white')
    dwg.add(text)

    dwg.save()

print("SVG files with centered numbers and random fill colors generated.")
