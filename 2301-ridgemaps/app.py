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

#========== Function for map creation
def create_map():
    #define variable values depending on input
    figsizedict = {"square": (12,12), "rectangle": (14.8,10.5)}
    titleposdict = {"top left": [.16, .78, "left"], "top right":[.86, .78,  "right"], 
                 "bottom left": [.16, .22, "left"], "bottom right":[.86, .22, "right"] }
    
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
                line_color = _line_color,
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
    
    #plt.savefig("ridgemap.png", bbox_inches='tight', dpi=300, transparent=False, pad_inches=0)
    return fig

# ========== Make selection
# Draw rectangle on map and get coordinates to use
st.markdown('### Select area')
st.markdown("Areas that are too large (e.g. a whole country) might not be able to show")

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


# ========== Create and customise map
st.markdown('### Create map')   
with st.form(key="Create map"):
    col1, col2 = st.columns([2,1], gap="medium")
    with col1:
        _title = st.text_input("Title (optional)", "")
    with col2:
        _figsize = st.selectbox('Map shape',('square', 'rectangle'))
    with st.expander("Customise map style"):

        st.markdown("**Background**")
        _bgcolor = st.color_picker("Colour", '#111111', key=0)
        st.markdown("")
        st.markdown("**Title**")
        col3,col4,col5,col6 = st.columns([1.2,1.7,1,1], gap="small")
        with col3:
            _title_pos = st.selectbox('Position',('top left', 'top right', 'bottom left', 'bottom right'))
        with col4:
            _title_font = st.selectbox('Font',('Courier New', 'Ubuntu'))
        with col5:
            _title_fontsize = st.number_input("Font size", min_value=10, max_value=60, value=35)
        with col6:
            _title_color = st.color_picker('Colour', '#ffffff', key=1)
        st.markdown("")
        st.markdown("**Ridge lines**")
        col7,col8,col9 = st.columns([1,1,1], gap="small")
        with col7:
            _num_lines = st.number_input("Number of lines", min_value=30, max_value=150, value=80)
        with col8:
            _linewidth = st.number_input("Width", min_value=0.1, max_value=8.0, value=1.0)
        with col9:
            _line_color = st.color_picker('Colour', '#ffffff', key=2)

        col10,col11,col12,col13 = st.columns([1,1,1,1], gap="small")
        with col10:
            _elevation_pts = st.number_input("Elevation points", min_value=10, max_value=200, value=150)
        with col11:
            _vertical_ratio = st.number_input("Vertical ratio", min_value=10, max_value=150, value=80)
        with col12:
            _water_ntile = st.number_input("Water ntile", min_value=0, max_value=8, value=2)
        with col13:
            _lake_flatness = st.number_input("Lake flatness", min_value=0, max_value=8, value=3)

    button_create_map = st.form_submit_button('Create map')


if "button_create_map" not in st.session_state:
    st.session_state.button_create_map = False

if button_create_map:
        st.session_state.button_create_map = True

#fig = "None" 

if (st.session_state.button_create_map) & (map_selection["last_active_drawing"]!= None):
    fig = create_map()
    st.pyplot(fig)
elif ( st.session_state.button_create_map) & (map_selection["last_active_drawing"]== None):
    st.markdown('**Select area first**')
    fig = "None" 
else:
    fig = "None" 


#st.write(fig)  
if fig != "None":
    col14,col15,col16 = st.columns([1,1,1], gap="small")
    with col14:
        plt.savefig("ridgemaps.png", bbox_inches="tight", dpi=300, pad_inches=0)
        with open("ridgemaps.png", "rb") as file:
            png = st.download_button(
                label="Download png",
                data=file,
                file_name="ridgemaps.png",
                mime="image/png"
            )
    with col15:
        plt.savefig("ridgemaps.svg", bbox_inches="tight", pad_inches=0)
        with open("ridgemaps.svg", "rb") as file:
            svg = st.download_button(
                label="Download svg",
                data=file,
                file_name="ridgemaps.svg",
                mime="image/png"
            )


test = st.button("test")
if test:
    st.write("test")


