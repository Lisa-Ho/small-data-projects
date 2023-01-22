import folium
from folium.plugins import Draw
import streamlit as st
from streamlit_folium import st_folium

import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from ridge_map import RidgeMap

st.set_page_config(
    page_title="RidgeMaps",
    page_icon="bicyclist",
    #layout="wide",
     )
st.title('RidgeMaps')

# ========== Make selection
# Draw rectangle on map and get coordinates to use
st.write("Select an area to map")

m = folium.Map()
Draw(draw_options={
                "polyline": False,
                "rectangle": True,
                "circle": False,
                "circlemarker": False,
                "marker":False,
                "polygon":False
            }).add_to(m)

map_selection = st_folium(m, width=800, height=450)
if map_selection["last_active_drawing"]!= None:
    #st.write(output["last_active_drawing"])
    bl = map_selection["last_active_drawing"]["geometry"]['coordinates'][0][0]
    tr = map_selection["last_active_drawing"]["geometry"]['coordinates'][0][2]
    st.write("bottom left", bl)
    st.write("top right", tr)


    
    #===== USER INPUTS
    #figure
    _figsize = "rectangle"
    _bgcolor = "#111111"
    
    #elevation lines
    _num_lines = 80
    _elevation_pts = 200
    _vertical_ratio = 80
    _water_ntile = 2
    _lake_flatness = 3
    _linewidth = 1
    
    #title
    _title = 'English\nChannel'
    _title_pos = "top right"
    _title_fontsize = 35
    _title_font = "Courier New"
    _title_color = "white"
    
    #define variable values depending on input
    figsizedict = {"square": (12,12), "rectangle": (12,9)}
    titleposdict = {"top left": [.16, .78, "left"], "top right":[.86, .78,  "right"], 
                 "bottom left": [.16, .22, "left"], "bottom right":[.86, .22, "right"] }
    
    
    #plt.get_cmap("Reds_r")
    
    
    #===== PLOT
    #Setup figure
    fig,ax = plt.subplots(figsize=figsizedict[_figsize])
    fig.set_facecolor(_bgcolor)
    
    #elevation lines
    rm = RidgeMap(bl + tr, font = "Ubuntu")
    values = rm.get_elevation_data(num_lines=_num_lines, elevation_pts=_elevation_pts)
    ridges = rm.plot_map(values=rm.preprocess(values=values, vertical_ratio=_vertical_ratio, 
                                              water_ntile=_water_ntile, lake_flatness=_lake_flatness), 
                kind='elevation',
                label=None,
                line_color = "white",
                #line_color = "Reds",
                background_color = _bgcolor,
                ax=ax,
                linewidth=_linewidth,
               )
    
    #title
    plt.figtext(titleposdict[_title_pos][0], titleposdict[_title_pos][1], _title.upper(), va='top', 
                ha=titleposdict[_title_pos][2],
                fontsize=_title_fontsize, color=_title_color, fontname=_title_font, linespacing=1.5,
                bbox=dict(facecolor=_bgcolor, linewidth=0, pad=10, alpha=1))
    
    #plt.savefig("english-channel.png", bbox_inches='tight', dpi=300, transparent=False, pad_inches=0)
    
    st.pyplot(fig)