import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="London Cycling Rates",
    page_icon="bicyclist",
    #layout="wide",
     )

st.markdown('<style>div.appview-container{background-color: #f7f6f4;}</style>',unsafe_allow_html=True)
st.markdown('<style>div[data-testid="stForm"]{background-color: #fcfbfb;}</style>',unsafe_allow_html=True)
st.markdown('<style>section[data-testid="stSidebar"]{background-color: #dfdedd;}</style>',unsafe_allow_html=True)

st.title('Cycling rates in London')


# ========== DATA & SETUP
# Load data
@st.cache
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/Lisa-Ho/data-a-and-v/main/2210-london-cycling/cycling_rates_london_cleaned_2016-2021.csv")
    return df
    
df = load_data()

# Dictionaries
display_dict = {'E09000007': 'CMD', 'E09000001': 'CTY', 'E09000012': 'HCK', 'E09000013': 'HMS', 'E09000014': 'HGY',
             'E09000019': 'ISL', 'E09000020': 'KNS', 'E09000022': 'LAM', 'E09000023': 'LSH', 'E09000025': 'NWM',
             'E09000028': 'SWR', 'E09000030': 'TOW', 'E09000032': 'WNS', 'E09000033': 'WST', 'E09000002': 'BAR',
             'E09000003': 'BRN', 'E09000004': 'BXL',  'E09000005': 'BRT',  'E09000006': 'BRM',  'E09000008': 'CRD',
             'E09000009': 'ELG',  'E09000010': 'ENF',  'E09000011': 'GRN',  'E09000015': 'HRW',  'E09000016': 'HVG',
             'E09000017': 'HDN',  'E09000018': 'HNS',  'E09000021': 'KNG',  'E09000024': 'MRT',  'E09000026': 'RDB',
             'E09000027': 'RCH',  'E09000029': 'STN',  'E09000031': 'WTH'}


# ========== SIDEBAR
# Customise map
st.sidebar.subheader("Customise visual")

with st.form(key ='Form1'):
    with st.sidebar:
        main_title = st.text_input("Title", "Cycling rates in London")
        title_fontsize = st.number_input("Title fontsize", min_value=10, max_value=35, value=30)
        clr_title = st.color_picker('Title colour', '#184e77')
        clr_background = st.color_picker('Background colour', '#f7f6f4')
        clr_value = st.color_picker('Highlight value colour', '#1e6091')
        clr_line = st.color_picker('Line colour', '#168aad')
        clr_area = st.color_picker('Area colour', '#76c893')
        alpha_area = st.number_input("Area opacity (0=transparent, 1=solid)",min_value=0.00, max_value=1.00, value=0.5)
        submitted = st.form_submit_button('Update map')

# =========== FILTER SELECTIONS

row_0, row_01 = st.columns([1,2])

with st.form(key='columns_in_form'):
    st.markdown('**Change selection**')
    col1, col2 = st.columns(2)
    with col1:
        purpose = st.radio("Cycling purpose",('Any', 'Leisure', 'Travel'))
    with col2:
        frequency = st.radio("Cycling frequency", ('At least once per month', 'At least once per week', 'At least 3 times per week', 'At least 5 times per week'))
    submitted = st.form_submit_button('Update map')

footer = "Source: Active Lives Survey | Design: Lisa Hornung"
subtitle = "Proportion of people cycling " + frequency.lower() + " for " + purpose.lower() + " purpose (%)"

st.write("")

# =========== VISUALISATION

# Map view

## Plotting
#filter data set based on input
data = df[(df["ONS Code"].isin(display_dict.keys())) & (df["Frequency"] == frequency) & 
        (df["Purpose"]==purpose)].reset_index()
data["Display name"] = data["ONS Code"].map(display_dict)

# ========= Layout
# Initialise Figure and define layout
#8,7 | 10, 8.75
layout = [
        ["___","___","___","___","ENF","___","___","___"],
        ["___","___","HRW","BRN","HGY","WTH","___","___"],
        ["HDN","ELG","BRT","CMD","ISL","HCK","RDB","HVG"],
        ["HNS","HMS","KNS","WST","CTY","TOW","NWM","BAR"],
        ["___","RCH","WNS","LAM","SWR","LSH","GRN","BXL"],
        ["___","___","KNG","MRT","CRD","BRM","___","___"],
        ["___","___","___","STN","___","___","___","___"],
        ]
fig,axs = plt.subplot_mosaic(layout, figsize=(12,9), empty_sentinel="___") 
fig.set_facecolor(clr_background)
plt.subplots_adjust(wspace=0.1, hspace=0.1, left=0.05, right=0.95, bottom=0.05, top=0.9)

#=========== Plotting
# plotting boroughs
y_values = ['2016', '2017', '2018','2019', '2020', '2021']        
x_values = [1,2,3,4,5,6]
height = max(data[y_values].max()) + 30

