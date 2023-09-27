import colorsys

def hex_to_hsl(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = round(h * 360)
    s = round(s * 100)
    l = round(l * 100)
    return (h, s, l)

hex_color_list = []
with open("list1.txt", "r") as file:
    for line in file:
        hex_color_list.append(line.strip())

hsl_color_list = [hex_to_hsl(hex_code) for hex_code in hex_color_list]

for i, hsl in enumerate(hsl_color_list):
    print(hsl)
