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
from plotting import create_map

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

#========== APP

st.title('ridgemapp')
st.markdown("### Create elevation maps in no time")
st.markdown("**Select area > Chose style > Customise > Download > Print and share**")
st.markdown("""---""") 

#========== Sidebar


# ========= Make selection
# Draw rectangle on map and get coordinates to use
st.markdown('Draw an rectangle on the map to select area')
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
st.markdown('Select a style')
captions=["Dark", "Transparent", "Comic", "Flat"]
style_id = image_select(
    label="",
    images=[ "examples/dark.png",
        "examples/transparent.png",
        "examples/comic.png",
        "examples/flat.png"],
    captions=captions,
    index = 0,
    return_value ="index",
    key="style_selected"
)
style_selected = map_styles[captions[style_id]]

# ========== Customise map
style_updated = {}
font_styles = ['Calibri','Cambria','Candara', 'Courier New', 'DejaVu Sans','Ebrima', 'Gabriola','Impact',
             'Lucida Console','Segoe Print', 'Segoe UI', 'Tahoma','Times New Roman', 'Ubuntu', "Verdana"]
title_positions = ['top left', 'top right', 'bottom left', 'bottom right']
fig_shapes = ["square", "rectangle"]

with st.form(key="Create map"):
    style_custom = {}
    st.markdown("Customise map style")
    col1, col2 = st.columns([2,1], gap="medium")
    with col1:
        style_custom["title"] = st.text_input("Title (optional)", style_selected["title"])
    with col2:
        style_custom["fig_shape"] = st.selectbox('Shape',options=fig_shapes,index=fig_shapes.index(style_selected["fig_shape"]) )
    with st.expander("More style options"):
        st.markdown("**Background**")
        col3a, col3b, col3c = st.columns([1,1,2], gap="small")
        with col3a:
            style_custom["bg_transparent"] = st.checkbox('Transparent',value=False)
        with col3b:
            style_custom["bg_color"] = st.color_picker("Colour", style_selected["bg_color"], key=0)

        st.markdown("")
        st.markdown("**Title**")
        col3,col4,col5,col6 = st.columns([1.2,1.7,1,1], gap="small")
        with col3:
            style_custom["title_pos"] = st.selectbox('Position',options=title_positions,index=title_positions.index(style_selected["title_pos"]))
        with col4:
            style_custom["title_font"] = st.selectbox('Font',options=font_styles, index= font_styles.index(style_selected["title_font"] ))
        with col5:
            style_custom["title_fontsize"] = st.slider("Fontsize", min_value=10, max_value=60, value=style_selected["title_fontsize"])
        with col6:
            style_custom["title_color"] = st.color_picker('Colour', style_selected["title_color"], key=1)
        col6a,col6b,col6c = st.columns([1,1.2,2], gap="small")
        with col6a:
            style_custom["title_bg_color"] = st.color_picker('Background colour', style_selected["title_bg_color"], key=2)
        with col6b:
            style_custom["title_bg_alpha"] = st.slider("Background opacity", min_value=0.0, max_value=1.0, value=style_selected["title_bg_alpha"],
            help="0=transparent, 1=solid")
        
        st.markdown("")
        st.markdown("**Ridge lines**")
        col7,col8,col9 = st.columns([1,1,2], gap="small")
        with col7:
            style_custom["num_lines"] = st.slider("Number of lines", min_value=30, max_value=150, value=style_selected["num_lines"])
        with col8:
            style_custom["linewidth"] = st.slider("Linewidth", min_value=1, max_value=6, value=style_selected["linewidth"])
        with col9:
            style_custom["line_color"] = st.color_picker('Colour', style_selected["line_color"], key=3)
        col10,col11,col12,col13 = st.columns([1,1,1,1], gap="small")
        with col10:
            style_custom["elevation_pts"] = st.slider("Elevation points", min_value=10, max_value=200, value=style_selected["elevation_pts"], help="The more points, the smoother the ridge lines")
        with col11:
            style_custom["vertical_ratio"] = st.slider("Vertical ratio", min_value=10, max_value=150, value=style_selected["vertical_ratio"], help="How steep or flat hills are displayed")
        with col12:
            style_custom["water_ntile"] = st.slider("Water ntile", min_value=0, max_value=8, value=style_selected["water_ntile"], help="Set to 0 if you do not want any water marked")
        with col13:
            style_custom["lake_flatness"] = st.slider("Lake flatness", min_value=0, max_value=8, value=style_selected["lake_flatness"], help="Set to 0 if you do not want any water marked")

    button_update_map = st.form_submit_button('Update')
st.markdown('Your ridgemap design! :point_down: :tada:')

# ========== Manage session states
#st.markdown("Button: " + str(button_update_map))
#map updates
if "update_map" not in st.session_state:
    st.session_state.update_map = False
if (st.session_state.style_selected) & (button_update_map==False):
   st.session_state.update_map = False
if button_update_map:
    st.session_state.update_map = True

#st.markdown("Session state: " + str(st.session_state.update_map))

# Create map when area selected and update with custom map styles
if (st.session_state.update_map == False) & (map_selection["last_active_drawing"]!= None):
    style = style_selected
    fig = create_map(style, bl, tr)
    st.pyplot(fig)
elif (st.session_state.update_map) & (map_selection["last_active_drawing"]!= None):
    style = style_custom
    fig = create_map(style, bl, tr)
    st.pyplot(fig)
elif (st.session_state.update_map) & (map_selection["last_active_drawing"]== None):
    st.markdown('**Select area first**')
    fig = "None" 
else:
    fig = "None" 

#export image
if fig != "None":
    plt.savefig("ridgemaps.png", bbox_inches="tight", dpi=300, pad_inches=0, transparent=style["bg_transparent"])
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
