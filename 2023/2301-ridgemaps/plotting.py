import matplotlib.pyplot as plt
from ridge_map import RidgeMap, FontManager

def create_map(style_dict, coord_bl, coord_tr):
    #define variable values depending on input
    figsizedict = {"square": (12,12), "rectangle": (14.8,10.5)}
    titleposdict = {"top left": [.165, .78, "left"], "top right":[.855, .78,  "right"], 
                 "bottom left": [.165, .22, "left"], "bottom right":[.855, .22, "right"] }
    if style_dict["bg_transparent"] == True:
        bg_alpha = 0
    else:
        bg_alpha = 1
    
    #===== PLOT
    #Setup figure
    fig,ax = plt.subplots(figsize=figsizedict[style_dict["fig_shape"]])
    fig.set_facecolor(style_dict["bg_color"])
    
    #elevation lines
    rm = RidgeMap(coord_bl + coord_tr, font = "Ubuntu")
    values = rm.get_elevation_data(num_lines=style_dict["num_lines"], elevation_pts=style_dict["elevation_pts"])
    ridges = rm.plot_map(values=rm.preprocess(values=values, vertical_ratio=style_dict["vertical_ratio"], 
                                              water_ntile=style_dict["water_ntile"], lake_flatness=style_dict["lake_flatness"]), 
                kind='elevation',
                label=None,
                line_color = style_dict["line_color"],
                bg_alpha = bg_alpha,
                #line_color = "Reds",
                background_color = style_dict["bg_color"],
                ax=ax,
                linewidth=style_dict["linewidth"],
               )
    
    #title
    _title_pos = style_dict["title_pos"]
    plt.figtext(titleposdict[_title_pos][0], titleposdict[_title_pos][1], style_dict["title"].upper(), va='top', 
                ha=titleposdict[_title_pos][2],
                fontsize=style_dict["title_fontsize"], color=style_dict["title_color"], fontname=style_dict["title_font"], 
                linespacing=1, bbox=dict(facecolor=style_dict["title_bg_color"], linewidth=0, pad=10, alpha=style_dict["title_bg_alpha"]))

    return fig