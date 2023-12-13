import sys
from madrid.natural import natural

# example
# run_madrid_natural.py 3 1000 /home/goat/projects/geospatial_svg/data/Madrid-shp/shape/natural.shp madrid/style.css xxx.svg -4.0 40.3

if len(sys.argv) < 8:
    print('provide args')
# Set the Python function arguments from the command line values provided
item_scale = int(sys.argv[1])
group_scale = int(sys.argv[2])
data_path = sys.argv[3]
style_path = sys.argv[4]
destination_path = sys.argv[5]
center_x = sys.argv[6]
center_y = sys.argv[7]

file = open(style_path, 'r', encoding='utf-8')
style_def = file.read()
svg_tag = natural(
    item_scale, group_scale,
    data_path, style_def,
    center_x, center_y
)
if svg_tag:
    file = open(destination_path, 'w')
    file.write(svg_tag)
    print('File created: ', file)
else:
    print('No file created')