##loop through data
for ax in axs:
    data_filtered = data[data["Display name"]==ax]
        
    #display name of borough
    axs[ax].text(1.05, height-10, ax, fontsize=10, ha="left", va='top', color="#111111")
    
    #plot area chart
    axs[ax].fill_between(x_values, list(data_filtered[y_values].values[0]), zorder=1, color=clr_area, alpha=0.7,
                    linewidth=0)   
    axs[ax].plot(x_values, list(data_filtered[y_values].values[0]), zorder=2, 
             color=clr_line,linewidth=2.5)    
    
    #plot last value dot
    axs[ax].scatter(max(x_values), list(data_filtered[y_values].values[0])[-1], zorder=3,color=clr_line)
    
    #display most recent % value
    axs[ax].text(max(x_values)-0.05, height-7, '{:,.0f}%'.format(list(data_filtered[y_values].values[0])[-1]), 
             ha="right", fontsize=20, fontweight='bold', va='top', color=clr_value)
        
    #format axis
    axs[ax].set_xlim(xmin=0.8, xmax=6.2)
    axs[ax].set_ylim(ymax=height, ymin=0) 
    axs[ax].set_facecolor(clr_background)    
    axs[ax].axis("off")

#============= Legend           
lgd = fig.add_axes([0.82, 0.05, 0.1, 0.1]) #axes to hold legend
lgd.text(1.05,height-3,data["Display name"][0], fontsize=8, ha="left", va='top', color="#111111")
lgd.fill_between(x_values,list(data.loc[0][y_values].values), zorder=1,color="#999999", alpha=0.7,linewidth=0)    
lgd.plot(x_values,list(data.loc[0][y_values].values), zorder=2,color="#333333",linewidth=1.5)    
lgd.scatter(max(x_values),list(data.loc[0][y_values].values)[-1], zorder=3,color="#333333")
lgd.text(max(x_values)-0.05, height-2, '{:,.0f}%'.format(list(data.loc[0][y_values].values)[-1]), 
        ha="right", fontsize=15, fontweight='bold', va='top', color="#333333")
lgd.set_xlim(xmin=0.8, xmax=6.2)
lgd.set_ylim(ymax=height, ymin=0) 
lgd.set_facecolor("#E4E4E4")
for pos in ["top", "bottom", "right", "left"]:
    lgd.spines[pos].set_visible(False)
lgd.set_xticks([1,6], ["2016", "2021"],fontsize = 10)
lgd.set_yticks([])
lgd.annotate('latest\nrate', xy=(max(x_values)+0.3, height-10), xycoords='data', xytext=(10, 0), textcoords='offset points', 
                   fontsize=11, ha='left', va='center', annotation_clip=False,
                    arrowprops=dict(arrowstyle="->",facecolor='black'))
lgd.annotate('borough', xy=(min(x_values)+0.2, height-1), xycoords='data', xytext=(0, 16), textcoords='offset points', 
                   fontsize=11, ha='center', va='center', annotation_clip=False,
                    arrowprops=dict(arrowstyle="->",facecolor='black'))


#=============== Text           
## Add titles and footer
y_pos = 1.05
x_pos = 0.05

fig.text(x_pos, y_pos, main_title, fontsize=title_fontsize, ha='left',va="top",
             fontweight="bold",  color=clr_title)
fig.text(x_pos, y_pos-(title_fontsize*0.2*0.01), subtitle, fontsize=15, ha='left',va="top",
             fontweight="normal",   color="#111111")
fig.text(x_pos, -0.05, footer, fontsize=11, ha='left',va="center",
             fontweight="normal",  linespacing=1.5, color="#111111")


#============ London wide stats
inner = df[(df["Area name"]=="Inner London") & (df["Frequency"]==frequency) & (df["Purpose"]==purpose)]["2021"].iloc[0]
outer = df[(df["Area name"]=="Outer London") & (df["Frequency"]==frequency) & (df["Purpose"]==purpose)]["2021"].iloc[0]
london = df[(df["Area name"]=="London") & (df["Frequency"]==frequency) & (df["Purpose"]==purpose)]["2021"].iloc[0]

fig.text(x_pos, y_pos-0.14,  "Total 2021: " + '{:,.0f}%'.format(london), fontsize=15, ha='left',va="top",
         fontweight="bold",color=clr_value)
fig.text(x_pos, y_pos-0.18, "Inner: " + '{:,.0f}%'.format(inner) + "  |  Outer: " + '{:,.0f}%'.format(outer) , 
         fontsize=11, ha='left',va="top", fontweight="regular",color="#111111")

st.pyplot(fig)


## ======= Download
st.write("")
st.write("")

# download data
csv = data[['ONS Code', 'Area name','2016', '2017', '2018','2019', '2020', '2021']].to_csv(index=False)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='london_cycling_rates_%s_%s.csv' % (purpose.lower(), frequency.lower()),
    mime='text/csv',
)

#download image
plt.savefig("london_cycling_rates.png",bbox_inches="tight", pad_inches=0.2)
with open("london_cycling_rates.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="london_cycling_rates.png",
            mime="image/png"
          )

st.write("")
st.subheader("About")
st.markdown("Data source: [Active Lives Survey 2021](https://www.gov.uk/government/statistics/walking-and-cycling-statistics-england-2021)")
st.markdown("App created by Lisa Hornung. Visit my [website](https://inside-numbers.com/) or follow me on [Github](https://github.com/Lisa-Ho), [Mastodon](https://fosstodon.org/@LisaHornung), [Twitter](https://twitter.com/LisaHornung_).")