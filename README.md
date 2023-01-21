# Small data analysis and viz projects

Repository for small-ish analysis and data viz projects. 

### 12/2021 UK Charities and their activities

Analysis using a new dataset that classifies and tags all active and inactive charities in the UK according to their activity/sector. This analysis explores how number of charities in specific activities have changed, whether specific sectors were more "trendy" at some point and whether others have died out. First time doing a streamgraph in python. Data available [here](https://charityclassification.org.uk/data/data-downloads/). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2112-charity-class/notebooks/Charity-classification-analysis.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187970817-49afe9b8-abb5-4560-a7ef-c2d2897176a5.png" width="550">

### 03/2022 Star Wars characters

Been playing around with some Star Wars data using [SWAPI](https://t.co/KSn5X00PmE) and found a great template for making nice looking tables in [matplotlib](https://matplotlib.org/matplotblog/posts/how-to-create-custom-tables/). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2203-starwars-table/notebooks/most-popular-characters-table-viz.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187971376-06c19d63-4133-4537-8d24-3779935cd7b6.png" width="450">

### 04/2022 Sourdough Google searches

First time using a new library ([pytrends](https://pypi.org/project/pytrends/)) to pull data from the Google Search API. Following a [blog I wrote](https://inside-numbers.com/kneading-to-relax-exploring-lockdown-baking-trends) last year on sourdough baking, was curious if interest in sourdough was only a peak during the pandemic or remained high.

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2204-sourdough-google-trends/sourdough-google-trends-2019-2022.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187973494-33df8246-ee3f-467c-a090-e7a94771acce.png" width="450">

### 04/2022 Google searches of 'bike' across Europe

Another project using Google Search API to look at Google searches of 'bike' across Europe before & since the pandemic. Not much change in Scandinavia but higher interest in some countries suggesting a new normal? 🚲📈 

Heavily inspired by Google Trends [The New Normal](http://thenewnormal.is).

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2204-bike-europe-google-trends/bike-searches-pandemic-europe.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187972006-03a0b617-79bf-4716-8fcc-d82aa0d5185b.png" width="450">

### 04/2022 Cycling rates in London

Been looking at London cycling rates and found rates of regular cyclists are higher in inner + SW London. Latest data ending Nov 2020 shows increases in some boroughs since the pandemic. Data sourced from [Active Life Survey](https://www.gov.uk/government/statistical-data-sets/walking-and-cycling-statistics-cw). The map layout is based on the squared map from the [London Data Store](https://data.london.gov.uk/dataset/excel-mapping-template-for-london-boroughs-and-wards). Checkout [my Twitter thread](https://twitter.com/LisaHornung_/status/1514551012694102018?s=20&t=kroA3czupkueRsOOz1DlTw) to see how it's put together. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2204-prop-cycling-London-borough/cycling-rates-london-grid-tile-map.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187972669-bcd007ef-b0ec-46e9-8ae3-d765be3668d6.png" width="550">

### 07/2022 Gender pay gap (WIP)

Triggered by #TidyTuesday, got my hands on some gender pay gap data again. Worked up a couple of charts but wasn't too convinced where this was going. Wanted to focus on Tech vs charities, but haven't fully managed to do that yet. Was focused on trying out some new chart types, including beeswarm and ridge line plots. Might pick it up another time. Data comes from the [TidyTuesday repository](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-06-28). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2207-gender-pay-gap/GenderPayGap.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187974455-73488cdf-e77b-4413-8684-2bd19e24e465.png" width="550">

### 08/2022 Exploring OSMnx for mapping in python

Discovered [OSMnx](https://osmnx.readthedocs.io/en/stable/), a python library to easily extract geospatial data from OpenStreetMaps. Explored a few different ways to extract and display data. Definitely quite a powerful tool. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2208-OSMnx/Exploring-osmnx.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213873819-8f1f6d6a-01b2-4985-8e50-15c0b76c14ad.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213873848-24580d8f-7af0-436e-86b4-2b33eb29cb37.png" height="250">

### 10/2022 Cycling in London

Continued playing around with cycling data for London. Updated the tilegrid map and created a few more charts. Definitely getting better at customising charts in matplotlib and using different chart types. Also turned the tile grid map into a Streamlit app (live app available [here](https://liloho-london-cycling-rates-app-kgvppz.streamlit.app/)).

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2210-london-cycling/london_cycling_rates_exploration.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213873978-e80b3788-3e8c-46c4-b34e-df7cd5c5f624.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213873988-6559bea2-7b41-4cdb-98a6-9e7b1d269866.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213874002-72192250-c7a7-4eb9-8917-18f412e13564.png" height="250">


### 01/2023 Cultural venues in London

Follow up from maps I created as part of the #30DayMapChallenge 2022. Fun to play around with fishnet grids in python and created some maps that display aggregate data per square km (here: cultural venues in London). Definitely something I'll come back to at some point.

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2301-culture-venues-london/cultural-venues-london-maps.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213877655-1c1503a5-33dc-4fb4-b455-60203ea47fa4.png" width="550">


