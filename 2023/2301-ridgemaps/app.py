import folium
from folium.plugins import Draw
import streamlit as st
from streamlit_folium import st_folium
from streamlit_image_select import image_select
import json

import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from ridge_map import RidgeMap, FontManager

#========= Page config
st.set_page_config(
    page_title="ridgemapp",
    page_icon="🖼️",
    initial_sidebar_state="collapsed"
    #layout="wide",
     )

#load example styles
with open('map_styles.json', 'r') as json_file:
    map_styles = json.load(json_file)

#========== Functions
def create_map():
    #define variable values depending on input
    figsizedict = {"square": (12,12), "rectangle": (14.8,10.5)}
    titleposdict = {"top left": [.16, .78, "left"], "top right":[.86, .78,  "right"], 
                 "bottom left": [.16, .22, "left"], "bottom right":[.86, .22, "right"] }
    if _bg_transparent == True:
        bg_alpha = 0
    else:
        bg_alpha = 1
    
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
                bg_alpha = bg_alpha,
                #line_color = "Reds",
                background_color = _bgcolor,
                ax=ax,
                linewidth=_linewidth,
               )
    
    #title
    plt.figtext(titleposdict[_title_pos][0], titleposdict[_title_pos][1], _title.upper(), va='top', 
                ha=titleposdict[_title_pos][2],
                fontsize=_title_fontsize, color=_title_color, fontname=_title_font, linespacing=1,
                bbox=dict(facecolor=_bgcolor, linewidth=0, pad=10, alpha=1))

    return fig


#========== APP

st.title('ridgemapp')
st.markdown("## Create your own print ready design")
#========== Sidebar


# ========= Make selection
# Draw rectangle on map and get coordinates to use
st.markdown('Draw an rectangle to select the area to map')
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
    bl = map_selection["last_active_drawing"]["geometry"]['coordinates'][0][0]
    tr = map_selection["last_active_drawing"]["geometry"]['coordinates'][0][2]

#=========== Select style from image
st.markdown('Select style')
captions=["Style1", "Style2", "Style3", "Style4"]
style_id = image_select(
    label="",
    images=[
        "examples/example1.png",
        "examples/example2.png",
        "examples/example3.png",
        "examples/example4.png"
    ],
    captions=captions,
    index = 0,
    return_value ="index"
)
style_selected = map_styles[captions[style_id]]
for key in style_selected.keys():
    st.write(style_selected[key])



# ========== Customise map
with st.form(key="Create map"):
    st.markdown("Customise map style")
    col1, col2 = st.columns([2,1], gap="medium")
    with col1:
        _title = st.text_input("Title (optional)", "")
    with col2:
        _figsize = st.selectbox('Shape',('square', 'rectangle'))

    with st.expander("More style options"):
        st.markdown("**Background**")
        col3a, col3b, col3c = st.columns([1,1,2], gap="small")
        with col3a:
            _bg_transparent = st.checkbox('Transparent',value=False)
        with col3b:
            _bgcolor = st.color_picker("Colour", '#111111', key=0)

        st.markdown("")
        st.markdown("**Title**")
        col3,col4,col5,col6 = st.columns([1.2,1.7,1,1], gap="small")
        with col3:
            _title_pos = st.selectbox('Position',('top left', 'top right', 'bottom left', 'bottom right'))
        with col4:
            _title_font = st.selectbox('Font',('Courier New', 'Lato','Myriad Pro', 'Open Sans', 'Oswald', 'Times New Roman', 'Ubuntu'))
        with col5:
            _title_fontsize = st.slider("Font size", min_value=10, max_value=60, value=35)
        with col6:
            _title_color = st.color_picker('Colour', '#ffffff', key=1)
        
        st.markdown("")
        st.markdown("**Ridge lines**")
        col7,col8,col9 = st.columns([1,1,2], gap="small")
        with col7:
            _num_lines = st.slider("Number of lines", min_value=30, max_value=150, value=80)
        with col8:
            _linewidth = st.slider("Linewidth", min_value=1, max_value=6, value=1)
        with col9:
            _line_color = st.color_picker('Colour', '#ffffff', key=2)
        col10,col11,col12,col13 = st.columns([1,1,1,1], gap="small")
        with col10:
            _elevation_pts = st.slider("Elevation points", min_value=10, max_value=200, value=150, help="The more points, the smoother the ridge lines")
        with col11:
            _vertical_ratio = st.slider("Vertical ratio", min_value=10, max_value=150, value=80, help="How steep or flat hills are displayed")
        with col12:
            _water_ntile = st.slider("Water ntile", min_value=0, max_value=8, value=2, help="Set to 0 if you do not want any water marked")
        with col13:
            _lake_flatness = st.slider("Lake flatness", min_value=0, max_value=8, value=3, help="Set to 0 if you do not want any water marked")

    button_create_map = st.form_submit_button('Update')

if "create_map" not in st.session_state:
    st.session_state.create_map = False
if button_create_map:
        st.session_state.create_map = True

# Create map if button is clicked and area selected
if (st.session_state.create_map) & (map_selection["last_active_drawing"]!= None):
    fig = create_map()
    st.pyplot(fig)
elif ( st.session_state.create_map) & (map_selection["last_active_drawing"]== None):
    st.markdown('**Select area first**')
    fig = "None" 
else:
    fig = "None" 


#export image
if fig != "None":
    plt.savefig("ridgemaps.png", bbox_inches="tight", dpi=300, pad_inches=0, transparent=_bg_transparent)
    with open("ridgemaps.png", "rb") as image:
        png = st.download_button(
            label="Download png",
            data=image,
            file_name="ridgemap.png",
            mime="image/png"
        )
    plt.savefig("ridgemaps.svg", bbox_inches="tight", pad_inches=0)
    with open("ridgemaps.svg", "rb") as svg:
        svg = st.download_button(
            label="Download svg",
            data=svg,
            file_name="ridgemaps.svg"
        )
