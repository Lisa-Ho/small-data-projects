from generativepy.color import Color
from PIL import ImageColor
from matplotlib.colors import rgb2hex

# convert hex color to rgb to Color object (generativepy package)
def hex_to_Color(hexcode):
    rgb = ImageColor.getcolor(hexcode, 'RGB')
    rgb = [v/256 for v in rgb]
    rgb = Color(*rgb)
    return rgb

# create square grid of colours using colour interpolatoin from generativepy package
def get_colorlist(bounds, lb_color, tl_color, lr_color, tr_color):
    c00 = hex_to_Color(lb_color) #lower bottom
    c10 = hex_to_Color(tl_color) #top left
    c01 = hex_to_Color(lr_color) #lower right
    c11 = hex_to_Color(tr_color) #upper right
    c00_to_c10 = []
    c01_to_c11 = []
    colorlist = []

    num_grps = len(bounds)
    for i in range(num_grps):
        c00_to_c10.append(c00.lerp(c10, 1/(num_grps-1) * i))
        c01_to_c11.append(c01.lerp(c11, 1/(num_grps-1) * i))
    for i in range(num_grps):
        for j in range(num_grps):
            colorlist.append(c00_to_c10[i].lerp(c01_to_c11[i], 1/(num_grps-1) * j))
        
    # convert back to hex color
    colorlist = [rgb2hex([c.r, c.g, c.b]) for c in colorlist]
    return colorlist

# get colour for each data value based on two variables (v1,v2) and defined bounds (list)
def get_bivariate_choropleth_color(v1, v2, bounds, colorlist):
    #colorlist = create_color_list(bounds, lb_color, tl_color, lr_color, tr_color)
    if v1>=0 and v2>=0:
        count = 0
        stop = False
        for bound_v1 in bounds:
            for bound_v2 in bounds:
                if (not stop) and (v1 <= bound_v1):
                    if (not stop) and (v2 <= bound_v2):
                        color = colorlist[count]
                        stop = True
                count += 1
    else:
        color = [0.6,0.6,0.6,1]
    return color


